"""
Crear un programa en Python que analice un conjunto de **datos de ventas de una tienda**. El programa debe realizar varias operaciones de Data Science para proporcionar 
información valiosa sobre las ventas de la tienda.",
1. **Lectura de Datos**: Crea un DataFrame que contenga los datos provistos en el archivo **Datos_Ventas_Tienda.csv** provisto en esta lección. 
El archivo incluirá información como *fecha de venta*, *categoría de producto*, *cantidad vendida* y *precio*.\n",
2. **Fusión de Datos**: Crea un segundo DataFrame que contenga los datos del archivo **Datos_Ventas_Tienda2.csv** (también provisto en esta lección), 
y concaténalos para tener un solo dataFrame con toda la información.",
3. **Tratamiento de Datos**: Utiliza Pandas para manipular estos datos. Deberás realizar tareas como limpieza de datos, filtrado y  transformaciones básicas.",
4. **Análisis de Ventas**: Realiza análisis para responder preguntas como:",
- ¿Cuál es el producto más vendido?",
- ¿Cuál es el mes con más ventas?",
5. **Datos Agrupados**: Agrupa los datos por categoría de producto y analiza las ventas por categoría.\n",
6. **Guardar Resultados**: Al final, guarda el DataFrame completo (incluyendo la columna de meses) en un archivo .csv en tu ordenador."
"""

from re import I
import pandas as pd

ventas1 = pd.read_csv("../data/Datos_Ventas_Tienda.csv")
ventas2 = pd.read_csv("../data/Datos_Ventas_Tienda2.csv")

total_ventas = pd.concat([ventas1, ventas2])
# Conver a formato fecha
total_ventas["Fecha"] = pd.to_datetime(total_ventas["Fecha"])

total_ventas.info()
print(total_ventas.head())

# ¿Cuál es el producto más vendido?
producto_mas_vendido =  total_ventas.groupby("Producto")["Cantidad"].sum().sort_values(ascending=False).index[0]
print(producto_mas_vendido)

# ¿Cuál es el mes con más ventas?
total_ventas["Mes"] = total_ventas["Fecha"].dt.month
mes_mas_vendido = total_ventas.groupby("Mes")["Mes"].count().sort_values(ascending=False).index[0]
print(mes_mas_vendido)


# Al final, guarda el DataFrame completo (incluyendo la columna de meses) en un archivo .csv en tu ordenador.
ventas_agrupadas = total_ventas.groupby("Producto")["Total Venta"].sum()
print(ventas_agrupadas)

