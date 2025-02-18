#1
num = float(input("Enter the number:"))
print(f"{num:.2f}")

#2
num1 = float(input())
num2 = float(input())
num3 = float(input())

print(max(num1, num2, num3))
print(min(num1, num2, num3))

#3
km = float(input("Enter kilometrs"))
print(f"Meters: {km * 1000}, Cantimeters: {km * 10000} ")

#4
a, b = map(int, input("Enter two numbers: ").split())
print(f"Quotient: {a // b}, Remainder: {a % b}")

#5
c = float(input("Enter Celsius temperature"))
print(f"Fahrenheit: {c * 9/5 + 32}")

#6
n = int(input("Enter a number: "))
print("Last digit:", abs(n) % 10)

#7
n = int(input("Enter a number: "))
print("Even" if n % 2 == 0 else "Odd")