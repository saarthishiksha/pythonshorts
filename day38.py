### 1. Random Module
import random
### 2. Generating Random Numbers
import random
random_float = random.random()
print(f"Random float between 0 and 1: {random_float}")
random_int = random.randint(1, 10)
print(f"Random integer between 1 and 10: {random_int}")
### 3. Random Choice from a List
fruits = ["apple", "banana", "cherry", "date"]
random_fruit = random.choice(fruits)
print(f"Random fruit selected: {random_fruit}")
### 4. Shuffling a List
deck = ["Ace", "King", "Queen", "Jack"]
random.shuffle(deck)
print(f"Shuffled deck: {deck}")
### 5. Generating Random Samples
numbers = list(range(1, 21))  # List of numbers from 1 to 20
random_sample = random.sample(numbers, 5)  # Select 5 unique random numbers
print(f"Random sample of 5 numbers: {random_sample}")
### 6. Setting a Seed
random.seed(40)  # Setting the seed
print(random.random())  # This will always produce the same output with the same seed