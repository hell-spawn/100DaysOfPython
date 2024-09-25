import pandas as pd


"""
Crea una serie temporal que represente todos los días desde el inicio del año 2024 hasta el septimo dia del mismo mes y año.
Usa el método adecuado para generar esta serie y asígnala a una variable llamada primera_semana_2024
"""

primera_semana_2024 = pd.date_range("2024-01-01", periods=7)
print(primera_semana_2024)






df = pd.read_csv("../data/Mercado_de_Valores_España.csv")
print(df.info())
print(df.head(10))

primera_semana_2024 = pd.to_datetime(df["Fecha"],  format="%d/%m/%Y") 
print(primera_semana_2024.head(10))



