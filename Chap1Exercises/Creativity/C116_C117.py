# In our implementation of the scale function (page 25), the body of the loop executes the command data[j] *= factor.
# We have discussed that numeric  types are immutable, and that use of the *= operator in this context causes the
# creation of a new instance (not the mutation of an existing instance). How is it still possible, then, that our
# implementation of scale changes the  actual parameter sent by the caller?

def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor
    print(data)

# Caller
data = [1, 2, 3]
scale(data, 3)

"""
The implementation of the scale function modifies the actual parameter sent by the caller because lists in Python
are mutable, even though the individual elements in the list might be immutable.

A Python list is a mutable object. This means its contents can be changed directly, even if the elements themselves
are immutable.

When a list is passed as an argument to a function, what is passed is a reference to the original list, not a copy.
Therefore, any changes made to the list elements inside the function affect the original list in the caller's scope.

While numeric types like integers are immutable, the statement data[j] *= factor does not replace the data list itself.
Instead, the integer at data[j] is fetched, multiplied by factor, and a new integer is created.
This new integer is then assigned back to the same index of the list, effectively mutating the list's contents.
"""

# Had we implemented the scale function as follows, does it work properly?

def scaleV2(data, factor):
    for val in data:
        val *= factor
    print(data)

data2 = [1, 2, 3]
scaleV2(data2, 3)

"""
No, scaleV2 does not work properly. This is because scaleV2 is attempting to change the immutable elements of the list.

scaleV2 does create new instances of the values in the list, but it does not actually modify the list because it is 
not assigning val back to the same index in the list. So, the list remains unmodified.

Rebinding does not affect the list: In this version, val is a temporary variable that holds a copy of the value at each
position in the list (since the elements of the list are fetched one by one). The operation val *= factor modifies this 
temporary variable, but it does not affect the original list because the list itself is not being accessed or updated.

List remains unmodified: Since there is no reassignment to the indices of the list (like data[j] in the original
version), the list remains unchanged.
"""