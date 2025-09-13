# 1. If Statement
# Used to run a block of code only when the condition is True

a = 123
b = 456

if a > 10:   # checks the condition
    print(f"I will do task A {a}")   # runs only if condition is True

# If condition is false the it don't do anything.


# Write a program to check if a number is greater than 50.
print("Check the Number is greater then 50 or not")

num = int(input("Enter your number: "))

if num > 50: 
    print(f"Yoo, Your number {num} is greater then 50")


# Check if a person’s age is above 18, then print “You are an adult”.
print("Checking a persons age")
 
age = int(input("Enter your age: "))

if age >= 18:
    print("You are adult")