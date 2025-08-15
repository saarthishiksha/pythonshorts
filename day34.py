### 1. Class Kya Hote Hain?
class Dog:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute

    def bark(self):      # Method
        return "Woof!"
### 2. Object Kya Hote Hain?
my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
print(my_dog.bark())  # Output: Woof!
### 3. Constructor Method
class Cat:
    def __init__(self, name):
        self.name = name

my_cat = Cat("Whiskers")
print(my_cat.name)  # Output: Whiskers
### 4. Instance vs Class Variables
class Circle:
    pi = 3.14  # Class variable

    def __init__(self, radius):
        self.radius = radius  # Instance variable
circle1 = Circle(5)
circle2 = Circle(10)
print(circle1.pi)  # Output: 3.14
print(circle2.radius)  # Output: 10
### 5. Inheritance
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):  # Dog class inherits from Animal
    def bark(self):
        return "Woof!"

my_dog = Dog()
print(my_dog.speak())  # Output: Animal speaks
### 6. Polymorphism
class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal):
    print(animal.speak())

animal_sound(my_dog)  # Output: Animal speaks
animal_sound(Cat())    # Output: Meow!