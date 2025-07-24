#Set Create 
fruits = {"Apple", "Banana", "Cherry"}
#or using set constructor
fruits = set(["Apple", "Banana", "Cherry"])
#Set Access Karna
# Accessing elements in a set is not possible by index as sets are unordered.
# However, you can check for membership or iterate through the set.
for fruit in fruits:
    print(fruit)
# Adding an element
fruits.add("Orange")
print(fruits)  # Output: {'Apple', 'Banana', 'Cherry', 'Orange'}    
# Removing an element
fruits.remove("Banana")
print(fruits)  # Output: {'Apple', 'Cherry', 'Orange'}
# Discarding an element (does not raise an error if the element is not found)
fruits.discard("Grapes")  # No error if "Grapes" is not in the set
### 5. Set Operations
# Set operations like union, intersection, difference, and symmetric difference
# can be performed on sets. 
# Set union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)  # Output: {1, 2, 3, 4, 5}
# Set intersection
intersection_set = set1 & set2
print(intersection_set)  # Output: {3}    
# Set difference
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}
# Set symmetric difference
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
# Set length
print(len(fruits))  # Output: Number of unique elements in the set  
