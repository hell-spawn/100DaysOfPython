import pandas as pd


"""
El objetivo es fusionar libros con autores para obtener un DataFrame que contenga toda la información disponible, asociando cada 
libro con su autor correspondiente. Debes nombrar el DataFrame fusionado como: libros_autores
Utiliza el método de fusión adecuado para asegurar que no se pierda ningún libro o autor, 
incluso si no hay una correspondencia directa entre ellos. El resultado debe tener NaN donde no haya información disponible
"""
libros = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'titulo': ['El Quijote', 'La Odisea', 'Cien Años de Soledad', 'El Principito']
})

autores = pd.DataFrame({
    'ID': [1, 2, 3, 5],
    'nombre': ['Miguel de Cervantes', 'Homero', 'Gabriel García Márquez', 'J.K. Rowling']
})

libros_autores = pd.merge(libros, autores, on='ID', how='outer')

print(libros_autores)


"""
Tu tarea es fusionar cursos con inscripciones (en un DataFrame llamado: cursos_inscripciones) de tal manera que el 
resultado final incluya todos los registros de inscripciones, completándolos con la información disponible en cursos.

Utiliza el método de fusión adecuado para garantizar que no se pierda ninguna inscripción, incluso si el curso correspondiente 
no está listado en el DataFrame cursos. Es importante que el DataFrame resultante cursos_inscripciones muestre claramente 
qué inscripciones no tienen un curso correspondiente, rellenando esos espacios con NaN
"""

cursos = pd.DataFrame({
    'curso_id': [101, 102, 103],
    'nombre_curso': ['Introducción a Python', 'Data Science con Python', 'Machine Learning Avanzado']
})

inscripciones = pd.DataFrame({
    'curso_id': [102, 102, 101, 104],
    'fecha_inscripcion': ['2023-01-15', '2023-02-01', '2023-01-20', '2023-03-05']
})

cursos_inscripciones = pd.merge(inscripciones, cursos, on="curso_id", how="left")
print(cursos_inscripciones)


"""
Tu tarea consiste en fusionar productos con reviews para obtener un DataFrame que combine la información de ambos 
(al cual debes nombrar: productos_reviews), manteniendo los índices originales de cada uno.

Utiliza los parámetros adecuados de la función merge() para realizar esta combinación. El DataFrame resultante productos_reviews 
debe contener las columnas de ambos DataFrames originales, permitiendo así un análisis detallado de cada producto junto con sus reseñas.
"""

productos = pd.DataFrame({
    'ID': [10, 11, 12],
    'Nombre': ['Teclado', 'Mouse', 'Monitor'],
    'Marca': ['Logitech', 'Razer', 'Dell']
})

reviews = pd.DataFrame({
    'ID': [10, 11, 12],
    'Calificación': [5, 4, 4],
    'Comentario': ['Excelente producto', 'Buen producto', 'Satisfecho']
})


productos_reviews = pd.merge(productos, reviews,  right_index=True, left_index=True)
print(productos_reviews)
