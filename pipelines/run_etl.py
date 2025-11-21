import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.extract import extract_raw
from src.transform import transform
from src.load import load_processed

print("\n🚀 RUNNING ETL PIPELINE\n")

df = extract_raw()
df = transform(df)
load_processed(df)

print("\n✅ ETL DONE! cleaned_survey.csv CREATED.\n")
