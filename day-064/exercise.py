# Cargar Data frame
# Normalizar los datos
# Seleccionar la ciudad de la lista de ciudades y un mes y año
# Mostrar al usuario un grafico que muestre las temperaturas máximas y mínimas de la ciudad seleccionada en el mes y año seleccionado


import pandas as pd
import matplotlib.pyplot as plt


def get_data() -> pd.DataFrame:
    data = pd.read_csv('../data/Datos_Meteorológicos_Arg_2023.csv')
    data['Fecha'] = pd.to_datetime(data['Fecha'], format='%d/%m/%Y')
    print(data.info())
    return data

def build_plot(data: pd.DataFrame, city_index: int, month: int) -> None:
    data_filter = data[(data['Fecha'].dt.month == month) & (data['Ciudad'] == cities[city_index])]
    #print(data_filter.head(30))
    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data_filter['Fecha'], data_filter['Temperatura Maxima'], color='red', label='Tmax')
    ax.plot(data_filter['Fecha'], data_filter['Temperatura Minima'], color='blue', label='Tmin')
    ax.set_xlabel('Date')
    ax.set_ylabel('Temperature')
    ax.set_title('Max and Min Temperatures in ' + cities[city_index])
    ax.grid(True)
    ax.tick_params(axis='x', pad=15)
    plt.legend()
    plt.xticks(data_filter['Fecha'],rotation=90)  # Cambiar el ángulo a 90 grados
    plt.tight_layout()
    plt.show()
    pass


while True:
    data: pd.DataFrame = get_data()

    cities = data['Ciudad'].unique()
    for i, city in enumerate(cities):
        print(f'{i + 1}. {city}')
    
    city_index = int(input('Select a city: ')) - 1
    month = int(input('Select a month(1-12): ')) 

    build_plot(data, city_index, month) 

    answer = input('Do you want to continue? (y/n): ')
    if answer.lower() != 'y':
        break

print('Goodbye!')
