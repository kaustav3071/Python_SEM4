def even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def operation(opr, num1, num2):
    if opr == 1:  # addition
        return num1 + num2
    elif opr == 2:  # substraction
        return (num1 - num2)
    elif opr == 3:
        return num1 * num2
    elif opr == 4:
        return num1 / num2
    else:
        return "Invalid number you select"