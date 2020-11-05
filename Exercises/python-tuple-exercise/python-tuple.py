print("1)")

# Exercise Question 1: Reverse the following tuple

aTuple = (10, 20, 30, 40, 50)

print(aTuple[::-1])

print("---------------------------------------------")
print("2)")

# Exercise Question 2: Access value 20 from the following tuple

aTuple = ("Orange", [10, 20, 30], (5, 15, 25))

print(aTuple[1][1])

print("---------------------------------------------")
print("3)")

# Exercise Question 3: Create a tuple with single item 50

aTuple = (50)
print(aTuple)

print("---------------------------------------------")
print("4)")

# Exercise Question 4: Unpack the following tuple into 4 variables

aTuple = (10, 20, 30, 40)
a, b, c, d = aTuple
print(f"{a} {b} {c} {d}")

print("---------------------------------------------")
print("5)")

# Exercise Question 5: Swap the following two tuples

tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1, tuple2 = tuple2, tuple1
print(f"tuple1 = {tuple1}, tuple2 = {tuple2}")

print("---------------------------------------------")
print("6)")

# Exercise Question 6: Copy element 44 and 55 from the following tuple into a new tuple

tuple1 = (11, 22, 33, 44, 55, 66)

tuple2 = tuple1[3:5]
print(tuple2)

print("---------------------------------------------")
print("7)")

# Exercise Question 7: Modify the first item (22) of a list inside a following tuple to 222

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

print("---------------------------------------------")
print("8)")

# Exercise Question 8: Sort a tuple of tuples by 2nd item

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)

print("---------------------------------------------")
print("9)")

# Exercise Question 9: Counts the number of occurrences of item 50 from a tuple

tuple1 = (50, 10, 60, 70, 50)

print(tuple1.count(50))

print("---------------------------------------------")
print("10)")


# Exercise Question 10: Check if all items in the following tuple are the same

def tuple(t):
    return all(i == t[0] for i in t)


tuple1 = (45, 45, 45, 45)
print(tuple(tuple1))
