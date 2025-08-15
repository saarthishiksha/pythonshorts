### 1. File Open Karna
file = open("day31.txt", "r")  # "r" mode for reading
### 2. Reading the Entire File
content = file.read()
print(content)
### 3. Reading Line by Line
# Using readline()
file= open("day31.txt", "r")  # Reopen the file
line = file.readline()
while line:
    print(line.strip())  # strip() removes leading/trailing whitespace
    line = file.readline()
# Using readlines()
# file.seek(0)  # Move the cursor back to the beginning of the file
# lines = file.readlines()
# for line in lines:
#     print(line.strip())
### 4. Using a Context Manager
with open("day31.txt", "r") as file:
    content = file.read()
    print(content)
### 5. Handling File Not Found Error
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
### 6. Reading Binary Files
with open("day31.png", "rb") as file:
    content = file.read()
print(type(content))
    # Process binary content