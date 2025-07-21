### 1. Break Statement
for i in range(10):
    if i == 5:
        break
    print(i)
### 2. Continue Statement
for i in range(5):
    if i == 2:
        continue
    print(i)
### 3. Using Break and Continue Together
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    if i == 7:
        break  # Stop when i is 7
    print(i)