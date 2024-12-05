import matplotlib.pyplot as plt


numeros = [10, 15, 7, 10, 22]

plt.figure(facecolor="green")
grafico_verde_numeros = plt.plot(numeros)
print(grafico_verde_numeros)
plt.show()


fig, axs = plt.subplots(nrows=2, ncols=2)
plt.show()
