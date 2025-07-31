### 1. Lambda Function Ka Syntax
# lambda arguments: expression
### 2. Basic Lambda Function
add=  lambda x, y: x + y
result = add(5, 3)
print(result)  # Output: 8
### 3. Lambda Function Ka Use
# - **Using `map()`**:  
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
# - **Using `filter()`**:  
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]
# - **Using `sorted()`**:  
pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda x: x[0])
print(sorted_pairs)  # Output: [(1, 'one'), (2, 'two'), (3, 'three')]
### 4. Lambda Functions with Multiple Arguments
multiply = lambda a, b, c: a * b * c
print(multiply(2, 3, 4))  # Output: 24
### 5. Limitations of Lambda Functions
def complex_function(x):
    if x > 0:
        return x * 2
    else:
        return x + 2
complex_function(4)