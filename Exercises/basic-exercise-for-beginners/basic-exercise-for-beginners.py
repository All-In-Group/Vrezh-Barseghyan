print("1)")

# Question 1: Given a two integer numbers return their product and  if the product is greater than 1000, then return their sum

def question_one(x, y):
    sum = x * y
    if sum < 1000:
        return sum
    else:
        sum = x + y
        return sum

print(question_one(40,60))
print("---------------------------------------------")
print("2)")

# Question 2: Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number

def question_two(number):
    previous = 0
    for i in range(number):
        sum = previous + i
        print("Current Number", i, "Previous Number ", previous, " Sum: ", sum)
        previous = i

print(question_two(10))
print("---------------------------------------------")
print("3)")

# Question 3: Given a string, display only those characters which are present at an even index number.

def question_three(word):
    for i in word:
        if word.index(i) % 2 == 0:
            print(i)

question_three("exercise")
print("---------------------------------------------")
print("4)")

# Question 4: Given a string and an integer number n, remove characters from a string starting from zero up to n and return a new string

def question_four(remove, k):
    return remove[k:]

print(question_four("pynative", 4))
print("---------------------------------------------")
print("5)")

# Question 5: Given a list of numbers, return True if first and last number of a list is same

given = [10, 20, 30, 40, 10]

def question_five(given):
    if given[0] == given[-1]:
        return True
    else:
        return False

print(question_five(given))
print("---------------------------------------------")
print("6)")

# Question 6: Given a list of numbers, Iterate it and print only those numbers which are divisible of 5

gl = [10, 20, 33, 46, 55]

def question_six(gl):
    for i in gl:
        if i % 5 == 0:
            print(i)

question_six(gl)
print("---------------------------------------------")
print("7)")

# Question 7: Return the total count of sub-string “Emma” appears in the given string


text = "Emma is good developer. Emma is a writer"
cnt = text.count("Emma")

print(cnt)
print("---------------------------------------------")
print("8)")

# Question 8: Print the following pattern

for _ in range(6):
    for i in range(_):
        print(_, end="")
    print("\n")

print("---------------------------------------------")
print("9)")

# Question 9: Reverse a given number and return true if it is the same as the original number
def question_nine(n):

    on = n
    rev = 0
    while (n > 0):
        a = n % 10
        rev = rev * 10 + a
        n = n // 10
    if on == rev:
        return True
    else:
        return False

print(question_nine(121))
print("---------------------------------------------")
print("10)")

# Question 10: Given a two list of numbers create a new list such that new list should contain only odd numbers from the first list and even numbers from the second list

f =[10, 20, 23, 11, 17]
s = [13, 43, 24, 36, 12]
t = []

def question_ten(f,s):
    for i in f:
        if i % 2  != 0:
            t.append(i)
    for i in s:
        if i % 2 ==0:
            t.append(i)
    return t

print(question_ten(f,s))
print("---------------------------------------------")
print("11)")

# Question 11: Write a code to extract each digit from an integer, in the reverse order


def question_eleven(number):
    while (number > 0):
        digit = number % 10
        number = number // 10
        print(digit, end=" ")

question_eleven(7536)
print()
print("---------------------------------------------")
print("12)")

# Question 12: Calculate income tax for the given income by adhering to the below rules

def question_twelve(income):
    taxPayable = 0
    if income <= 10000:
        taxPayable = 0
        print("no tax to pay")
    elif income <= 20000:
        taxPayable += (income - 10000) * 10 / 100
        print(f"tax {taxPayable}")
    else:
        taxPayable += 10000 * 10 / 100
        taxPayable += (income - 20000) * 20 / 100
        print((f"tax {taxPayable}"))

question_twelve(10000)
question_twelve(20000)
question_twelve(30000)
question_twelve(300000)
print("---------------------------------------------")
print("13)")

# Question 13: Print multiplication table form 1 to 10
def question_thirteen():
    for v in range(1, 11):
        for h in range(1, 11):
            print(v * h, end=" ")
        print("\t\t")

question_thirteen()
print("---------------------------------------------")
print("14)")

# Question 14: Print downward Half-Pyramid Pattern with Star (asterisk)

def question_fourteen():
    for i in range(6, 0, -1):
        for j in range(0, i - 1):
            print("*", end=' ')
        print(" ")

question_fourteen()
print("---------------------------------------------")
print("15)")

def question_fiftenn(a, b):
    answer = a ** b
    return f"The answer is {answer}"

print(question_fiftenn(4,4))