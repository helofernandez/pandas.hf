import pandas as pd

# Dados dos carros alemães
german_cars = pd.DataFrame({
    "company": ["ford", "mercedes", "BMW", "AUDI"],
    "price": [23845, 135925, 71795, 71400]
})

# Dados dos carros japoneses
japanese_cars = pd.DataFrame({
    "company": ["toyota", "Honda", "nissan", "mitsubishi"],
    "price": [29995, 23600, 61500, 58900]
})

# Juntar as duas tabelas
carros = pd.concat(
    [german_cars, japanese_cars],
    ignore_index=True
)

print(carros)