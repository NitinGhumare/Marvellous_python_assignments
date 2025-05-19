from functools import reduce

numbers = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

print("Input List :", numbers)

filtered = list(filter(lambda x: x % 2 == 0, numbers))
print("After filter:", filtered)

mapped = list(map(lambda x: x ** 2, filtered))
print("After map:", mapped)


total = reduce(lambda x, y: x + y, mapped)
print("Output (reduce)  :", total)
