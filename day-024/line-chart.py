import matplotlib.pyplot as plt

stock_price = [190.64, 190.09, 192.25, 191.79, 194.45, 196.45, 196.45, 196.42,
200.32, 200.32, 200.85, 199.2, 199.2, 199.2, 199.46, 201.46, 197.54, 201.12, 203.12,
203.12, 203.12, 202.83, 202.83, 203.36, 206.83, 204.9, 204.9, 204.9, 204.4, 204.06]

days = list(range(1, 31))

plt.plot(days, stock_price, marker='.', color='red')
plt.title('Opening Stock Prices')
plt.xlabel('Days')
plt.ylabel('$ USD')
plt.show()

