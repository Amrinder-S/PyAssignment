list=[]
n = int(input("Enter the number of elements in the list: "))
for i in range(0,n):
	el=input()
	list.append(el)
a = int(input("Enter the position you want to swap: "))
b = int(input("Enter the position it is to be append with: "))
temp = list[a-1]
list[a-1] = list[b-1]
list[b-1]=temp
print(list)
