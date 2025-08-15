### 1. Basic List Comprehension
# [expression for item in iterable]
squares = [x**2 for x in range(10)]
print(squares)  

### 2. Adding Conditions
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  

### 3. Nested List Comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  

### 4. Using Functions in List Comprehensions
def square(x):
    return x**2
squared_numbers = [square(x) for x in range(10)]
print(squared_numbers)  

### 5. Performance Benefits
# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)

# Using list comprehension
squares = [x**2 for x in range(10)]