
import pandas as pd
import os

def run():
    """
    Generates an Excel report from the KPI data.
    """
    print("Generating Excel report...")

    kpi_dir = "output/kpi_data"
    excel_writer = pd.ExcelWriter("output/kpi_report.xlsx", engine='openpyxl')

    for filename in os.listdir(kpi_dir):
        if filename.endswith(".csv"):
            sheet_name = os.path.splitext(filename)[0]
            df = pd.read_csv(os.path.join(kpi_dir, filename))
            df.to_excel(excel_writer, sheet_name=sheet_name, index=False)

    excel_writer.close()
    print("Excel report generated successfully.")

if __name__ == "__main__":
    run()
