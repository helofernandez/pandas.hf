import pandas as pd

# Criar a tabela dos carros alemães
german_cars = pd.DataFrame({
    "company": ["ford", "mercedes", "BMW", "AUDI"],
    "price": [23845, 135925, 71795, 71400]
})

# Criar a tabela dos carros japoneses
japanese_cars = pd.DataFrame({
    "company": ["toyota", "Honda", "nissan", "mitsubishi"],
    "price": [29995, 23600, 61500, 58900]
})

# Combinar as duas tabelas
german_cars["origem"] = "Alemães"
japanese_cars["origem"] = "Japoneses"

carros = pd.concat(
    [german_cars, japanese_cars],
    ignore_index=True
)

print(carros)