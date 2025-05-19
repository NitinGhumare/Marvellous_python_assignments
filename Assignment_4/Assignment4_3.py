# 3.
# Write a program that uses filter( ), map( ) and reduce( ).
# Specifications

# The program works with one list of numbers entered by the user.

# filter( ) keeps every number ≥ 70 and ≤ 90.

# map( ) adds 10 to each remaining number.

# reduce( ) returns the product of the mapped numbers.

# Input List      : [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# After filter    : [76, 89, 86, 90, 70]
# After map       : [86, 99, 96, 100, 80]
# Output (reduce) : 6538752000

from functools import reduce

numbers = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]

print("Input List :", numbers)


filtered = list(filter(lambda x: 70 <= x <= 90, numbers))

print("After filter :", filtered)

mapped = list(map(lambda x: x + 10, filtered))

print("After map  :", mapped)


product = reduce(lambda x, y: x * y, mapped)

print("Output (reduce):", product)
