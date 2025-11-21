import pandas as pd

RAW_DATA = "data/raw/survey_results_public.csv"

def extract_raw():
    print("📥 Extracting raw dataset...")
    df = pd.read_csv(RAW_DATA, low_memory=False)
    print("✔ Loaded", len(df), "rows")
    return df
