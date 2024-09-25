import numpy as np
import matplotlib.pyplot as plt 
from numpy import linalg

img=plt.imread("../data/27295659492.jpg")

#img=plt.imread("../data/demo.jpg")
#print(type(img)) #numpy.ndarray
print(img[0,0,:])
print(img.shape)
#plt.imshow(img)
#plt.show()

img_array = img / 255

print(img_array.max(), img_array.min())
print(img_array.dtype)

red_array = img_array[:, :, 0]
green_array = img_array[:, :, 1]
blue_array = img_array[:, :, 2]

print(img[0,0,:])
print(img_array[0,0,:])
print(red_array[0, 0:3 ])

#plt.imshow(red_array, cmap="Reds")
#plt.show()
#
#plt.imshow(green_array, cmap="Greens")
#plt.show()
#
#plt.imshow(blue_array, cmap="Blues")
#plt.show()

img_gray = img_array @ [0.2126, 0.7152, 0.0722]
print(img_gray.shape)
print(img_gray[0,])

#plt.imshow(img_gray, cmap="gray")
#plt.show()

U, s, Vt = linalg.svd(img_gray)

print(U.shape, s.shape, Vt.shape)


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
