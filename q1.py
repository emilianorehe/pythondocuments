def triangles(size):
	for r in range(1,size+1):
		for c in range(1,r+1):
			print("T", end="")
		print()
	for r in range(size-1,0,-1):
		for c in range(1,r+1):
			print("T",end="")
		print()
size=int(input("dame un numero que quieres que te imprima el archivo en T y que queiras en el medio: "))
t=triangles(size)
