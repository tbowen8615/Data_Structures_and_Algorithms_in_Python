# Implement the __sub__ method for the Vector class of Section 2.3.3, so  that the expression u−v returns a new vector
# instance representing the difference between two vectors.

# Implement the neg method for the Vector class of Section 2.3.3, so  that the expression −v returns a new vector
# instance whose coordinates are all the negated values of the respective coordinates of v.

# Implement the __mul__ method for the Vector class of Section 2.3.3, so  that the expression v * 3 returns a new vector
# with coordinates that are 3 times the respective coordinates of v.

# Exercise R-2.12 asks for an implementation of __mul__, for the Vector  class of Section 2.3.3, to provide support for
# the syntax v * 3. Implement the __rmul__ method, to provide additional support for syntax 3 v.

# Implement the __mul__ method for the Vector class of Section 2.3.3, so  that the expression u * v returns a scalar
# that represents the dot product of the vectors.

# The Vector class of Section 2.3.3 provides a constructor that takes an integer d, and produces a d-dimensional vector
# with all coordinates equal to  0. Another convenient form for creating a new vector would be to send the  constructor
# a parameter that is some iterable type representing a sequence  of numbers, and to create a vector with dimension
# equal to the length of  that sequence and coordinates equal to the sequence values. For example,  Vector([4, 7, 5])
# would produce a three-dimensional vector with coordinates <4, 7, 5>. Modify the constructor so that either of these
# forms is  acceptable; that is, if a single integer is sent, it produces a vector of that  dimension with all zeros,
# but if a sequence of numbers is provided, it produces a vector with coordinates based on that sequence.

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d,):
        """Create d-dimensional vector of zeros."""
        if isinstance(d, int):
            self._coords = [0] * d
        elif isinstance(d, (list, tuple)):
            self._coords = list(d)
        else:
            raise TypeError("Invalid parameter type for Vector")

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __mul__(self, other):
        """Return scalar multiplication of two vectors."""
        if isinstance(other, (int, float)): # Scalar multiplication
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
            return result
        elif isinstance(other, Vector): # Dot product
            if len(self) != len(other):
                raise ValueError("dimensions must agree")
            result = 0
            for j in range(len(self)):
                result += self[j] * other[j]
            return result
        else:
            raise TypeError("Operand must be a scalar (int/float) or a Vector")


    def __rmul__(self, scalar):
        """Return scalar multiplication of two vectors when scalar is on the left and vector on the right"""
        if not isinstance(scalar, (int, float)):
            raise TypeError("scalar must be an int or float")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = scalar * self[j]
        return result

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):            # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))            # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __radd__(self, other):
        """Return sum when list or tuple is on the left and vector is on the right."""
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other[j] + self[j] # Add in reverse order
        return result

    def __sub__(self, other):
        """Return difference of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __neg__(self):
        """Return the negation of the vector"""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = -1 * self[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other              # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'   # adapt list representation


# In Section 2.3.3, we note that our Vector class supports a syntax such as  v = u + [5, 3, 10,−2, 1], in which the sum
# of a vector and list returns  a new vector. However, the syntax v = [5, 3, 10,−2, 1] + u is illegal.  Explain how the
# Vector class definition can be revised so that this syntax generates a new vector.

"""
Modify the Vector class by implementing the __radd__ method. The __radd__ method is called when the left operand does
not support the addition operation with the right operand, and Python falls back to the right operand's __radd__ method
"""