from functools import reduce

# 1. Generate numbers from 1 to 20
numbers = list(range(1, 21))
print("1. Numbers from 1 to 20:")
print(numbers)
print("-" * 50)

# 2. Filter only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("2. Filtered even numbers:")
print(even_numbers)
print("-" * 50)

# 3. Square the filtered numbers
squared_numbers = list(map(lambda x: x**2, even_numbers))
print("3. Squared even numbers:")
print(squared_numbers)
print("-" * 50)

# 4. Sum of squared even numbers
sum_of_squares = reduce(lambda a, b: a + b, squared_numbers)
print("4. Sum of squared even numbers:")
print(sum_of_squares)
print("-" * 50)

# 5. Enumerate the squared numbers
print("5. Index and value of squared even numbers:")
for index, value in enumerate(squared_numbers):
    print(f"Index {index}: {value}")
