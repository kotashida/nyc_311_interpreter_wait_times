
import pandas as pd

SLA_THRESHOLD_SECONDS = 60

def calculate_requests_by_language(df):
    """Calculates the total number of requests by language."""
    return df.groupby('language').size().reset_index(name='request_count')

def calculate_median_wait_time(df):
    """Calculates the median wait time by language."""
    return df.groupby('language')['connect_time_sec'].median().reset_index(name='median_wait_time')

def calculate_sla_compliance(df):
    """Calculates SLA compliance by language."""
    df['sla_compliant'] = df['connect_time_sec'] <= SLA_THRESHOLD_SECONDS
    sla_compliance = df.groupby('language')['sla_compliant'].mean().reset_index(name='sla_compliance_rate')
    sla_compliance['sla_compliance_rate'] = sla_compliance['sla_compliance_rate'] * 100
    return sla_compliance

def calculate_borough_breakdown(df):
    """Calculates the number of service requests by borough."""
    return df.groupby('borough').size().reset_index(name='request_count')

def calculate_repeat_request_rate(df):
    """Calculates the repeat request rate."""
    repeat_rate = (1 - df['unique_key'].nunique() / len(df)) * 100
    return pd.DataFrame([{'repeat_request_rate': repeat_rate}])

def run():
    """
    Loads the processed data, calculates KPIs, and saves them to CSV files.
    """
    print("Starting KPI calculation...")

    # Load processed data
    try:
        df_service_requests = pd.read_parquet("data/processed/service_requests.parquet")
        df_interpreter_wait_times = pd.read_parquet("data/processed/interpreter_wait_times.parquet")
    except FileNotFoundError as e:
        print(f"Error: {e}. Please run the transformation script first.")
        return

    # Calculate KPIs
    requests_by_language = calculate_requests_by_language(df_interpreter_wait_times)
    median_wait_time = calculate_median_wait_time(df_interpreter_wait_times)
    sla_compliance = calculate_sla_compliance(df_interpreter_wait_times)
    borough_breakdown = calculate_borough_breakdown(df_service_requests)
    repeat_request_rate = calculate_repeat_request_rate(df_service_requests)

    # Save KPIs to CSV
    requests_by_language.to_csv("output/kpi_data/requests_by_language.csv", index=False)
    median_wait_time.to_csv("output/kpi_data/median_wait_time.csv", index=False)
    sla_compliance.to_csv("output/kpi_data/sla_compliance.csv", index=False)
    borough_breakdown.to_csv("output/kpi_data/borough_breakdown.csv", index=False)
    repeat_request_rate.to_csv("output/kpi_data/repeat_request_rate.csv", index=False)

    print("KPI calculation finished.")

if __name__ == "__main__":
    run()
