def fact(n):
	n=n
	a=1
	while (n>1):
		a=a*n
		n=n-1
	return (a)

x="y"
while(x=="y"):
	n=int(input("Dame un numero"))
	f=fact(n)
	while (n<0):
		n=int(input("error dame un numero positivo"))
		f=fact(n)
	print("El factorial de tu numero es:",f)
	x=int(input("Quieres intentar otro numero? 1=si, 2=no:"))
	while (x!=1 and x!=2):
		print ("Error")
		x=int(input("Quieres intentar otro numero? 1=si, 2=no:"))
