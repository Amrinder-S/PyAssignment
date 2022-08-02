str = input("Enter a string: ")
c = 0
if (str==str[::-1]):
	print("String is palindrome")
	c = c + 1
elif(str[ :len(str)//2]==str[len(str)//2: ]):
	print("String is symmetrical")
elif(c==0):
	print("String is neither palindrome nor symmetrical")
