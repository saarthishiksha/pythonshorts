# ZeroDivisionError
result = 10 / 0  # This will raise an exception
### 2. Try and Except Block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
### 3. Multiple Except Blocks
try:
    value = int(input("Enter a number: "))
    result = 10 / value
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")

### 4. Finally Block
try:
    file = open("example.txt", "r")
    # Perform file operations
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("This will always execute.")
### 5. Raising Exceptions
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    return "Access granted."
try:
    print(check_age(15))
except ValueError as e:
    print(e)  # Output: Age must be at least 18.

### 6. Custom Exception Classes
class CustomError(Exception):
    pass
try:
    raise CustomError("This is a custom error.")
except CustomError as e:
    print(e)  # Output: This is a custom error.
