class Person:
    #properties/Variables/Attributes/Characterisitces
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    #Behaviour/Method/Function
    def study(self):
        print("Student studying")
#Create an object
student1 = Person(name:"Hussein",age:23,gender:"Male")
print(student1.name,student1.age,student1.gender)

