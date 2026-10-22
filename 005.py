import pandas as pd

df = pd.read_csv("Carros.csv")

# Encontrar o maior preço de cada empresa
mais_caros = df.loc[
    df.groupby("company")["price"].idxmax()
]

print(mais_caros)