"""
Proyecto del Día 6 - Análisis de Medallas Olímpicas,
Objetivo,
Realizar un análisis exploratorio de datos ´(EDA) sobre un conjunto de datos de medallas olímpicas utilizando Pandas. 
Este proyecto te permitirá aplicar los conceptos aprendidos sobre **Series**, **DataFrames**, **limpieza de datos**, **operaciones básicas**, **filtrado** y **agregación** en Pandas.,
Consigna,
Vas a trabajar con el conjunto de datos *medallas.csv*, que descargarás de la lección **Proyecto del Día 6**, y que incluye información sobre las medallas de oro, plata, bronce 
y el total obtenido por cada país en los Juegos Olímpicos.,
Vas a realizar una serie de tareas básicas, que te permitirán responder a las preguntas del **cuestionario** que encontrarás al final del día. Las tareas que realizarás son:,
    1. **Cargar los Datos**: Importar los datos desde el archivo CSV a un DataFrame de Pandas.,
    2. **Exploración Inicial**: Utilizar métodos básicos para explorar el tamaño, las columnas y los tipos de datos del DataFrame.,
    3. **Limpieza de Datos**: Identificar y manejar valores faltantes o incorrectos, especialmente en las columnas de medallas donde los valores faltantes indican cero medallas.,
    4. **Análisis de Medallas de Oro por País**: Realiza las operaciones que sean necesarias para identificar cuáles fueron los 3 países con más medallas de Oro en total 
    (vas a necesitar investigar los métodos de dataframes para encontrar cuál te permite ordenar los valores de mayor a menor o viceversa).,
    5. **Análisis de Medallas Totales por País**: Obtener un dataframe que contenga sólo los países que ganaron más de 10 medallas en total.,
Una vez que hayas realizado estos pasos, realiza el **cuestionario del día**, que contiene preguntas que solo podrás responder tras haber explorado los datos siguiendo los pasos anteriores.,
¡Mucha suerte!
"""
import pandas as pd

df = pd.read_csv("../data/medallas.csv")
print(df)

print(" = = = = = = = = = = = = = = = = = = = = ")
print(df.info())
print(df.shape)
print(df.head())
print(df.index)
print(df.columns)
print(df.describe())
print(" = = = = = = = = = = = = = = = = = = = = ")
df['Oro'] = df['Oro'].fillna(0)
df['Plata'] = df['Plata'].fillna(0)
df['Bronce'] = df['Bronce'].fillna(0)

df['Oro'] = df['Oro'].astype(int)
df['Plata'] = df['Plata'].astype(int)
df['Bronce'] = df['Bronce'].astype(int)

print(" = = = = = = = = = = = = = = = = = = = = ")
print(df)
print(df.nlargest(3, "Oro")) # Search top 3 winners gold
print(df.sort_values(by='Oro', ascending=False).head((3))) # Search top 3 winners gold 

print(df[df['Total'] > 10])

