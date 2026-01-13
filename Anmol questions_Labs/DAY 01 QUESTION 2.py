#Question – List, Dictionary & Set Comprehensions

data = [1, 2, 3, 4, 5, 6, 2, 4]

# 1. List comprehension to store squares of all numbers
squares = [x**2 for x in data]
print("Squares:", squares)

# 2. Set comprehension to store only unique even numbers
unique_even_numbers = {x for x in data if x % 2 == 0}
print("Unique even numbers:", unique_even_numbers)

# 3. Dictionary comprehension where key is the number and value is its cube
cube_dict = {x: x**3 for x in data}
print("Number and its cube:", cube_dict)
