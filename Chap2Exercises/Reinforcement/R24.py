# Write a Python class, Flower, that has three instance variables of type str, int, and float, that respectively
# represent the name of the flower, its number of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should  include methods for setting the value
# of each type, and retrieving the value  of each type.

class Flower:
    def __init__(self, name: str, petal_count: int, price: float):
        """ Create a new Flower instance

        name must be a string
        petal_count must be an integer
        price must be a float

        """
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
        """Set the name of the flower."""
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        self._name = name

    def set_petal_count(self, petal_count: int):
        """Set the petal count of the flower."""
        if not isinstance(petal_count, int):
            raise TypeError("Petal count must be an integer.")
        self._petal_count = petal_count

    def set_price(self, price: float):
        """Set the price of the flower."""
        if not isinstance(price, float):
            raise TypeError("Price must be a float.")
        self._price = price

    def get_name(self):
        """Get the name of the flower."""
        return self._name

    def get_petal_count(self):
        """Get the petal count of the flower."""
        return self._petal_count

    def get_price(self):
        """Get the price of the flower."""
        return self._price
