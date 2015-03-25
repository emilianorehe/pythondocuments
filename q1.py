def triangles(size):
	for r in range(1,size+1):
		for c in range(1,r+1):
			print("t", end="")
		print()
	for r in range(size-1,0,-1):
		for c in range(1,r+1):
			print("t",end="")
		print()

print("This program makes a triangle using your number as the middle length")
size=int(input("Give me a number:"))
t=triangles(size)
