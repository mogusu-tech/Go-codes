class Animal:
    def move(self):
        print("Animal is walking.")

class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

cow = Animal()
dog = Dog()
dog.bark()
dog.move()