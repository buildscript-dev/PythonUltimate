
# To Take UserInput we can use,
# Input(): Input Function, by default it return string...

name = input("Enter your name: ")
# Oooh, It takes input but haven't returned anything?
# So, we need to use print() for that,

# print(name)
# So, It's print my name but it don't look good
# Then use this to look good.
print("Hello,", name)

# Next if we want to do addition,
# firstNum = input("Enter you firstNum: ")
# secondNum = input("Enter you secondNum: ")

# print(firstNum + secondNum)
# Fuck, the output is not correct,
# Yes, Because it is by default string, So convert it into int or float,

# 1. Way
# firstNum = int(firstNum)
# secondNum = int(secondNum)
# 2. Way
firstNum = int(input("Enter your firstNum: "))
secondNum = int(input("Enter your secondNum: "))
print( firstNum + secondNum)


# output
print(f"my name is {name}.")