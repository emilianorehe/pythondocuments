def find_threes (list):
	sum=0
	for x in range(0,len(list)):
		if(list[x]%3==0):
			sum+=list[x]
	return (sum)
a=int(input("dame un numero"))
b=int(input("dame un numero"))
c=int(input("dame un numero"))
d=int(input("dame un numero"))
e=int(input("dame un numero"))
f=int(input("dame un numero"))
g=int(input("dame un numero"))
h=int(input("dame un numero"))

list=[a,b,c,d,e,f,g,h]

print(list)

print("la suma de los numeros divisilbes entre 3 que estan en la lista es:",find_threes(list))
