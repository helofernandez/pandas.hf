import pandas as pd

df = pd.read_csv("Carros.csv")

# Ordenar pelo preço
ordenados = df.sort_values(by="price")

print(ordenados)