
import pandas as pd

def run():
    """
    Validates the raw service requests data.
    """
    print("Starting data validation...")
    
    try:
        df = pd.read_parquet("data/raw/service_requests.parquet")
    except FileNotFoundError:
        print("Error: data/raw/service_requests.parquet not found. Please run the ingestion script first.")
        return

    # Validation checks
    print(f"Validating {len(df)} records...")
    
    # 1. Check for null unique_key
    null_keys = df['unique_key'].isnull().sum()
    if null_keys > 0:
        print(f"Warning: Found {null_keys} records with null unique_key.")
    
    # 2. Check date formats (simple check for now)
    for col in ['created_date', 'closed_date']:
        if col in df.columns:
            try:
                pd.to_datetime(df[col], errors='raise')
            except Exception as e:
                print(f"Warning: Column {col} has invalid date formats: {e}")

    # 3. Check for consistent borough values
    if 'borough' in df.columns:
        known_boroughs = ['MANHATTAN', 'BRONX', 'BROOKLYN', 'QUEENS', 'STATEN ISLAND', 'Unspecified']
        unknown_boroughs = df[~df['borough'].isin(known_boroughs)]
        if not unknown_boroughs.empty:
            print(f"Warning: Found {len(unknown_boroughs)} records with unknown boroughs.")

    print("Data validation finished.")

if __name__ == "__main__":
    run()
