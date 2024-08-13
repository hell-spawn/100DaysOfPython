import pandas as pd
import math
from pandas.core import series

"""
Crear una DataFrame desde un CSV
"""
#df = pd.read_csv("../data/Precipitaciones.csv")
#
#print(df.shape)
#print(df.index)
#print(df.columns)
#print(df.describe())

#data_series = [4, 7, -5, 3]
#mi_serie = pd.Series(data_series);
#print(mi_serie)

"""
Crea una serie en Pandas a partir de la lista [10, 20, 30, 40] con índices personalizados ['a', 'b', 'c', 'd']. Llama a esta serie serie_con_indices.
Crea una variable llamada valor_c  donde almacenes el valor asociado al índice 'c'
Crea una función llamada imprimir_valor_c  que se capaz de mostrar el valor asociado al índice 'c'.

"""
#data =[10, 20, 30, 40]  
#index = ['a', 'b', 'c', 'd']
#serie_con_indices = pd.Series(data, index)
#
#
#def imprimir_valor_c():
#    print(serie_con_indices["c"])
#
#imprimir_valor_c()

"""
Ejercicio Series en Pandas 3
Utiliza el diccionario {'a': 30, 'b': 70, 'c': 160, 'd': 50} para crear una serie en Pandas, la cual llamarás serie_desde_diccionario.
Luego, accede a los valores asociados a los índices 'a' y 'd', sumándolos. 
Almacena esta suma en la variable suma_ad
Crea una función llamada: imprimir_suma_ad() que se encargue de imprimir el valor de suma_ad 

"""
#serie_desde_diccionario = pd.Series( {'a': 30, 'b': 70, 'c': 160, 'd': 50} )
#suma_ad = serie_desde_diccionario["a"] + serie_desde_diccionario['d']
#def imprimir_suma_ad():
#    print(suma_ad)
#imprimir_suma_ad()


"""
Ejercicio Operaciones Básicas con Series de Panda 1
Crea dos series de pandas utilizando listas de Python.
Puedes crear ambas series con los números enteros de tu elección solamente asegurate de que la serie 1 y la serie 2 las almacenes en variables nombradas: serie1 y serie2 respectivamente.
Luego, suma ambas series y asigna el resultado a una variable llamada serie_sumada. Imprime el resultado de serie_sumada.
"""

#serie1 = [2, 4, 6, 8]
#serie2 = [1, 1, 1, 1]
#serie_sumada = serie1 + serie2
#print(serie_sumada)

"""
Ejercicio Operaciones Básicas con Series de Panda 2
Dada una serie de pandas llamada serie_numerica que contienga los números de tu preferencia.
Realiza las siguientes operaciones matemáticas y guarda los resultados en variables separadas:
    Multiplica serie_numerica por 2 y guarda el resultado en serie_doble.
    Divide serie_numerica por 10 y guarda el resultado en serie_dividida.
Imprime los resultados de serie_doble y serie_dividida.

"""

#serie_numerica =pd.Series([2, 4, 6, 8])
#serie_doble = serie_numerica * 2
#serie_dividida = serie_numerica / 10
#
#print(serie_doble)
#print(serie_dividida)

"""
Ejercicio Operaciones Básicas con Series de Panda 3
Considera una serie de pandas llamada serie_grande que contiene los números del 1 al 10 o mayor al 10. Obten su item 9 y haya su raiz cuadrada.
Imprime el resultado.
Observación:
En estos ejercicios no tendrás el botón "Ejecutar código" por esta razón no podrás visualizar los datos generados. Si deseas visualizarlos podrás servirte de un cuaderno de Jupyter y luego probar el ejercicio con ayuda del botón: "Ejecutar pruebas"
"""

#serie_grande = pd.Series([x for x in range(11)])
#print(math.sqrt(serie_grande[9]))

"""
Dada una tabla (Diccionario) de ventas que contiene información sobre productos vendidos, incluyendo ID, Producto, Cantidad y Precio, 
"""

#data = {
#    'ID': [1, 2, 3, 4, 5],
#    'Producto': ['Producto A', 'Producto B', None, 'Producto D', 'Producto E'],
#    'Cantidad': [10, 20, 30, None, 50],
#    'Precio': [100, 200, 300, 400, None]
#}
#
#df = pd.DataFrame(data)
#print(df["Cantidad"].isnull())
#df_sin_duplicados = df.drop_duplicates(subset=["ID"])
#df["Precio"].fillna(df["Precio"].mean(), inplace=True)
#print(df)

"""
Crea una serie de Pandas llamada:  serie_numeros   que contenga los números del 1 al 20.
Luego, escribe un código que filtre y muestre solo aquellos números que sean mayores que 10.
Utiliza una variable llamada filtro para almacenar la serie  filtrada.
"""
#data = [x for x in range(1, 21)]
#serie_numeros = pd.Series(data)
#firtro = serie_numeros > 10
#print(serie_numeros[firtro])

"""
Dada una serie de Pandas que contiene los siguientes valores: [18, 22, 7, 9, 15, 8], filtra y muestra solo aquellos valores que sean pares.
    Primero, crea una serie de valores booleanos que represente la condición. Nombra a esta variable como: condicion_valores_pares
    Luego aplica esta serie para filtrar los valores originales.
"""

#valores = pd.Series([18, 22, 7, 9, 15, 8])
#
#condicion_valores_pares = valores % 2 == 0
#serie_valores_pares = valores[condicion_valores_pares]
#print(serie_valores_pares)
#
""" 
Filtrado de Series en Pandas 3
Crea una serie de Pandas llamada frutas y que contenga los siguientes elementos: ["manzana", "banana", "cereza", "durazno", "frambuesa"].
    Escribe un código que filtre y muestre solo aquellos elementos que contengan la letra "e" en su nombre. Almacena los elementos filtrados en una variable llamada frutas_con_e
    Utiliza una condición que aplique un método de strings para lograr este filtrado.
"""

#frutas = pd.Series(["manzana", "banana", "cereza", "durazno", "frambuesa"])
#filtro = frutas.str.contains("e")
#frutas_con_e = frutas[filtro]
#print(frutas_con_e)


"""
Agregación de Series en Pandas 1

Crea una serie de Pandas a partir de la siguiente lista de edades = [23, 30, 26, 27, 22, 24, 25, 28]. 
Luego, utiliza la función adecuada para calcular el promedio de estas edades. Almacena el promedio en una variable llamada: promedio_edades"" 

"""

#edades = pd.Series([23, 30, 26, 27, 22, 24, 25, 28])
#promedio_edades = edades.mean()


"""
Agregación de Series en Pandas 2

Dada lista con los siguientes valores de ventas diarias de una tienda en una semana:
ventas = [120, 150, 90, 200, 210, 130, 160], realiza las siguientes tareas:
    Crea una serie de Pandas con los días de la semana como índice  (asumiendo que el primer valor corresponde al Lunes).
    Calcula y muestra la suma total de las ventas de la semana. Almacena este valor en una variable llamada: suma_total_ventas
    Encuentra y muestra el día de mayores ventas. Almacena este valor en una variable llamada: dia_mayores_ventas
    Calcula y muestra el promedio de ventas de la semana. Almacena este valor en una variable llamada: promedio_ventas
"""


#ventas = pd.Series([120, 150, 90, 200, 210, 130, 160], ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"])
#
#suma_total_ventas = ventas.sum()
#dia_mayores_ventas =  ventas.max()
#promedio_ventas = ventas.mean()

#print(f"Suma {suma_total_ventas}")
#print(f"dia_mayores_ventas {dia_mayores_ventas}")
#print(f"promedio_ventas {promedio_ventas}")


"""
Agregación de Series en Pandas 3
Considera una serie de Pandas que representa las ventas de un mes, donde cada valor corresponde a las ventas de un día específico. No modifiques la serie de Pandas brindada en el ejercicio.
Realiza las siguientes operaciones y muestra los resultados empleando los métodos correspondientes:
    Calcula el total de ventas del mes. Almacena su valor en una variable llamada: total_ventas_mes
    Encuentra el día con las ventas más bajas. Almacena su valor en una variable llamada: dia_ventas_mas_bajas
    Determina el promedio mensual de ventas.  Almacena su valor en una variable llamada: promedio_ventas_mes
"""

# Serie de ventas del mes

ventas_mes = pd.Series([220, 235, 260, 213, 202, 298, 265, 198, 220, 230, 190, 215, 275, 222, 218, 245, 233, 210, 290, 210, 215, 220, 225, 230, 245, 250, 260, 270, 280, 295])
total_ventas_mes = ventas_mes.sum()
dia_ventas_mas_bajas = ventas_mes.min()
promedio_ventas_mes = ventas_mes.mean()

print(total_ventas_mes)
print(dia_ventas_mas_bajas)
print(promedio_ventas_mes)

