### 1. Module Kya Hote Hain?
# my_module.py
# def greet(name):
#     return f"Hello, {name}!"
### 2. Importing a Module
import my_module
print(my_module.greet("Alice"))  # Output: Hello, Alice!
### 3. Importing Specific Functions
from my_module import greet
print(greet("Bob"))  # Output: Hello, Bob!
### 4. Importing with an Alias
import my_module as mm
print(mm.greet("Charlie"))  # Output: Hello, Charlie!
### 5. Importing All Functions
from my_module import * 
print(greet("Dave"))  # Output: Hello, Dave!
### 6. Creating Your Own Module
import math
print(math.sqrt(16))  # Output: 4.0
