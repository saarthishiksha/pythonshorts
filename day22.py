### 1. Dictionary Create
# Dictionary banane ka syntax
# dictionary_name = {key1: value1, key2: value2, ...}
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
### 2. Dictionary Access Karna
# Dictionary ke elements ko access karne ke liye key ka use hota hai:
print(student["name"])  # Output: Alice
print(student["age"])   # Output: 20
print(student["major"])  # Output: Computer Science
### 3. Dictionary Mein Item Add Karna
student["graduation_year"] = 2023
print(student)  # Output: {'name': 'Alice', 'age': 20, 'major': 'Computer Science', 'graduation_year': 2023}
### 4. Dictionary Mein Item Update Karna
student["age"] = 21 # Age ko update kar rahe hain   
print(student)  # Output: {'name': 'Alice', 'age': 21, 'major': 'Computer Science', 'graduation_year': 2023}
### 5. Dictionary Mein Item Delete Karna
del student["major"]  # Major ko delete kar rahe hain
print(student)  # Output: {'name': 'Alice', 'age': 21, 'graduation_year': 2023}
### 5.1 Dictionary Mein Item Delete Karna Aur Value Ko Store Karna
# Agar aap item ko delete karte waqt uski value ko store karna chahte hain
# to aap pop() method ka use kar sakte hain:
major = student.pop("major")
print(major)    # Output: Computer Science
print(student)  # Output: {'name': 'Alice', 'graduation_year': 2023}
### 6. Dictionary Mein Keys Aur Values Ko Iterate Karna
for key, value in student.items():
    print(f"Key: {key}, Value: {value}")
### 8. Dictionary Ka Length Pata Karna
print(len(student))  # Output: 3 (kyunki ab dictionary mein 3 items hain)
### 9. Dictionary Ko Copy Karna
student_copy = student.copy()  # Copy kar rahe hain
print(student_copy)  # Output: {'name': 'Alice', 'age': 21, 'graduation_year': 2023}
### 10. Dictionary Comprehension
squared_numbers = {x: x**2 for x in range(1, 6)}
print(squared_numbers)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
### 7. Dictionary Mein Check Karna Ki Key Hai Ya Nahi
if "name" in student:   
    print("Name key exists in the dictionary.") # Output: Name key exists in the dictionary.
else:
    print("Name key does not exist in the dictionary.")