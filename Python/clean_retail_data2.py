import pandas as pd

df = pd.read_excel("Online Retail.xlsx")

print("Excel file loaded successfully!")
print("Number of rows:", len(df))

df.insert(
    df.columns.get_loc("Description") + 1,
    "Non_Capital_Description",
    ""
)

print("New column created successfully!")

for index, value in df["Description"].items():

    if pd.notna(value):

        text = str(value)

        if not text.isupper():

            df.loc[index, "Non_Capital_Description"] = text
            df.loc[index, "Description"] = ""

print("Cleaning completed!")

output_file = "Online Retail_Capital_Cleaned_NEW.xlsx"

df.to_excel(output_file, index=False)

print("New file saved as:", output_file)
print("Columns in new file:")
print(df.columns.tolist())
