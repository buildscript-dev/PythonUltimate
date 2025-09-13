# Logical Operators in Python
# These operators are used to combine multiple conditions 
# and return a Boolean result (True or False).

# Types of logical operators:
# 1. AND (and) - Returns True only if *all* conditions are True.
print(123 > 100 and 232 == 232)   # True because both conditions are True
print(123 > 100 and 232 == 232 and 123 == 1234)   # False because the last condition is False

# Note: AND has short-circuit behavior. 
# If it finds a False condition, it stops checking further.

# 2. OR (or) - Returns True if *at least one* condition is True.
print(123 == 1234 or 23 == 123 or 123 > 123 or 78 > 12)   # True because the last condition is True

# OR also has short-circuit behavior.
# It stops checking once it finds a True condition.

# 3. NOT (not) - Reverses the Boolean value.
# If the condition is True, it becomes False.
# If the condition is False, it becomes True.
print(not 123 == 123)   # False because 123 == 123 is True, and NOT makes it False
