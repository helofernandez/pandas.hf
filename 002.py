import pandas as pd

# Carrega o arquivo CSV
df = pd.read_csv("Carros.csv")

# Garante que a coluna 'price' seja numérica (descarta/trata valores nulos se houver)
df['price'] = pd.to_numeric(df['price'], errors='coerce')

# Encontra a linha com o maior preço
carro_mais_caro = df.loc[df['price'].idxmax()]

print("Montadora com o carro mais caro:")
print(f"Empresa: {carro_mais_caro['company']}")
print(f"Preço: {carro_mais_caro['price']}")