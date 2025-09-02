# NYC 311 Interpreter Access KPI & Reporting Pack

## Project Goal

This project provides an automated pipeline that ingests NYC 311 interpreter wait-time and service request datasets, validates and standardizes the data, and produces a weekly Excel KPI workbook and an auto-generated PowerPoint deck to highlight service equity and access gaps.

## Core Metrics & KPIs

- **Requests by Language:** Total volume of service requests categorized by the language of the interpreter.
- **Median Wait Time:** Median time an individual waits for an interpreter, filterable by language and borough.
- **SLA Compliance:** Percentage of calls answered within the target Service Level Agreement (SLA) time.
- **Borough-Level Breakdown:** Geospatial and tabular breakdown of all KPIs by NYC borough.
- **Repeat Request Rate:** Percentage of requests that are duplicates or repeat calls for the same issue.
- **Weekly Trends:** Week-over-week comparison of key metrics like volume, wait time, and SLA compliance.

## Technical Stack

- **Language:** Python 3.9+
- **Core Libraries:** See `requirements.txt`
- **Storage:** Parquet files for raw and processed data.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/kotashida/nyc_311_interpreter_wait_times
    ```
2.  Navigate to the project directory:
    ```bash
    cd nyc_311_interpreter_wait_times
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the entire pipeline, execute the `run_pipeline.py` script:

```bash
python run_pipeline.py
```

This will perform the following steps:

1.  **Ingest:** Download the latest data from the NYC OpenData portal.
2.  **Validate:** Perform data quality checks.
3.  **Transform:** Clean and standardize the data.
4.  **Calculate KPIs:** Compute the key performance indicators.
5.  **Generate Reports:** Create an Excel workbook and a PowerPoint presentation in the `output` directory.

## Project Structure

```
├── data
│   ├── processed
│   └── raw
├── output
│   ├── charts
│   └── kpi_data
├── src
│   ├── __pycache__
│   ├── calculate_kpis.py
│   ├── generate_excel.py
│   ├── generate_ppt.py
│   ├── ingest.py
│   ├── transform.py
│   └── validate.py
├── project_plan.md
├── README.md
├── requirements.txt
└── run_pipeline.py
```
