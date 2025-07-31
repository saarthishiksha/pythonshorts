### 1. Parameters
def greet(name):  # 'name' is a parameter
    print(f"Hello, {name}!")
### 2. Arguments
greet("Alice")  # "Alice" is an argument
### 3. Positional Arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")
introduce( 30,"Bob")  # Output: My name is Bob and I am 30 years old.
### 4. Keyword Arguments
introduce(age=25, name="Alice")  # Output: My name is Alice and I am 25 years old.
### 5. Default Parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")
greet()        # Output: Hello, Guest!
greet("Bob")  # Output: Hello, Bob!
### 6. Variable-Length Arguments
# `*args`: Ye non-keyword variable-length arguments ko handle karta hai:  
def add_numbers(a,*args):
    return sum(args)
print(9,add_numbers(1, 2, 3, 4,5))  # Output: 10
# `**kwargs`: Ye keyword variable-length arguments ko handle karta hai:  
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=25,rollno=1)  