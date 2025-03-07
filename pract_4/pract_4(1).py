class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.grades=[]
    def average(self):
        return sum(self.grades)/len(self.grades)
    def display(self):
        print("Student Information")
        print("Student Name:", self.name)
        print("Student Age:", self.age)
        print("Average Grade:", self.average())
        print("Grades:")
        for k in self.grades:
            print(k,end=" ")
name=input("Enter Student name:")
age=int(input("Enter Student age:"))
s1 = Student(name,age)
n=int(input("Enter number of grades:"))
for i in range(n):
    grade=int(input(f"Enter grade {i+1}:"))
    s1.grades.append(grade)

s1.display()