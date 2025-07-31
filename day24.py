### 1. Slicing Syntax
#sequence[start:stop:step]
### 2. String Slicing
text = "Hello, World!"
# *Basic Sli cing*
print(text[0:5])  # Output: Hello
print(text[:5])   # Output: Hello (start se 5 tak)
print(text[7:])   # Output: World! (7 se end tak)
# *Negative Indexing*
print(text[-6:])  # Output: World! (last 6 characters)
# *Slicing with Step*
print(text[::2])  # Output: Hlo ol! (har 2nd character)
### 3. List Slicing
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# *Basic Slicing*
print(numbers[2:5]) # Output: [2, 3, 4]
print(numbers[:3])    # Output: [0, 1, 2]
print(numbers[5:])    # Output: [5, 6, 7, 8, 9]
print(numbers[-3:])   # Output: [7, 8, 9]
print(numbers[::3])    # Output: [0, 3, 6, 9] (har 3rd element)
### 4. Tuple Slicing
fruits = ("Apple", "Banana", "Cherry", "Date", "Elderberry")
print(fruits[1:4])  # Output: ('Banana', 'Cherry', 'Date')
