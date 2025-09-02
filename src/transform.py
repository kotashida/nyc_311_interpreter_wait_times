
import pandas as pd

def transform_service_requests(df):
    """Transforms the service requests dataframe."""
    df['created_date'] = pd.to_datetime(df['created_date'], errors='coerce')
    df['closed_date'] = pd.to_datetime(df['closed_date'], errors='coerce')
    df['borough'] = df['borough'].str.lower()
    return df

def transform_interpreter_wait_times(df):
    """Transforms the interpreter wait times dataframe."""
    df.rename(columns={'call_time': 'call_datetime'}, inplace=True)
    df['call_datetime'] = pd.to_datetime(df['call_datetime'], errors='coerce')
    df['language'] = df['language'].str.lower()
    df['connect_time_sec'] = pd.to_numeric(df['connect_time_sec'], errors='coerce')
    return df

def run():
    """
    Loads the raw data, transforms it, and saves it to the processed data folder.
    """
    print("Starting data transformation...")

    # Load raw data
    try:
        df_service_requests = pd.read_parquet("data/raw/service_requests.parquet")
        df_interpreter_wait_times = pd.read_parquet("data/raw/interpreter_wait_times.parquet")
    except FileNotFoundError as e:
        print(f"Error: {e}. Please run the ingestion script first.")
        return

    # Transform data
    df_service_requests_transformed = transform_service_requests(df_service_requests)
    df_interpreter_wait_times_transformed = transform_interpreter_wait_times(df_interpreter_wait_times)

    # Save processed data
    df_service_requests_transformed.to_parquet("data/processed/service_requests.parquet", index=False)
    df_interpreter_wait_times_transformed.to_parquet("data/processed/interpreter_wait_times.parquet", index=False)

    print("Data transformation finished.")

if __name__ == "__main__":
    run()
