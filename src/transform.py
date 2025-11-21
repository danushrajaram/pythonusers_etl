import pandas as pd
import pycountry_convert as pc

def normalize_gender(g):
    if isinstance(g,str):
        if g.strip()=="Man": return "MAN"
        if g.strip()=="Woman": return "WOMAN"
    return "OTHERS"

def country_to_continent(country):
    try:
        cc = pc.country_name_to_country_alpha2(country)
        return pc.country_alpha2_to_continent_code(cc)
    except:
        return None

def transform(df):
    print("🧹 Cleaning & transforming...")

    df["Age1stCode"] = pd.to_numeric(df["Age1stCode"], errors="coerce")
    df["ConvertedComp"] = pd.to_numeric(df["ConvertedComp"], errors="coerce")

    df["KnowsPython"] = df["LanguageWorkedWith"].str.contains("Python", na=False)
    df["GenderNorm"] = df["Gender"].apply(normalize_gender)
    df["Continent"] = df["Country"].apply(country_to_continent)
    df["JobSat"] = df["JobSat"].apply(convert_satisfaction)
    df["CareerSat"] = df["CareerSat"].apply(convert_satisfaction)

    return df

JOB_MAP = {
    "Very satisfied": 5,
    "Slightly satisfied": 4,
    "Neither satisfied nor dissatisfied": 3,
    "Slightly dissatisfied": 2,
    "Very dissatisfied": 1
}

def convert_satisfaction(value):
    return JOB_MAP.get(value, None)

