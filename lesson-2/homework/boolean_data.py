#1
username = input("Enter a username: ")
password = input("Enter a password: ")
if username and password:
    print("Successful.")
else:
    print("It is incorrect")

#2
a, b = map(float, input("Enter two numbers: ").split())

if a == b:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

#3
n = int(input("Enter a number: "))
if n > 0 and n % 2 == 0:
   print("The number is positive and even.")
else:
   print("The number is positive and odd.")

#4
a, b, c = map(float, input("Enter three numbers separated by space: ").split())
if a != b and b != c and a != c:
    print("All numbers are different.")
else:
    print("Some numbers are the same.")

#5
str1, str2 = input("Enter two strings separated by space: ").split()

if len(str1) == len(str2):
    print("The strings have the same length.")
else:
    print("The strings have different lengths.")

#6
num = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")

#7
num1, num2 = map(float, input("Enter two numbers separated by space: ").split())

if num1 + num2 > 50.8:
    print("The sum is greater than 50.8.")
else:
    print("The sum is not greater than 50.8.")