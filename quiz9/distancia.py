import math
def distancia():
	if (x1>x2):
		x3=x1-x2
	else:
		x3=x2-x1
	if(y1>y2):
		y3=y1-y2
	else:
		y3=y2-y1
	c=math.sqrt(x3**2+y3**2)
	return c
x1=int(input("dame el valor de x1: "))
x2=int(input("dame el valor de x2: "))
y1=int(input("dame el valor de y1: "))
y2=int(input("dame el valor de y2: "))
a=distancia()
print("la distancias es ", a)
