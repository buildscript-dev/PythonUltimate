l = [12, -1232, -12, 53, 2, -1]
print("Before sorting:", l)

l.sort()
print("After sorting:", l)

for i in l:
    if i >= 0:
        print(f"Positive value: {i}")
    else:
        print(f"Negative value: {i}")

largest = l[0]
secondLargest = l[0]

for i in range(len(l)):
    if l [i]> largest:
        largest = l[i]
        index = i

for i in l:
    if l > largest:
        secondLargest = largest
        largest = i-1




print(f"You largest number is {largest} at index {index}")
print(f"You largest number is {secondLargest} at index {index}")
    