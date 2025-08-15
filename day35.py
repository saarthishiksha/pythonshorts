### 1. Self Keyword
class Person:
    def __init__(self, name, age):
        self.name = name  # self.name is an instance variable
        self.age = age    # self.age is an instance variable

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

person1 = Person("Alice", 30)
print(person1.introduce())  # Output: My name is Alice and I am 30 years old.
### 2. Constructor Method
class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
my_car = Car("Toyota", 2020)
print(my_car.model)  # Output: Toyota
print(my_car.year)   # Output: 2020
### 3. Default Values in Constructors
class Book:
    def __init__(self, title, author="Unknown"):
        self.title = title
        self.author = author

my_book = Book("1984")
print(my_book.author)  # Output: Unknown
### 4. Multiple Constructors (Using Class Methods)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod
    def square(cls, size):
        return cls(size, size)  # Calls the constructor

my_square = Rectangle.square(5)
print(my_square.width)  # Output: 5
print(my_square.height) # Output: 5  