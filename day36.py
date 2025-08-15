### 2. Standard Libraries
# - **math**: Mathematical functions aur constants.
# - **datetime**: Date aur time operations.
# - **os**: Operating system ke functionalities.
# - **sys**: Python interpreter ke functionalities.
import math
print(math.sqrt(16))
### 3. Third-Party Libraries
# pip install requests
### 4. Using Third-Party Libraries
import requests
response = requests.get("https://api.github.com")
print(response.status_code)  # Output: 200
### 5. Creating Your Own Library
# my_library.py
def greet(name):
    return f"Hello, {name}!"
# main.py
from my_module import greet
print(greet("Alice"))  # Output: Hello, Alice!