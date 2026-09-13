import pandas as pd

INPUT_FILE = "ApexPlanet_DataAnalytics_Dataset.xlsx"
OUTPUT_FILE = "ApexPlanet_Task1_Cleaned_Dataset.xlsx"

df = pd.read_excel(INPUT_FILE)

# Standardize column names
df.columns = [c.strip() for c in df.columns]

# Standardize date
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df["Order_Date"] = df["Order_Date"].dt.strftime("%Y-%m-%d")

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].median()).round().astype(int)
df["City"] = df["City"].fillna("Unknown").astype(str).str.strip()

# Standardize text
for col in ["Order_ID", "Customer_ID", "Customer_Name", "Gender", "Product", "Category"]:
    df[col] = df[col].astype(str).str.strip()

# Preserve original IDs and make duplicate transaction IDs unique
df["Original_Order_ID"] = df["Order_ID"]
seen = {}
new_ids = []
for oid in df["Order_ID"]:
    seen[oid] = seen.get(oid, 0) + 1
    new_ids.append(oid if seen[oid] == 1 else f"{oid}_DUP{seen[oid]-1}")
df["Order_ID"] = new_ids

# Ensure numeric columns are numeric
for col in ["Quantity", "Unit_Price", "Total_Sales"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Recalculate sales only if the source value is missing
df["Total_Sales"] = df["Total_Sales"].fillna(df["Quantity"] * df["Unit_Price"])

df.to_excel(OUTPUT_FILE, index=False)
print(f"Saved cleaned dataset to {OUTPUT_FILE}")
