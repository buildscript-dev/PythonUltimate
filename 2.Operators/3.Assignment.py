# Assignment Operators (=)
# Used to assign values to variables

name = input("Enter your name: ")
print("Hello,", name)


# Reassigning values (overwriting the old value)
num = 123
num = num + 123   # now num = 246
num = num + 123   # now num = 369
print("Reassigned num:", num)


# Compound assignment operators
# These combine arithmetic with assignment
# Examples: +=, -=, *=, /=, //=, %=, **=

num1 = 123
num1 += 1232   # equivalent to num1 = num1 + 1232
print("After compound assignment:", num1)
