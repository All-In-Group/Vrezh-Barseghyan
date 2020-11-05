print("1)")

# Exercise Question 1: Add a list of elements to a given set

sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(sampleList)
print(sampleSet)

print("---------------------------------------------")
print("2)")

# Exercise Question 2: Return a set of identical items from a given two Python set

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.intersection(set2))

print("---------------------------------------------")
print("3)")

# Exercise Question 3: Returns a new set with all items from both sets by removing duplicates

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.union(set2))

print("---------------------------------------------")
print("4)")

# Exercise Question 4: Given two Python sets, update first set with items that exist only in the first set and not in the second set.

set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)
print(set1)

print("---------------------------------------------")
print("5)")


#Exercise Question 5: Remove 10, 20, 30 elements from a following set at once

set1 = {10, 20, 30, 40, 50}

set1.difference_update({10, 20, 30})
print(set1)

print("---------------------------------------------")
print("6)")

# Exercise Question 6: Return a set of all elements in either A or B, but not both

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1.symmetric_difference(set2))

print("---------------------------------------------")
print("7)")

# Exercise Question 7: Determines whether or not the following two sets have any elements in common. If yes display the common elements

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if set1.isdisjoint(set2):
  print("Two sets have no items in common")
else:
  print("Two sets have items in common")
  print(set1.intersection(set2))

print("---------------------------------------------")
print("8)")

# Exercise Question 8: Update set1 by adding items from set2, except common items

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference_update(set2)
print(set1)

print("---------------------------------------------")
print("9)")

#Exercise Question 9: Remove items from set1 that are not common to both set1 and set2

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.intersection_update(set2)
print(set1)