### 1. Tuple Create Karna
fruits = ("Apple", "Banana", "Cherry")
### 2. Tuple Access Karna
print(fruits[0])  # Apple
print(fruits[1])  # Banana
print(fruits[2])  # Cherry
### 3. Tuple Length Pata Karna
print(len(fruits))
### 4. Tuple Mein Item Count Karna
print(fruits.count("Apple"))
### 5. Tuple Mein Item Index Pata Karna
print(fruits.index("Cherry"))
### 6. Tuple Ko Unpack Karna
a, b, c = fruits
print(a)  # Apple
print(b)  # Banana
print(c)  # Cherry
### 7. Tuple Ko Join Karna
joined = ",".join(fruits)
print(joined)  # Apple,Banana,Cherry
### 8. Tuple Ko Sort nhi Kar Sakte
# Tuples are immutable, so we cannot sort them directly.
### 9. Tuple Ko Create Karne Ke Different Ways
vegetables = "Carrot", "Potato", "Tomato"
print(vegetables)
### 10. Tuple Ko List Se Create Karna
tuple2 = tuple(["Apple", "Banana", "Cherry"])
print(tuple2)