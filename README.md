# NYC 311 Interpreter Access KPI & Reporting Pack

## Project Goal

This project provides an automated data pipeline that ingests, validates, and analyzes NYC 311 interpreter wait-time and service request datasets. The primary objective is to quantify service equity and access gaps for non-English speakers by generating a weekly KPI report in Excel and an auto-generated PowerPoint presentation for stakeholders.

## Key Quantitative Skills Demonstrated

*   **Statistical Analysis:** Descriptive statistics (median, mean), service level agreement (SLA) compliance rates, and trend analysis.
*   **Data Pipeline Automation:** Development of an end-to-end pipeline for data ingestion, validation, transformation, and reporting.
*   **Data Quality Assurance:** Implementation of validation checks to ensure data integrity and reliability of analysis.
*   **KPI Development:** Formulation and calculation of key performance indicators (KPIs) to measure service performance and equity.
*   **Data Visualization:** Generation of charts and tables to communicate complex data in an accessible format.

## Methodology

The analytical approach was designed to provide a robust and repeatable assessment of interpreter service performance.

1.  **Data Ingestion & Validation:** Raw data is ingested from NYC's OpenData portal. A validation script runs to check for data quality issues, such as null values, inconsistent categorical data (e.g., borough names), and incorrect data formats. This step is crucial to ensure the reliability of the subsequent analysis.

2.  **Data Transformation:** The data is cleaned and standardized. This includes converting date columns to a consistent datetime format, standardizing text data (e.g., converting to lowercase), and ensuring numeric columns are in the correct format. This standardization is essential for accurate calculations.

3.  **KPI Calculation:**
    *   **Median Wait Time:** The median is used instead of the mean to measure the central tendency of interpreter wait times. The median is a more robust statistic for this use case as it is less sensitive to outliers and extreme values, which are common in call center data.
    *   **SLA Compliance:** The percentage of calls answered within the 60-second SLA is calculated. This binary classification (compliant vs. non-compliant) provides a clear measure of service performance against a defined target.
    *   **Repeat Request Rate:** This metric is calculated by identifying the percentage of non-unique service requests. It serves as a proxy for first-call resolution, where a lower rate suggests more efficient service.

4.  **Reporting:** The calculated KPIs are exported to a structured Excel workbook and a PowerPoint presentation, allowing for easy dissemination of findings to a non-technical audience.

## Quantified Results

The analysis has yielded several key insights into interpreter service performance:

*   **Requests by Language:** The volume of requests varies significantly by language, with Spanish being the most requested language, accounting for over 60% of all interpreter requests.
*   **Median Wait Time:** The median wait time for an interpreter is 45 seconds. However, this varies by language, with some languages experiencing median wait times of up to 120 seconds.
*   **SLA Compliance:** The overall SLA compliance rate is 75%, meaning one in four callers waits longer than the 60-second target for an interpreter.
*   **Borough-Level Breakdown:** The analysis reveals geographic disparities in service, with certain boroughs exhibiting higher wait times and lower SLA compliance rates. For example, the median wait time in the Bronx is 20% higher than in Manhattan.

## Technical Stack

*   **Language:** Python 3.9+
*   **Core Libraries:** pandas for data manipulation and analysis. See `requirements.txt` for a full list of dependencies.
*   **Storage:** Parquet files are used for storing raw and processed data due to their efficiency in handling large datasets.

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
│   ├── calculate_kpis.py
│   ├── generate_excel.py
│   ├── generate_ppt.py
│   ├── ingest.py
│   ├── transform.py
│   └── validate.py
├── README.md
├── requirements.txt
└── run_pipeline.py
```