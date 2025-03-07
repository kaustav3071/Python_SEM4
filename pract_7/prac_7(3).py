
filename = "sample.txt"

with open(filename, "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("This file contains sample text.\n")
    file.write("Python file handling is easy!\n")

print("File written successfully!")

with open(filename, "r") as file:
    content = file.read()


print("\nReading from the file:")
print(content)
