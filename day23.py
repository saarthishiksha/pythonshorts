# 1. String Create Karna
text = "Hello, World!"
print(text)
# 2. String Indexing
print(text[0])  # H
print(text[1])  # e
print(text[2])  # l
print(text[3])  # l
print(text[4])  # o 
# 3. String Slicing
print(text[0:5])  # Hello
print(text[7:12])  # World
print(text[-1])  # !
# 4. String Length
print(len(text))  # 13
# 5. String Ko Uppercase Mein Convert Karna
print(text.upper())  # HELLO, WORLD!
# 6. String Ko Lowercase Mein Convert Karna
print(text.lower())  # hello, world!
# 7. String Ko Title Case Mein Convert Karna
print(text.title())  # Hello, World!
# 8. String Se Whitespace Remove Karna
print(text.strip())  # Hello, World!
# 9. String Ko Split Karna
print(text.split(","))  # ['Hello', ' World!']
# 10. String Ko Join Karna
words = ['Hello', 'World!']
print(" ".join(words))  # Hello World!
# 11. String Mein Substring Ki Position Pata Karna
print(text.find("World"))  # 7
# 12. String Mein Substring Ki Count Pata Karna
print(text.count("l"))  # 3
# 13. String Ko Replace Karna
print(text.replace("World", "Python"))  # Hello, Python!
# 14. String Ko Check Karna Ki Wo Alphanumeric Hai Ya Nahi
print(text.isalnum())  # False