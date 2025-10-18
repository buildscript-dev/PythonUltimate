# -------------------------------
# What is a while loop?
# -------------------------------
# A while loop keeps repeating a block of code
# as long as the condition is True.
# When the condition becomes False, the loop stops.

# -------------------------------
# Example 1: Simple Counting
# -------------------------------
import random


count = 1
print("Example 1: Counting from 1 to 5")
while count <= 5:              # loop runs while count is less than or equal to 5
    print("Number:", count)
    count += 1                 # increase count by 1 each time
print("Loop finished!\n")       # this runs after the loop ends


# -------------------------------
# Example 2: Infinite Loop (be careful!)
# -------------------------------
# This loop will go on forever because the condition is always True.
# I will demonstrate it but stop it quickly using break.
print("Example 2: Infinite loop demo with break")
loop_counter = 1
while True:                     # condition always True
    print("Looping... step", loop_counter)
    loop_counter += 1
    if loop_counter > 3:        # we manually stop it after 3 loops
        break
print("Stopped the infinite loop!\n")


# -------------------------------
# Example 3: Using break inside a loop
# -------------------------------
print("Example 3: Break when n == 4")
n = 1
while True:
    if n == 4:                  # break when n reaches 4
        break
    print(n)
    n += 1
print("Loop ended because of break!\n")


# -------------------------------
# Example 4: Using Floor Division
# -------------------------------
print("Example 4: Enter you number: ")
a = int(input("Enter Your Number"))
while a > 0:
    print(a % 10)
    a = a // 10


# -------------------------------
# Example 5: Print in Reverse
# -------------------------------
b = int(input("Example 5: Enter Your Number: "))
copy = b
rev = 0
while b > 0:
    rev = rev * 10 + b % 10
    b = b //10

if copy == rev:
    print("It is Pallindromic Number")
else: 
    print("It is not Pallindromic Number")
    

# -------------------------------
# Example 6: Random Number Generator
# -------------------------------
import random

randomNumber = random.randint(1, 10)  # use 1–10 (11 would make 10 possible too)
tries = 0

while True:
    guessNumber = int(input("Guess Your Number: "))
    tries += 1  # count every attempt
    
    if randomNumber == guessNumber:
        print("You are Right! 🎉")
        print(f"It took you {tries} tries.")
        break
    elif randomNumber < guessNumber:
        print("Go a little lower...")
    elif randomNumber > guessNumber:
        print("Go a little higher...")

# -------------------------------
# Example 7: 
# -------------------------------