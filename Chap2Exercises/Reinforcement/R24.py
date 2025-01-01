# Write a Python class, Flower, that has three instance variables of type str, int, and float, that respectively
# represent the name of the flower, its number of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should  include methods for setting the value
# of each type, and retrieving the value  of each type.

class Flower:
    def __init__(self, name: str, petal_count: int, price: float):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not isinstance(petal_count, int):
            raise TypeError("Petal count must be an integer.")
        if not isinstance(price, float):
            raise TypeError("Price must be a float.")

        self._name = name
        self._petal_count = petal_count
        self._price = price

    def set_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        self._name = name

    def set_petal_count(self, petal_count: int):
        if not isinstance(petal_count, int):
            raise TypeError("Petal count must be an integer.")
        self._petal_count = petal_count

    def set_price(self, price: float):
        if not isinstance(price, float):
            raise TypeError("Price must be a float.")
        self._price = price

    def get_name(self):
        return self._name

    def get_petal_count(self):
        return self._petal_count

    def get_price(self):
        return self._price
