### 1. Function Define
def greet():
    print("Hello, World!")
### 2. Function Call
greet()
### 3. Function with Parameters
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
### 4. Function with Return Statement
def add(a, b):
    return a + b
add(4,6)
result = add(5, 3)
print(result)  # Output: 8
### 5. Default Parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()        # Output: Hello, Guest!
greet("Bob")  # Output: Hello, Bob!
### 6. Keyword Arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")
introduce(age=25, name="Alice")
### 7. Variable-Length Arguments
def add_numbers(*args):
    return sum(args)
print(add_numbers(1, 2, 3, 4))  # Output: 10