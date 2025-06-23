import pandas as pd
import os

parent = "exercises\\14library"
sharedata_path = os.path.join(parent, "2025_06_18_sharedata.csv")
df = pd.read_csv(sharedata_path)
# print(df.head())
# # print(df[["LTP"]][(int(df[["LTP"]]) >= 300 and int(df[["LTP"]]) <= 500)]) # dataframes cannot be type casted to int as like this
df["LTP"] = pd.to_numeric(df["LTP"].astype(str).str.replace(",", ""), errors="coerce")

# print(type(df["LTP"]))
filtered_df = df[(df["LTP"] >= 300) & (df["LTP"] <= 500)]
filtered_path = os.path.join(parent, "filtered_stock.csv")
filtered_df.to_csv(filtered_path, index=False)
