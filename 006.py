import pandas as pd

df = pd.read_csv("Carros.csv")

# Calcular a média por empresa
media = df.groupby("company")["average-mileage"].mean()

print(media)