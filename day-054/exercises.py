"""
Region, Temp(f), Rainfall(mm), humidity(%)
kanto,  73, 67, 43
johto,  91, 88, 64
hoenn,  87, 134, 58
sinnoh, 102, 43, 37
unova,  69, 96, 70

"""
import numpy as np

w1, w2, w3 = 0.3, 0.2, 0.5

kanto_array = [73, 67, 43]
johto_array = [91, 88, 64]
hoenn_array = [87, 134, 58]
sinnoh_array = [102, 43, 37]
unova_array = [69, 96, 70]

weights_array = [w1, w2, w3]

# Custom dot product region vs weights


def crop_yield(region, weights):
    result = 0
    for x, y in zip(region, weights):
        result += x * y

    return result


print(crop_yield(kanto_array, weights_array))

weights = np.array(weights_array)
kanto = np.array(kanto_array)

type(kanto)

print(kanto[0])  # Support index notation

print("Dot product")
print(np.dot(kanto, weights))

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 * arr2)

print(arr1.sum())

climate_data = np.array([
                         [73, 67, 43],
                         [91, 88, 64],
                         [87, 134, 58],
                         [102, 43, 37],
                         [69, 96, 70]
                    ])

print("Dot Product")
print(climate_data @  weights)

# 1D array (vector)
print(weights.shape)
# 2D array (matrix)
print(climate_data.shape)
# 3D array
arr3 = np.array(
        [[[11, 12, 13], 
          [13, 14, 15]], 
         [[15, 16, 17], 
          [17, 18, 19.5]]])

print(arr3.shape)

climate_data = np.genfromtxt('../data/climate.txt', skip_header=1, delimiter=',')

print(climate_data.shape)

dot_climate = climate_data @ weights

for value in dot_climate:
    print(value)




