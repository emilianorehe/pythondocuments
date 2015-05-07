def gcd(x,y):
    if(x==y):
        re=x
    elif(x>y):
        re=gcd((x-y),y)
    else:
        re=gcd(x,(y-x))
    return re

x=int(input("dame un numero "))
y=int(input("dame otro numero "))
z=gcd(x,y)
print("el comun divisor es ",z)
