

class Temperature():

    def __init__(self, celsius: int) -> None:
        self.celsius = celsius

   # def fahrenheit(self) -> float:
   #    return self.celsius * 9 / 5 + 32

    """Decorator property se puede llamar un metodo como si fuera una propiedad """
    @property
    def fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    #Exercise 80: Writing a Setter Method

    @fahrenheit.setter
    def fahrenheit(self, value: int)-> None:
        if value < -460:
            raise ValueError('Temperatures less than -460F are not possible')
        self.celsius = ( value - 32 ) * 5 / 9 


freezing = Temperature(0)
print(freezing.fahrenheit)
freezing.celsius = -10
print(freezing.fahrenheit)
freezing.fahrenheit = 32
print(freezing.celsius)
freezing.fahrenheit = -500
