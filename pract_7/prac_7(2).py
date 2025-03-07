number=int(input("Enter the number upto you want to insert : "))

file_odd = open("odd_numbers.txt","w")
file_even = open("even_numbers.txt","w")
for i in range(number):
    if i % 2 == 0:
        file_odd.write(str(i) + "\n")
    else:
        file_even.write(str(i) + "\n")

print("All numbers inserted successfully")
