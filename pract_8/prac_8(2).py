# Write a program to access an element in a list and handle an IndexError if the index
# is out of range. Display a user-friendly error message and prompt the user to enter a
# valid index.

list1 = [1,2,3,4,5]
while True:
    try:
        idx = int(input(f"Enter the index from 0 to {len(list1)-1}: "))
        print("Element at index", idx, "is", list1[idx])
        break
    except IndexError as e:
        print("Exception is : ", e)
    except ValueError as e:
        print("Exception is : ", e)