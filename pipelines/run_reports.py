import pandas as pd
from pathlib import Path

df = pd.read_csv("data/processed/cleaned_survey.csv")

OUT = Path("data/reports")
OUT.mkdir(exist_ok=True)

# 1️⃣ Avg Age
pd.DataFrame({"avg_age":[df["Age1stCode"].mean()]}).to_csv(
    OUT/"avg_age_first_code.csv", index=False)

# 2️⃣ Python %
(df.groupby("Country")["KnowsPython"].mean()*100).to_csv(
    OUT/"python_pct_country.csv")

# 3️⃣ Avg Salary
df.groupby("Continent")["ConvertedComp"].mean().to_csv(
    OUT/"avg_salary_continent.csv")

# 4️⃣ Most desired language
langs = df["LanguageDesireNextYear"].dropna().str.split(";").explode()
langs.value_counts().to_csv(OUT/"desired_lang_2020.csv")

# 5️⃣ Hobby users
(df.groupby(["GenderNorm","Continent"])["Hobbyist"].value_counts(normalize=True))\
 .to_csv(OUT/"hobby_gender_continent.csv")

# 6️⃣ Satisfaction
(df.groupby(["GenderNorm","Continent"])[["JobSat","CareerSat"]].mean())\
 .to_csv(OUT/"job_career_satisfaction.csv")

print("\n📊 ALL REPORTS GENERATED\n")
