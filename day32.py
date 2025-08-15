### 1. File Open Karna for Writing
# Using "w" mode
file = open("content.txt", "w")
### 2. Writing to a File
with open("content.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.")
### 3. Writing Multiple Lines
lines = ["First line.\n", "Second line.\n", "Third line.\n"]
with open("content.txt", "w") as file:
    file.writelines(lines)
### 4. Appending to a File
with open("content.txt", "a") as file:
    file.write("\nThis line is appended.")
### 5. Handling Exceptions
try:
    with open("content.txt", "w") as file:
        file.write("Writing to the file.")
except IOError:
    print("Error: Unable to write to the file.")
### 6. Writing Binary Files
with open("day32.png", "wb") as file:
    file.write(binary_data)  # binary_data should be in bytes
    type(file)