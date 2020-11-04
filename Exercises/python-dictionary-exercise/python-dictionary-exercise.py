print("1)")

# dictionary exercise 1: Below are the two lists convert it into the dictionary


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

a = dict(zip(keys, values))
print(a)

print("---------------------------------------------")
print("2)")

# dictionary exercise 2: Merge following two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

a = {**dict1, **dict2}
print(a)

print("---------------------------------------------")
print("3)")

# dictionary exercise 3: Access the value of key ‘history’

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])

print("---------------------------------------------")
print("4)")

# dictionary exercise 4: Initialize dictionary with default values

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

a = dict.fromkeys(employees, defaults)
print(a)

print("---------------------------------------------")
print("5)")

# dictionary exercise 5: Create a new dictionary by extracting the following keys from a given dictionary

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}

keys = ["name", "salary"]

x = {i: sampleDict[i] for i in keys}
print(x)

print("---------------------------------------------")
print("6)")

# dictionary exercise 6: Delete set of keys from Python Dictionary

sample = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
remove = ["name", "salary"]

sample = {k: sample[k] for k in sample.keys() - remove}
print(sample)

print("---------------------------------------------")
print("7)")

# dictionary exercise 7: Check if a value 200 exists in a dictionary

sampleDict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sampleDict.values():
    print(True)
else:
    print(False)

print("---------------------------------------------")
print("8)")

# dictionary exercise 8: Rename key city to location in the following dictionary

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

sampleDict['location'] = sampleDict.pop('city')
print(sampleDict)

print("---------------------------------------------")
print("9)")

# dictionary exercise 9: Get the key corresponding to the minimum value from the following dictionary


sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

for i in sampleDict.keys():
    if sampleDict[i] == min(sampleDict.values()):
        print(i)


print("---------------------------------------------")
print("10)")

# dictionary exercise 10: Given a Python dictionary, Change Brad’s salary to 8500

sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}

sampleDict['emp3']['salary'] = 8500
print(sampleDict)