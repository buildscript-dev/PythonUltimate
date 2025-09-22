# -------------------------------
# For Loop in Python
# -------------------------------
# A for loop is used to repeat a block of code (iteration).
# It works with sequences like lists, tuples, strings, sets, or with numbers using range().
# The loop variable (often called 'i') changes value each time.
# You can name the loop variable anything, not just 'i'.

# -------------------------------
# Range Function
# -------------------------------
# range() generates a sequence of numbers.
# Syntax: range(start, stop, step)
# - start (optional) → starting number (default 0)
# - stop (required)  → ending number (excluded!)
# - step (optional)  → how much to increase/decrease each time (default 1)

# Example 1: Iterating from 0 to 4
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Example 2: Iterating from 1 to 10
for i in range(1, 11):  # 1 through 10
    print(i)

# Example 3: Using step (increment by 2)
for i in range(1, 15, 2):  # 1, 3, 5, ..., 13
    print(i)

# Example 4: Reverse loop (counting down)
for i in range(10, 0, -1):  # 10 down to 1
    print(i)


# -------------------------------
# Practical Examples
# -------------------------------

# Multiplication table of 5
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)

# Multiplication table of 7
for i in range(7, 71, 7):  # 7, 14, ..., 70
    print(i)

# Universal multiplication table
n = int(input("Which table do you want? "))
for i in range(n, (n * 10) + 1, n):  # n, 2n, 3n, ..., 10n
    print(i)

# Direct Method
name = "BuildScript is Cool"

for i in name:
    print(i)