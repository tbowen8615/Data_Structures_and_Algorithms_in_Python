# Python allows negative integers to be used as indices into a sequence, such as a string.
# If string s has length n, and expression s[k] is used for index
# -n <= k < 0, what is the equivalent index >= 0 such that s[j]
# references the same element?

s = "Tyler"
# len(s) = 5
# -5 <= k < 0
print(s[-1], s[-1 + 5])
print(s[-2], s[-2 + 5])
print(s[-3], s[-3 + 5])
print(s[-4], s[-4 + 5])
print(s[-5], s[-5 + 5])

# equivalent index is s[k + n] where j = k + n