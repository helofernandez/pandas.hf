import pandas as pd

df = pd.read_csv("Carros.csv")

# Contar carros por empresa
total_carros = df["company"].value_counts()

print(total_carros)