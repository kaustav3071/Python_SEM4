from package_6_3 import *

choice = int(input("Enter the operation you want to perform:"
               "\n1.Area Calculation"
               "\n2.Prime Number Checker"
                   "\nEnter the choice : "))

if choice == 1:
    shape_choice=int(input("Enter the shape of the shape:"
                           "\n1.Circle"
                           "\n2.Rectangle"
                           "\n3.Triangle"
                           "\nEnter the shape number : "))

    if shape_choice == 1:
        shape="Circle"
    elif shape_choice == 2:
        shape="Rectangle"
    elif shape_choice == 3:
        shape="Triangle"
    print(f"The shape of the shape is {shape} and its area is {calculate_area(shape_choice)}")

elif choice == 2:
    number = int(input("Enter the number to check:"))
    if (prime(number)):
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} is not prime")

