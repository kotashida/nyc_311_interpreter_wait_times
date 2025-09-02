
import pandas as pd
import requests
from datetime import datetime, timedelta

def fetch_data(url, params):
    """Fetches data from a SODA API endpoint."""
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def run():
    """
    Ingests data from the last 7 days from NYC OpenData and saves it to raw parquet files.
    """
    print("Starting data ingestion...")
    # Define data sources
    sources = {
        "service_requests": {
            "url": "https://data.cityofnewyork.us/resource/erm2-nwe9.json",
            "id_col": "unique_key"
        },
        "interpreter_wait_times": {
            "url": "https://data.cityofnewyork.us/resource/dzvt-6g3v.json",
            "id_col": "case_id"
        }
    }

    # Define date range for the query (last 7 days)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    
    for name, source in sources.items():
        print(f"Fetching {name}...")

        if name == "interpreter_wait_times":
            date_column = "call_time"
            date_filter = f"{date_column} > '{start_date.strftime('%Y-%m-%dT%H:%M:%S.000')}'"
        else:
            date_column = "created_date"
            date_filter = f"{date_column} between '{start_date.strftime('%Y-%m-%dT%H:%M:%S.000')}' and '{end_date.strftime('%Y-%m-%dT%H:%M:%S.000')}'"

        params = {
            "$where": date_filter,
            "$limit": 50000  # Set a high limit to get all data for the week
        }
        data = fetch_data(source["url"], params)

        if data:
            df = pd.DataFrame(data)
            if not df.empty:
                # Save to raw parquet file
                file_path = f"data/raw/{name}.parquet"
                df.to_parquet(file_path, index=False)
                print(f"Successfully saved {len(df)} records to {file_path}")
            else:
                print(f"No data returned for {name} for the given date range.")
        else:
            print(f"Failed to fetch data for {name}.")

    print("Data ingestion finished.")

if __name__ == "__main__":
    run()
