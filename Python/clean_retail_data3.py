import pandas as pd

df = pd.read_excel("Online Retail_1.xlsx")

print("Missing descriptions before cleaning:",
      df["Description"].isna().sum())

description_map = (
    df.dropna(subset=["Description"])
      .groupby("StockCode")["Description"]
      .agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
)

df["Description"] = df["Description"].fillna(
    df["StockCode"].map(description_map)
)

print("Missing descriptions after cleaning:",
      df["Description"].isna().sum())

df.to_excel("Online Retail_Cleaned_1.xlsx", index=False)

print("Cleaning completed!")
print("Saved as: Online Retail_Cleaned_1.xlsx")
