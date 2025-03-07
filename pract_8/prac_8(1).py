class AgeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


age = int(input("Enter your age: "))
try:
    if age < 18:
        raise AgeException("You are not eligible to vote")
    else:
        print("You are eligible to vote")
except AgeException as e:
    print(e)

