import numpy as np
import pandas as pd


'''
Introducción a NumPy 1

Se te ha proporcionado un dataset que contiene información sobre varias ciudades, incluyendo su población y el número de 
visitantes anuales. Este dataset está representado en el siguiente DataFrame de Pandas:

'''
datos = {
    "Ciudad": ["Ciudad de México", "Buenos Aires", "Río de Janeiro", "Lima", "Bogotá", "Santiago de Chile", "São Paulo", "La Habana", "Cancún", "Cartagena"],
    "País": ["México", "Argentina", "Brasil", "Perú", "Colombia", "Chile", "Brasil", "Cuba", "México", "Colombia"],
    "Población": [9265833, 3059574, 6748314, 9756020, 7181663, 6199241, 12333146, 2164182, 888124, 1036671],
    "Visitantes": [21000000, 15000000, 13000000, 9000000, 8000000, 7500000, 20000000, 4000000, 5000000, 3000000]
}

df = pd.DataFrame(datos)
print(df.head(5))

prom = np.mean(df["Población"])
prom = np.round(prom)
print(prom)


'''
Encuentra el valor mínimo de visitantes usando el método adecuado de numpy, y almacena este valor en una variable llamada: 
min_visitantes
'''

min_visitantes = np.min(df["Visitantes"])
print(min_visitantes)

'''
Encuentra el valor máximo de visitantes usando el método adecuado de numpy, y almacena este valor en una variable llamada: 
max_visitantes
'''

max_visitantes = np.max(df["Visitantes"])
print(max_visitantes)

'''
Crea un array de numpy nombrado numeros que contenga los primeros 10 números enteros (del 1 al 10). Luego escribe un 
código para obtener el quinto elemento de este array. Almacenalo en una variable llamada quinto_elemento
'''

numeros = np.array([1,2,3,4,5,6,7,8,9,10])
quinto_elemento = numeros[4]
print(quinto_elemento)


'''
Crea un array bidimensional al que nombres: matriz con forma (3, 3) que representa una matriz de números del 1 al 9. 
Escribe un código para extraer la segunda fila completa de esta matriz. Almacenala en una variable nombrada segunda_fila
'''
matriz = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
segunda_fila = numeros[1]
print(segunda_fila)

'''
Crea un array bidimensional al que nombres: matriz con forma (3, 3) que representa una matriz de números del 1 al 9, 
identico al ejercicio anterior. Luego utiliza la indexacion booleana para guardar en una variable llamada 
pares_impares los numeros pares como true, y los impares como false.
'''

matriz = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

pares_impares = matriz % 2 == 0
print(pares_impares)

'''
Crea un array de NumPy llamado array_original  que contenga los números del 1 al 12 y luego cambia su forma 
para que se convierta en un array de 3 filas y 4 columnas. Almacenalo en una variable llamada array_reshape
'''

array_original = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
array_reshape = array_original.reshape(3, 4)
print(array_reshape)


'''
Crea un array bidimensional llamado: array_original de forma (2, 3) que contenga los primeros 6 números 
enteros positivos. Utiliza el método correcto para cambiar sus filas por columnas. Almacenalo en una 
variable llamada array_modificado
'''

array_original = np.array([[1,2,3],[4,5,6]])
array_modificado = np.transpose(array_original)
print(array_modificado)


'''
Crea un array de 2 dimensiones array_original de forma (2, 3) que contenga los primeros 6 números enteros positivos. Identico 
al del ejercicio anterior. Luego, crea una copia aplanada de este array y almacénalo en una variable llamada array_aplanado
'''
array_original = np.array([[1,2,3],[4,5,6]])
array_aplanado = np.ravel(array_original)
print(array_aplanado)
