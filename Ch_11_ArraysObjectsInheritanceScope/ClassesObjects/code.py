# Classes and Objects
class MyClass:
    x = 5

print(MyClass)

p1 = MyClass()
print(p1.x)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(p1)

class Person2:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def __str__(self):
        return f"{self.name}({self.age})"

p2 = Person2("William", 37)
print(p2)


class Person3:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 

    def myfunc(self):
        print("Hello my name is " + self.name)

p3 = Person3("Mike", 37)
p3.myfunc()

# Modify the Object
p3.age = 40
print(p3.age)

# Delete Obj Properties
del p3.age
print(p3.age)

# Delete Objects
del p3
print(p3)


