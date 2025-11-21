import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
st.write("📂 Working Directory:", os.getcwd())


df = pd.read_csv("../data/processed/cleaned_survey.csv")



st.set_page_config(page_title="StackOverflow ETL Insights", layout="wide")

st.title("📊 StackOverflow Developer Survey 2019 — FULL ETL ANALYTICS REPORT")
st.caption("🚀 All 6 Assignment Questions Below — With Answers + Charts + Insights")


# ===============================================================
# QUESTION 1️ — Avg Age when first code
# ===============================================================

st.markdown("## 1️ What is the **average age** developers wrote their first line of code?")

if "Age1stCode" not in df.columns:
    st.error(f"Column 'Age1stCode' not found. Available columns: {df.columns.tolist()}")
else:
    avg_age = round(df["Age1stCode"].mean(), 2)

    col1, col2 = st.columns(2)
    col1.metric("📌 Avg Age (Years)", avg_age)

    fig_age = px.histogram(df, x="Age1stCode", nbins=30,
                           title="📊 Distribution of First Code Age")
    col2.plotly_chart(fig_age, use_container_width=True)

    st.info(f"💡 **INSIGHT:** Most developers started coding before {avg_age} years old!")

# ===============================================================
# QUESTION 2️ — Python % by Country
# ===============================================================

st.markdown("## 2️ % of developers knowing **Python in each Country**")

python_pct = (df.groupby("Country")["KnowsPython"].mean()*100).sort_values()

fig_py = px.bar(
    python_pct.tail(15),
    title="🐍 Top 15 Countries with Most Python Developers",
    text_auto=".2f"
)

st.plotly_chart(fig_py, use_container_width=True)

top_country = python_pct.idxmax()
top_val = round(python_pct.max(),2)
st.success(f"🔥 **{top_country} has the highest Python share: {top_val}%**")

# ===============================================================
# QUESTION 3️ — Avg Salary by Continent
# ===============================================================

st.markdown("## 3️ Average developer salary by **Continent**")

salary = df.groupby("Continent")["ConvertedComp"].mean().dropna()

fig_sal = px.bar(
    salary,
    title="💰 Average Salary per Continent (USD)",
    color=salary.values,
    text_auto=".2f"
)
st.plotly_chart(fig_sal, use_container_width=True)

st.warning("💡 North America & Europe show highest salary levels.")

# ===============================================================
# QUESTION 4️ — Most Desired Language 2020
# ===============================================================

st.markdown("## 4️ Most desired programming languages for **2020**")

desired = (
    df["LanguageDesireNextYear"].dropna()
      .str.split(";")
      .explode()
      .value_counts()
      .head(12)
)

fig_lang = px.pie(
    names=desired.index,
    values=desired.values,
    title="🔥 Most Wanted Languages (2020)",
    hole=0.45
)
st.plotly_chart(fig_lang, use_container_width=True)

st.success(f"🏆 **Top Desired Language:** {desired.index[0]}")

# ===============================================================
# QUESTION 5️ — Hobby Coding % by Gender + Continent
# ===============================================================

st.markdown("## 5️ % of people who code as a hobby — by Gender & Continent")

# Compute % safely
hobby_raw = (
    df.groupby(["GenderNorm", "Continent"])["Hobbyist"]
      .value_counts(normalize=True) * 100
)

# FORCE into Series ALWAYS
hobby_series = pd.Series(hobby_raw, name="Percent (%)")

# Convert to DataFrame
hobby_df = hobby_series.reset_index()

# Filter only YES values
hobby_yes = hobby_df[hobby_df["Hobbyist"] == "Yes"]

fig_hobby = px.bar(
    hobby_yes,
    x="Continent",
    y="Percent (%)",
    color="GenderNorm",
    barmode="group",
    title="🎮 Hobby Coders (%) by Gender & Continent",
    text_auto=".2f"
)

st.plotly_chart(fig_hobby, use_container_width=True)

st.info("💡 Shows how many developers continue coding outside work based on gender and geography.")

# ===============================================================
# QUESTION 6️ — Job + Career Satisfaction
# ===============================================================

st.markdown("## 6️ Job & Career Satisfaction by **Gender & Continent**")

sat = df.groupby(["GenderNorm","Continent"])[["JobSat","CareerSat"]].mean()

fig_heat = px.imshow(
    sat["JobSat"].unstack(),
    color_continuous_scale="Plasma",
    title="🔥 Job Satisfaction Heatmap (1–5 Score)"
)

st.plotly_chart(fig_heat, use_container_width=True)

st.write("✔ Higher score = More satisfied developers")

# ===============================================================
# END OF REPORT
# ===============================================================

st.success("🎉 ALL 6 ASSIGNMENT QUESTIONS ANSWERED ✔")
