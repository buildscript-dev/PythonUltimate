# For Loop
# It's used to iterate over a sequence (like a list, tuple, dictionary, set, or string) it's finite
# It works on the basis of number
# i is a variable that changes its value in each iteration
# instead of i we can use any variable name
# iteration is the process of repeating a set of instructions a certain number of times     


# Range Function
# Used to generate a sequence of numbers, often used in for loops for iteration

# Example 1: Iterating through a range of numbers
for i in range(5):  # Loops from 0 to 4
    print(i)  # Prints the current number
    # Start form 0 and end at 4 (5 is excluded)

# we can also specify start and end values in range function
for i in range(1, 11):  # Loops from 1 to 10
    print(i)  # Prints the current number

    # we can also add step value in range function
    for i in range(1, 15, 2):  # Generates numbers from 1 to 14, incrementing by 2
        print(i)  # Prints the current number

        # we can also use this reverse order
        for i in range(10, 0, -1):  # Loops from 10 to 1
            print(i)  # Prints the current numbern



# Example 2: Print a table of 5
for i in range(1, 11):  # Loops from 1 to 10
    print("5 x ", i, " = ", 5 * i)  # Prints the multiplication table of 5