print("1)")

# Exercise Question 1: Given a two list. Create a third list by picking an odd-index element from the first list and even index elements from second.

listOne = [3, 6, 9, 12, 15, 18, 21]
listTwo = [4, 8, 12, 16, 20, 24, 28]
listThree = []

oddElements = listOne[1::2]
print("Element at odd-index positions from list one")
print(oddElements)

EvenElement = listTwo[0::2]
print("Element at even-index positions from list two")
print(EvenElement)

print("Printing Final third list")
listThree.extend(oddElements)
listThree.extend(EvenElement)
print(listThree)

print("---------------------------------------------")
print("2)")

# Exercise Question 2: Given an input list removes the element at index 4 and add it to the 2nd position and also, at the end of the list

l = [54, 44, 27, 79, 91, 41]

print("Original list ", l)
e = l.pop(4)
print("List After removing element at index 4 ", l)

l.insert(2, e)
print("List after Adding element at index 2 ", l)

l.append(e)
print("List after Adding element at last ", l)

print("---------------------------------------------")
print("3)")

# Exercise Question 3: Given a list slice it into a 3 equal chunks and rever each list
my_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


n = 3

x = list(divide_chunks(my_list, n))
print(x)

print("---------------------------------------------")
print("4)")

# Exercise Question 4: Given a list iterate it and count the occurrence of each element and create a dictionary to show the count of each element

sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sampleList)

count = {}
for i in sampleList:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

print("Printing count of each item  ", count)

print("---------------------------------------------")
print("5)")

# Exercise Question 5: Given a two list of equal size create a set such that it shows the element from both lists in the pair


firstList = [2, 3, 4, 5, 6, 7, 8]
secondList = [4, 9, 16, 25, 36, 49, 64]
print("First List ", firstList)
print("Second List ", secondList)
print(set(zip(firstList, secondList)))

print("---------------------------------------------")
print("6)")

# Exercise Question 6: Given a following two sets find the intersection and remove those elements from the first set


first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print("First Set ", first_set)
print("Second Set ", second_set)

intersection = first_set.intersection(second_set)
print("Intersection is ", intersection)
for item in intersection:
    first_set.remove(item)

print("---------------------------------------------")
print("7)")

# Exercise Question 7: Given two sets, Checks if One Set is Subset or superset of Another Set. if the subset is found delete all elements from that set

firstSet = {57, 83, 29}
secondSet = {57, 83, 29, 67, 73, 43, 48}

print(f"First Set {firstSet}")
print(f"Second Set {secondSet}")

print(f"First set is Super set of second set -  {firstSet.issubset(secondSet)}")
print(f"Second set is Super set of First set -  {secondSet.issubset(firstSet)}")

print(f"First set is Super set of second set -  {firstSet.issuperset(secondSet)}")
print(f"Second set is Super set of First set -  {secondSet.issuperset(firstSet)}")

if firstSet.issubset(secondSet):
    firstSet.clear()
elif secondSet.issubset(firstSet):
    secondSet.clear()

print(f"First Set {firstSet}")
print(f"Second Set {secondSet}")

print("---------------------------------------------")
print("8)")

# Exercise Question 8: Iterate a given list and Check if a given element already exists in a dictionary as a key’s value if not delete it from the list

rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
sampleDict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

print(f"List - {rollNumber}")
print(f"Dictionary -  {sampleDict}")

rollNumber[:] = [item for item in rollNumber if item in sampleDict.values()]
print("after removing unwanted elemnts from list ", rollNumber)

print("---------------------------------------------")
print("9)")

# Exercise Question 9: Given a dictionary get all values from the dictionary and add it in a list but don’t add duplicates

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

print(f"Speed = {speed}")

speedList = []
for i in speed.values():
    if i not in speedList:
        speedList.append(i)
print("unique list", speedList)


print("---------------------------------------------")
print("10)")

# Exercise Question 10: Remove duplicate from a list and create a tuple and find the minimum and maximum number

z = [87, 45, 41, 65, 94, 41, 99, 94]

unique = list(set(z))
print(f"Unique items {list(set(z))}")
tup = tuple(unique)
print(f"Tuple {tup}")
print(f"min: {min(tup)}")
print(f"max: {max(tup)}")