def dotProduct(v1,v2):
    y1=len(v1)
    y2=len(v2)
    if y1 != y2:
        print("el tamaño de lso vesctores es diferente")
    else:

        x=0
        for i in range (len(v1)):
            x=x+(v1[i]*v2[i])

        return x
v=[1,2,3,5]
V=[2,4,5,6]
x=dotProduct(v,V)
print(x)
