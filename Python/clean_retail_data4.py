import pandas as pd

df = pd.read_excel("Online Retail_1.xlsx")

print("Excel file loaded successfully!")
print("Rows:", len(df))

next_customer_id = 18288

blank_invoices = df.loc[
    df["CustomerID"].isna(),
    "InvoiceNo"
].unique()

print("Invoices with missing CustomerID:", len(blank_invoices))

invoice_customer_map = {}

for invoice in blank_invoices:
    invoice_customer_map[invoice] = next_customer_id
    next_customer_id += 1

df["CustomerID"] = df["CustomerID"].fillna(
    df["InvoiceNo"].map(invoice_customer_map)
)

df.to_excel(
    "Online_Retail_CustomerID_3.xlsx",
    index=False
)

print("Cleaning completed!")
print("Last CustomerID used:", next_customer_id - 1)
print("File saved as: Online_Retail_CustomerID_3.xlsx")
