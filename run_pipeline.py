from src import ingest, validate, transform, calculate_kpis, generate_excel, generate_ppt

def run_pipeline():
    """Runs the entire data pipeline."""
    ingest.run()
    validate.run()
    transform.run()
    calculate_kpis.run()
    generate_excel.run()
    generate_ppt.run()

if __name__ == "__main__":
    run_pipeline()