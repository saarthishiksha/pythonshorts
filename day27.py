### 1. Basic Return Statement
def add(a, b):
    return a + b
result = add(5, 3)
print(result)  # Output: 8
### 2. Multiple Return Statements
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(check_even_odd(10))  # Output: Even
print(check_even_odd(7))   # Output: Odd
### 3. Returning Multiple Values
def get_coordinates():
    return (10, 20)
x, y = get_coordinates()
print(f"x: {x}, y: {y}")  # Output: x: 10, y: 20
### 4. Return Statement Without Value
def no_return():
    print("This function does not return anything.")
result = no_return()
print(result)  # Output: None
### 5. Using Return in Recursive Functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # Output: 120