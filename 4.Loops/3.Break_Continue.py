# 'break' immediately exits the loop when a condition is met.

for i in range(1, 12):
    if i == 10:  # Condition to stop the loop
        break    # End/exit the loop here
    else:
        print(i) # Prints numbers from 1 to 9


# is break runs then else didn't  if else then break don't 

# 'continue' skips the current iteration and moves to the next one.

for i in range(1, 12):
    if i == 10:  # Condition to skip
        continue # Skip this iteration and move to next
    else:
        print(i) # Prints numbers from 1 to 11, except 10
