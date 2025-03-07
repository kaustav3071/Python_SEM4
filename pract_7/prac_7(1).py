with open("basic.txt","w") as file:
    file.write("Hello My Name is Kaustav Das")

file.close()

with open("basic.txt","r") as file1:
    content = file1.read()
    print("The Content of the file is : ",content)