x=int(input("dame un numero "))
y=int(input("dame otro numero "))
c=0
if (y<x):
  a=x
  b=y
  x=b
  y=a
while (x!=y):
  c=c+x
  x=x+1
c=c+y
print("el resultado del rango de los numero es: ",c)
