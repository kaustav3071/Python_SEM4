class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,sid):
        super().__init__(name,age)
        self.sid=sid
    def display(self):
        print(f"Name:{self.name}\nAge:{self.age}\nID:{self.sid}")


name=input("Enter name:")
age=int(input("Enter age:"))
sid=int(input("Enter id:"))
s1=Student(name,age,sid)
s1.display()