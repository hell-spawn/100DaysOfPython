import numpy as np
import matplotlib.pyplot as plt



A_M = np.log(2) / 2
print(np.log(2))
print(A_M)

B_M = np.log(2250) - A_M * 1971
print(B_M)

Moores_law = lambda year: np.exp(B_M) * np.exp(A_M * year)


ML_1971 = Moores_law(1971)
print(ML_1971)
ML_1973 = Moores_law(1973)
print(ML_1973)
print("In 1973, G. Moore expects {:.0f} transistors on Intels chips".format(ML_1973))
print("This is x{:.2f} more transistors than 1971".format(ML_1973 / ML_1971))


data = np.loadtxt("../data/transistor-counts.csv", delimiter=",", usecols=[1, 2], skiprows=1)

year = data[:, 1]  # grab the second column and assign
transistor_count = data[:, 0]  # grab the first column and assign

print("year:\t\t", year[:10])
print("trans. cnt:\t", transistor_count[:10])


yi = np.log(transistor_count)

model = np.polynomial.Polynomial.fit(year, yi, deg=1)

model = model.convert()
model

B, A = model

print(f"Rate of semiconductors added on a chip every 2 years: {np.exp(2 * A):.2f}")

transistor_count_predicted = np.exp(B) * np.exp(A * year)
transistor_Moores_law = Moores_law(year)
plt.style.use("fivethirtyeight")
plt.semilogy(year, transistor_count, "s", label="MOS transistor count")
plt.semilogy(year, transistor_count_predicted, label="linear regression")


plt.plot(year, transistor_Moores_law, label="Moore's Law")
plt.title( "MOS transistor count per microprocessor\n" + "every two years \n" + "Transistor count was x{:.2f} higher".format(np.exp(A * 2)))
plt.xlabel("year introduced")
plt.legend(loc="center left", bbox_to_anchor=(1, 0.5))
plt.ylabel("# of transistors\nper microprocessor")

plt.show()

