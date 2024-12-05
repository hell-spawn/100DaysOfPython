import matplotlib.pyplot as plt


"""
Gráficos de Línea (Line Plots) en Matplotlib 1

Crea un gráfico de línea simple utilizando Matplotlib con los siguientes datos:

"""
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.grid(visible=True)
plt.plot(x,y)
plt.show()


"""
Gráficos de Línea (Line Plots) en Matplotlib 2

Utilizando el gráfico de línea simple con las rejillas (o grid) activas. Identico al ejercicio anterior con los siguientes datos:
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
Agrega los métodos necesarios para que el grafico se muestre con lineas rojas sólidas y con círculos en los puntos.
"""

plt.grid(visible=True)
plt.plot(x,y, "ro-")
plt.show()

"""
Gráficos de Línea (Line Plots) en Matplotlib 3

Utilizando el gráfico de línea simple con las rejillas (o grid) activas, con lineas rojas sólidas y con círculos en los puntos. Identico al ejercicio anterior con los siguientes datos:
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
Agrega los métodos necesarios para definir los límites del gráfico del eje x mínimo en 0 y máximo en 10, y 
el eje y mínimo en 0 y máximo en 12
"""


plt.grid(visible=True)
plt.axis((0,10,0,12))
plt.plot(x,y, "ro-")
plt.show()
