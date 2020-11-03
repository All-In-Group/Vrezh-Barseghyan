print("1)")

# Exercise Question 1: Print First 10 natural numbers using while loop
i = 0
while i<= 10:
    print(i)
    i+=1

print("---------------------------------------------")
print("2)")

# Exercise Question 2: Print the following pattern

for r in range(1,6):
    for c in range(1,r+1):
        print(c,end = " ")
    print()

print("---------------------------------------------")
print("3)")

# Exercise Question 3: Accept number from user and calculate the sum of all number between 1 and given number

s = 0
a = int(input("Enter a number: "))

for i in range(1, a+1, 1):
    s += i

print(s)

print("---------------------------------------------")
print("4)")

# Exercise Question 4: Print multiplication table of given number

n = 2
for i in range(1, 11):
    product = n*i
    print(product)

print("---------------------------------------------")
print("5)")

# Exercise Question 5: Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for i in list1:
    if i > 150:
        break
    if i % 5 ==0:
        print(i)

print("---------------------------------------------")
print("6)")

# Exercise Question 6: Given a number count the total number of digits in a number

n = 75869
print(len(str(n)))

print("---------------------------------------------")
print("7)")

# Exercise Question 7: Print the following pattern using for loop

def pattern(n):
    for i in range(0,n+1):
        for j in range(n-i,0,-1):
            print(j,end=' ')
        print()

pattern(5)

print("---------------------------------------------")
print("8)")

# Exercise Question 8: Reverse the following list using for loop

list1 = [10, 20, 30, 40, 50]

for i in list1[::-1]:
    print(i)

print("---------------------------------------------")
print("9)")

# Exercise Question 9: Display -10 to -1 using for loop

for n in range(-10, 0, 1):
    print(n)

print("---------------------------------------------")
print("10)")

# Exercise Question 10: Display a message “Done” after successful execution of for loop

for i in range(5):
    print(i)
print("Done!")

print("---------------------------------------------")
print("11)")

# Exercise Question 11: Python program to display all the prime numbers within a range

def func(start,end):
    print("Prime numbers between", start, "and", end, "are:")

    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

func(25, 50)

print("---------------------------------------------")
print("12)")

# Exercise Question 12: Display Fibonacci series up to 10 terms

nterms = 10

n1, n2 = 0, 1
count = 0

if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

print("---------------------------------------------")
print("13)")

# Exercise Question 13: Write a loop to find the factorial of any number

def fact(n):
    answer = 1
    for i in range(1,n+1):
        answer *= i
    print(answer)

fact(5)

print("---------------------------------------------")
print("14)")

# Exercise Question 14: Reverse a given integer number

def rev(number):
    while (number > 0):
        digit = number % 10
        number = number // 10
        print(digit, end="")

rev(76542)

print("---------------------------------------------")
print("15)")

# Exercise Question 15: Use a loop to display elements from a given list which are present at even positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in my_list[1::2]:
    print(i, end=" ")

print("---------------------------------------------")
print("16)")

# Exercise Question 16: Display the cube of the number up to a given integer

input_number = 6
for i in range(1, input_number + 1):
    print("Current Number is :", i, " and the cube is", (i **3))

print("---------------------------------------------")
print("17)")

# Exercise Question 17: Find the sum of the series 2 +22 + 222 + 2222 + .. n terms

number_of_terms = 5
a1 = 2
sum = 2
for i in range(0, number_of_terms):
    print(a1, end=" ")
    sum += a1
    a1 = (a1 * 10) + 2

print("---------------------------------------------")
print("18)")

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")

print("---------------------------------------------")