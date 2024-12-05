import numpy as np

'''
Crea un programa que defina dos arrays usando NumPy: el primer array A debe ser un array unidimensional de 5 
elementos, iniciando en 1 y con pasos de 2 (i.e., [1, 3, 5, 7, 9]), y el segundo array B 
debe ser un array bidimensional de forma (5,1), con valores que comiencen en 10 y aumenten de 10 en 10 
(i.e., [[10], [20], [30], [40], [50]]).
Utiliza el concepto de broadcasting para sumar estos dos arrays y almacena su resultado en una variable llamada resultado
'''

A = np.array([1, 3, 5, 7, 9])
B = np.array([[10], [20], [30], [40], [50]])

resultado = A + B
print(resultado)

'''
Crea un programa que defina dos arrays usando NumPy: el primer array A debe ser un array unidimensional de 10 
elementos, iniciando en 1 hasta el 10, y el segundo array B debe ser un array bidimensional de forma (5,1), 
con valores que comiencen en 10 y aumenten de 10 en 10 (i.e., [[10], [20], [30], [40], [50]]).

Utiliza el concepto de broadcasting para multiplicar estos dos arrays almacena el resultado en una variable llamada resultado
'''


A = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
B = np.array([[10], [20], [30], [40], [50]])

resultado = A * B
print(resultado)

'''
Crea un programa que defina un array usando NumPy: A debe ser un array unidimensional de solamente 3 elementos, iniciando 
en 1 y terminando en 3 (inclusive)

Utiliza la función matemática adecuada para almacenar en una variable llamada resultado el exponente de cada numero contenido en A 
'''

A = np.array([1, 2, 3])
resultado = np.exp(A)
print(resultado)

'''
Dado el siguiente array de numpay
array = np.array([3, np.nan, 7, np.nan, 0, 4.5, np.nan])
Utiliza la función adecuada para comprobar la presencia de NaN, y almacena el resultado en una variable llamada: nan_presencia
'''

array = np.array([3, np.nan, 7, np.nan, 0, 4.5, np.nan])
nan_presencia = np.isnan(array)
print(nan_presencia)


'''
Tratamiento de Datos Faltantes con NumPy 2
Dado el siguiente array de numpay
array = np.array([3, np.nan, 7, np.nan, 0, 4.5, np.nan])
Crea una variable llamada promedio_sin_nans que almacene el promedio excluyendo cualquier valor np.nan. Debes utilizar una función de 
NumPy que ignore los np.nan automáticamente para este cálculo
'''

array = np.array([3, np.nan, 7, np.nan, 0, 4.5, np.nan])
promedio_sin_nans = np.nanmean(array)
print(promedio_sin_nans)

'''
Tratamiento de Datos Faltantes con NumPy 3
Dado el siguiente array de numpay
array = np.array([3, np.nan, 7, np.nan, 0, 4.5, np.nan])
Crea una variable nombrada sustituir_nans donde almacenes los np.nan encontrados en el array sustituidos por cero (0). Emplea la función correcta de NumPy para esta finalidad.
'''

array = np.array([3, np.nan, 7, np.nan, 0, 4.5, np.nan])
sustituir_nans = np.where(np.isnan(array), 0, array)
print(sustituir_nans)

