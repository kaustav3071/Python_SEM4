from maths_func import *

choice = int(input("Enter your choice\n1:Even/Odd Check\n2:Operation\nEnter choice : "))
if choice == 1:
    number = int(input("Enter the number : "))
    if (even(number)):
        print("Even")
    else:
        print("Odd")
elif choice == 2:
    number1 = int(input("Enter the number 1 : "))
    number2 = int(input("Enter the number 2 : "))

    choice = int(input("Enter your choice"
                       "\n1: Add"
                       "\n2: Subtract"
                       "\n3: Multiply"
                       "\n4: Divide"
                       "\nEnter choice : "))
    if choice == 1:
        print("Answer is : ", operation(1,number1, number2))
    elif choice == 2:
        print("Answer is : ", operation(2,number1, number2))
    elif choice == 3:
        print("Answer is : ", operation(3,number1, number2))
    elif choice == 4:
        print("Answer is : ", operation(4,number1, number2))
    else:
        print("Invalid choice")