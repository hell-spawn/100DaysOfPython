import matplotlib.pyplot as plt
import numpy as np


#x = np.arange(1, 11, 1)
#y =  x ** 2
#
#fig, ax = plt.subplots()
#ax.stem(x, y)
#ax.set(xlabel='Número (x)', ylabel='Cuadrado del número (x^2)')
#ax.set_title('Relación entre Números y sus Cuadrados')
#plt.show()



#x = np.arange(1, 6, 1)
#y1 = [6, 1, 4, 4, 8]
#y2 = [4, 6, 3, 5, 8]
#y3 = [7, 9, 9, 2, 7]
#y = np.vstack([y1, y2, y3])
#
## plot
#fig, ax = plt.subplots()
#
#ax.stackplot(x, y, labels=['Serie y1', 'Serie y2', 'Serie y3'], colors=['red', 'blue', 'green'])
#ax.legend(loc='upper left')
#
#ax.set_title('Distribución acumulativa de valores por serie de tiempo')
#ax.set_xlabel('Tiempo')
#ax.set_ylabel('Valores Acumulados')
#
#plt.show()

# Generar los datos para cada muestra usando numpy.random.normal
np.random.seed(0) # Establecer la misma semilla para la generación de datos
data1 = np.random.normal(loc=0, scale=0.5, size=100)
data2 = np.random.normal(loc=2, scale=1, size=100)
data3 = np.random.normal(loc=-2, scale=1.5, size=100)

fig, ax = plt.subplots()
ax.violinplot([data1, data2, data3], showmeans=False, showmedians=True)

# Establecer las etiquetas del eje x
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(['Muestra 1', 'Muestra 2', 'Muestra 3'])

# Añadir título al gráfico
ax.set_title('Comparación de distribuciones en Violin Plot')

plt.show()
