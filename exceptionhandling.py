try:
    print(number)
except:
    print("Please declare your variable first")

num1 = 39
num2 = 0
try:
    print(num1/num2)
except ZeroDivisionError:
    print("Please you cant devide number by zero")
finally:
    print("Success")