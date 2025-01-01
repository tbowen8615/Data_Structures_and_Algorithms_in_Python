# Demonstrate how to use Python's List Comprehension syntax to produce the list
# ['a', 'b', 'c', 'd', 'e', ..., 'z']

result = [chr(x) for x in range(97, 123)]
resultV2 = [chr(x) for x in range(ord('a'), ord('z') + 1)]

print(result)
print(resultV2)