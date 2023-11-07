import pandas as pd
import glob

filepaths = glob.glob("invoices/*.xlsx")

for filepaths in filepaths:
    df = pd.read_excel(filepaths, sheet_name="Sheet 1")
    print(df)
