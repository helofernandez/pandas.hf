import pandas as pd

df = pd.read_csv("Carros.csv")

# Filtrar os carros da Toyota
toyota = df[df["company"].str.lower() == "toyota"]

print(toyota)