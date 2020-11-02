import os

print("1)")

# Exercise Question 1: Accept two numbers from the user and calculate multiplication

a = int(input('First number: '))
b = int(input("Second number: "))


c = a * b
print(f"The answer is {c}")

print("---------------------------------------------")
print("2)")

# Exercise Question 2: Display “My Name Is James” as “My**Name**Is**James” using output formatting of a print() function

print('My', 'Name', 'Is', 'James', sep='**')
print("---------------------------------------------")
print("3)")

# Exercise Question 3: Convert decimal number to octal using print() output formatting

print('%o' % (8))
print("---------------------------------------------")
print("4)")

# Exercise Question 4: Display float number with 2 decimal places using print()

print('%.2f' % 458.541315)
print("---------------------------------------------")
print("5)")

# Exercise Question 5: Accept list of 5 float numbers as a input from user

l = []

a = float(input("Add number: "))
b = float(input("Add another number: "))
c = float(input("Add another number: "))
d = float(input("Add another number: "))
e = float(input("Add another number: "))

l.append(a)
l.append(b)
l.append(c)
l.append(d)
l.append(e)


print(l)
print("---------------------------------------------")
print("6)")

# Exercise Question 6: write all file content into new file by skiping line 5 from following file

count = 0
with open("test.txt", "r") as fp:
    lines = fp.readlines()
    count = len(lines)
with open("newFile.txt", "w") as fp:
    for line in lines:
        if count == 3:
            count -= 1
            continue
        else:
            fp.write(line)
        count -= 1

print("---------------------------------------------")
print("7)")

# Exercise Question 7: Accept any three string from one input() call

for i in range(10):
    try:
        str1, str2, str3 = input("Type 3 words: ").split()
        print(str1, str2, str3)
    except Exception as e:
        continue
    else:
        break

print("---------------------------------------------")
print("8)")

# Exercise Question 8: You have the following data.

quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))

print("---------------------------------------------")
print("9)")

# Exercise Question 9: How to check file is empty or not


print(os.stat("test.txt").st_size == 0)
print("---------------------------------------------")
print("10)")

# Exercise Question 10: Read line number 4 from the following file

with open("test.txt", "r") as fp:
    lines = fp.readlines()
    print(lines[3])

print("---------------------------------------------")

