print("1)")

# Exercise Question 1: Given a Python list you should be able to display Python list in the following order

q = [100, 200, 300, 400, 500]

q = q[::-1]
print(q)

print("---------------------------------------------")
print("2)")

# Exercise Question 2: Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)
print("---------------------------------------------")
print("3)")

# Exercise Question 3: Given a Python list. Turn every item of a list into its square

l = [1, 2, 3, 4, 5, 6, 7]
l = [x * x for x in l]
print(l)

print("---------------------------------------------")
print("4)")

# Exercise Question 4: Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

for i in list1:
    for o in list2:
        a = [i + o]
        print(a, end='')
print()
print("---------------------------------------------")
print("5)")

# Exercise Question 5: Given a two Python list. Iterate both lists simultaneously such that list1 should display item in original order and list2 in reverse order

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

print("---------------------------------------------")
print("6)")

# Exercise Question 6: Remove empty strings from the list of strings

z = ["Mike", "", "Emma", "Kelly", "", "Brad"]
z = list(filter(None, z))
print(z)
print("---------------------------------------------")
print("7)")

# Exercise Question 7: Add item 7000 after 6000 in the following Python List

x = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
x[2][2].append(7000)
print(x)
print("---------------------------------------------")
print("8)")

# Exercise Question 8: Given a nested list extend it with adding sub list ["h", "i", "j"] in a such a way that it will look like the following list

x = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
y = ["h", "i", "j"]

x[2][1][2].extend(y)
print(x)

print("---------------------------------------------")
print("9)")

# Exercise Question 9: Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

a = [5, 10, 15, 20, 25, 50, 20]

index = a.index(20)
a[index] = 200
print(a)
print("---------------------------------------------")
print("10)")

# Exercise Question 10: Given a Python list, remove all occurrence of 20 from the list

list1 = [5, 20, 15, 20, 25, 50, 20]


def removeValue(sampleList, val):
    return [value for value in sampleList if value != val]


resList = removeValue(list1, 20)
print(resList)
