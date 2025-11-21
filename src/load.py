def load_processed(df, path="data/processed/cleaned_survey.csv"):
    print("💾 Saving processed data...")
    df.to_csv(path, index=False)
    print("✔ Saved:", path)
