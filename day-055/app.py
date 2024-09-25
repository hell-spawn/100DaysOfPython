import pandas as pd


"""
Combinar DataFrames en Pandas con join()

Utiliza el método join() para combinar df_a y df_b en un nuevo DataFrame llamado df_combinado, usando el argumento por defecto de how.
"""


# Creación del DataFrame df_a
df_a = pd.DataFrame({
    'id': [1, 2, 3],
    'Nombre': ['Ana', 'Beto', 'Carla']
})
df_a.set_index('id', inplace=True)

# Creación del DataFrame df_b
df_b = pd.DataFrame({
    'id': [1, 2, 3],
    'Edad': [25, 30, 35]
})
df_b.set_index('id', inplace=True)

df_combinado = df_a.join(df_b)

print(df_combinado)


"""
Dado el DataFrame productos_df con columnas ProductoID, Nombre y Precio, y el DataFrame categorias_df con columnas CategoriaID y NombreCategoria
"""

productos_df = pd.DataFrame({
    'ProductoID': [1, 2, 3, 4],
    'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
    'Precio': [100, 150, 200, 250]
}).set_index('ProductoID')

categorias_df = pd.DataFrame({
    'CategoriaID': [1, 2],
    'NombreCategoria': ['Categoría 1', 'Categoría 2']
}).set_index('CategoriaID')


df_combinado = productos_df.join(categorias_df)


"""
DataFrames en un DataFrame llamado df_combinado de tal manera que se conserven todos los registros del DataFrame de productos_df, 
incluso si no tienen una categoría correspondiente en categorias_df. Para esto, debes utilizar el parámetro how="right" en el método join().
"""

productos_df = pd.DataFrame({
    'ProductoID': [1, 2, 3, 4],
    'Nombre': ['Producto 1', 'Producto 2', 'Producto 3', 'Producto 4'],
    'Precio': [100, 150, 200, 250]
})

productos_df = productos_df.set_index('ProductoID')

categorias_df = pd.DataFrame({
    'CategoriaID': [1, 2, 3],
    'NombreCategoria': ['Categoría 1', 'Categoría 2', 'Categoría 3']
}).set_index('CategoriaID')

df_combinado = categorias_df.join(productos_df, how="right")
print(df_combinado)


""" 
Concatenar DataFrames en Pandas con concat 
Tu tarea es utilizar el método concat() para concatenar estos dos DataFrames verticalmente en un nuevo DataFrame llamado ventas_total. 
Asegúrate de ignorar los índices originales para que el índice del DataFrame resultante sea continuo.
"""

ventas_enero = pd.DataFrame({'Producto': ["Manzanas", "Bananas", "Naranjas"], 'Cantidad': [300, 200, 150]})
ventas_febrero = pd.DataFrame({'Producto': ["Manzanas", "Bananas", "Naranjas"], 'Cantidad': [350, 210, 170]})

ventas_total = pd.concat([ventas_enero, ventas_febrero], ignore_index=True)

print(ventas_total)

"""
Utiliza el método concat() para unir estos dos DataFrames horizontalmente, formando un nuevo DataFrame llamado info_cliente. 
Asegúrate de que los índices se mantengan para que cada fila corresponda correctamente entre los dos DataFrames.
"""
datos_cliente = pd.DataFrame({'Nombre': ["Ana", "Luis", "Marta"], 'Edad': [34, 45, 28]})
compras_cliente = pd.DataFrame({'Producto': ["Libro", "Lápiz", "Cuaderno"], 'Precio': [15.50, 0.50, 2.00]})

info_cliente = pd.concat([datos_cliente, compras_cliente], axis=1)
print(info_cliente)

"""
Tu tarea es concatenar estos DataFrames verticalmente en un nuevo DataFrame llamado ventas_tienda, utilizando el parámetro keys para 
marcar cada bloque de datos con las etiquetas "Tienda A" y "Tienda B", respectivamente. Asegúrate de que el DataFrame resultante tenga un índice jerárquico que refleje estas claves.
"""

tienda_a = pd.DataFrame({'Producto': ["Manzanas", "Bananas"], 'Cantidad': [500, 300]})
tienda_b = pd.DataFrame({'Producto': ["Naranjas", "Peras"], 'Cantidad': [400, 250]})

ventas_tienda = pd.concat([tienda_a,tienda_b], keys=["Tienda A", "Tienda B"] )

print(ventas_tienda)
