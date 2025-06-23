import pandas as pd
import os
import matplotlib.pyplot as plt

parent = "exercises\\14library"
filterd_path = os.path.join(parent, "filtered_stock.csv")
df = pd.read_csv(filterd_path)
df["Volume"] = pd.to_numeric(
    df["Volume"].astype(str).str.replace(",", ""), errors="coerce"
)
plt.scatter(x=df["LTP"], y=df["Volume"])
plt.xlabel("LTP")
plt.ylabel("Volume")
plt.title("LTP vs Volume")
plt.show()
