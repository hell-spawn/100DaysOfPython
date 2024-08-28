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

