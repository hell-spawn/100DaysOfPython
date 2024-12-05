import pandas as pd
import numpy as np


'''
Crea un DataFrame de Pandas llamado mi_dataframe con dos columnas: "Frutas" y "Cantidad".
La columna "Frutas" debe contener los valores "Manzana", "Banana" y "Cereza".
La columna "Cantidad" debe contener los números 5, 8 y 3 respectivamente.
Luego, convierte este DataFrame en un array de NumPy y guárdalo en una variable llamada array_frutas.
'''

mi_dataframe = pd.DataFrame( {
    "Frutas": ["Manzana", "Banana" , "Cereza"], 
    "Cantidad": [5, 8, 3] 
    })

print(mi_dataframe.head())

array_frutas = mi_dataframe.to_numpy()
print(array_frutas)


'''
Integración de NumPy con Pandas 2
Crea un DataFrame de Pandas llamado mi_dataframe con dos columnas: "Frutas" y "Cantidad". Identico al ejercicio anterior.
La columna "Frutas" debe contener los valores "Manzana", "Banana" y "Cereza".
La columna "Cantidad" debe contener los números 5, 8 y 3 respectivamente.
    Luego, filtra las filas donde la cantidad sea mayor a 4, almacena el resultado en una variable llamada: mi_dataframe_filtrado
    Convierte el resultado en un array de NumPy. Guarda el array resultante en una variable llamada array_filtrado
'''

mi_dataframe = pd.DataFrame({
    "Frutas": ["Manzana", "Banana" , "Cereza"],
    "Cantidad": [ 5, 8, 3 ]
    })

mi_dataframe_filtrado = mi_dataframe[mi_dataframe["Cantidad"] > 4] 
print(mi_dataframe_filtrado.head())

array_filtrado = mi_dataframe_filtrado.to_numpy()
print(array_filtrado)

'''
Integración de NumPy con Pandas 3
Crea un array de NumPy llamado mi_array con dos columnas y tres filas.
    La primera columna debe contener los números 10, 20 y 30.
    La segunda columna debe contener los números 40, 50 y 60.
Convierte este array en un DataFrame de Pandas llamado df_numeros y asigna los nombres "Decenas" y "Centenas" a las columnas. 
'''
mi_array = np.array([[10, 40], [20, 50], [30, 60]])

df_numeros = pd.DataFrame(mi_array, columns=["Decenas", "Centenas"])

print(df_numeros.head())
