import pandas as pd

path = "../data/Top-Películas.csv"

df = pd.read_csv(path)
df["año"] = df["año"].astype(dtype="Int32")

print(df.info())

#print(df.sort_values(by="recaudación(M)", ascending=False))

#print(df.sort_values(by=["rating", "recaudación(M)"], ascending=False).head(10))

print(df.groupby("año")["recaudación(M)"].sum().sort_values(ascending=False))



