# If–Elif–Else Statement
# Used when there are multiple conditions to check

money = int(input("Enter the money you have: "))  # user types a number, converted to integer

if money == 10:   # First condition
    print("I will have choti advance")   # Runs only if money is exactly 10

elif money == 20:   # Second condition (checked only if the first was False)
    print("I will have choti advance + fruti")

else:   # Fallback case if none of the above are True
    print("I will buy Red Bull")
