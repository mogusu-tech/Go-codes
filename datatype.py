number = 67 #integer
second = 45.98 #Float
greeting = "Hello there" #String
isPythonInteresting = True #Boolean

#Data Structures - Multiple values stored in a single variable
cars = ["toyota","nissan","vw","Audi"]#List - Ordered and changeable
fruits = ("apple","mango","banana") #This is a tuple - Ordered but They are unchangeable
countries = {"Kenya","Tunisia","Algeria"} #Set Elements are Unordered and unchangeable
student = {
    "first_name":"Jane",
    "age":25,
    "course":"Web development",
    "gender":"Female"
}# This is a dictionary key-value pair

print(number)
print(second)
print(greeting)
print(isPythonInteresting)
print(cars)
print(fruits)
print(countries)
print(student)
print(student["gender"])

#Determining a DataType
print(type(countries))
print(type(student))

#Typecasting - Converting from one data type to another
print(float(number))
print(int(second))