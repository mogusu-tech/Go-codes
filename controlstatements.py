temperature = int(input("Enter temperature in Celsius: "))
if temperature > 25:
    print("It is too hot")
else:
    print("It is too cold")

#A python program that checks three numbers and returns the smallest
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 < num2 and num1 <num3:
    print(num1,"is the smallest number")
elif num2 < num1 and num2 <num3:
    print(num2,"is the smallest number")
else:
    print(num3,"is the smallest number")

#Program to check whether a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")