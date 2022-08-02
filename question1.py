a = input("Enter a string: ")
a = a.lower()
anew = a[0]+a[1:].replace(a[0],'$')
print(anew)
