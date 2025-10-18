# ------------------------------------
# Python Notes: List
# ------------------------------------
# A List in Python is a collection that allows you to store multiple values in a single variable.
# Lists are very flexible and commonly used.

# Keywords describing a List:
# 1. Mutable      → values inside a list can be changed.
# 2. Duplicate    → allows duplicate values.
# 3. Ordered      → elements are stored in an index order (you can access them by position).
# 4. Heterogeneous → can store different data types (string, int, float, bool, etc.).


# ------------------------------------
# List Basics
# ------------------------------------
fruits = ["apple", "banana", "coconut", "kiwi", "dragon fruit"]

# Indexing (accessing values)
print("First element:", fruits[0])       # apple
print("Second last element:", fruits[-2]) # kiwi
print("Complete List:", fruits)


# ------------------------------------
# Ways of Iterating (looping) over a List
# ------------------------------------

# 1st Way → Direct Index Access
print("\nLoop using range(len(fruits)):")
for i in range(len(fruits)):
    print(fruits[i])

# 2nd Way → Direct Iteration
print("\nLoop directly through items:")
for fruit in fruits:
    print(fruit)


# ------------------------------------
# What is a Method?
# ------------------------------------
# A method is like a function, but it is called using a dot (.)
# Methods are built-in actions that can be performed on objects like lists.


# ------------------------------------
# Common List Methods
# ------------------------------------

# append() → Adds value at the END
fruits.append("grapes")
print("\nAfter append:", fruits)

# insert() → Adds value at a specific index
fruits.insert(3, "mango")   # inserts mango at index 3
print("After insert:", fruits)

# remove() → Removes a specific value (first occurrence)
fruits.remove("grapes")
print("After remove:", fruits)

# sort() → Sorts the list (alphabetical in this case)
fruits.sort()               # sorts in ascending order
print("After sort:", fruits)

# reverse() → Reverses the list order
fruits.reverse()
print("After reverse:", fruits)

# pop() → Removes and returns the last element (or specific index)
popped_item = fruits.pop()  
print("After pop:", fruits, "| Popped:", popped_item)

# clear() → Empties the list completely
copy_list = fruits.copy()   # making a copy before clearing
fruits.clear()
print("After clear:", fruits, "| Copy remains:", copy_list)
