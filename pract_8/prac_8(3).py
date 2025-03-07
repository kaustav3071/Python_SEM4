# Write a program to convert a string to an integer and handle a ValueError if the string
# is not a valid number. Display a user-friendly error message and prompt the user to
# enter a valid number.

while True:
    try:
        user_input = input("Enter a number: ")
        number = int(user_input)
        print("The number is", number)
        break
    except ValueError as e:
        print("Exception is : ", e)