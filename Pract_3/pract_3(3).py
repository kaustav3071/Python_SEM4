def MAX(list):
    return max(list)
def MIN(list):
    return min(list)
def SUM(list):
    return sum(list)
def AVERAGE(list):
    return sum(list)/len(list)

length=int(input("Enter the length of list: "))
list=[]
for i in range(length):
    list.append(int(input(f"Enter the element {i+1}: ")))

print("Maximum element of list is: ",MAX(list))
print("Minimum element of list is: ",MIN(list))
print("Sum of list is: ",SUM(list))
print("Average of list is: ",AVERAGE(list))