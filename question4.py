list = []
n = int(input("Enter the number of elements of the list: "))
print("Enter the value of list")
for i in range (0,n):
	element=input()
	list.append(element)
temp=list[0]
list[0]=list[-1]
list[-1]=temp
print(list)
