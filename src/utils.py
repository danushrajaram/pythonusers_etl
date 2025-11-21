import pandas as pd

def normalize_gender(value: str):
    if pd.isna(value):
        return "OTHERS"

    value = value.strip().lower()

    if value == "man" or value == "male":
        return "MAN"
    if value == "woman" or value == "female":
        return "WOMAN"

    return "OTHERS"
