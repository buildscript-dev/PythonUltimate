# Conditional Statements
# They allow decision-making by executing different blocks of code based on conditions.

# -----------------------------
# 1. If Statement
# Runs a block of code only if the condition is true
a = 123
if a > 10:
    print("I will do task A")   # This will run because a > 10 is True


# -----------------------------
# 2. If–Else Statement
# Runs one block if the condition is true, otherwise runs the other
if a > 100:
    print("I will do task A")
else:
    print("I will do task B")   # This runs only if a <= 100


# -----------------------------
# 3. If–Elif–Else Statement
# Used when there are multiple conditions to check
money = int(input("Enter the money you have: "))

if money == 10:
    print("I will have choti advance")
elif money == 20:
    print("I will have choti advance + fruti")
else:
    print("I will buy Red Bull")
