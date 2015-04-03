x=int(input("dame la altura del rectangulo: "))
y=int(input("dame la base del rectangulo: "))
z=int(input("dame el area del rectangulo: "))
if x<0:
    print ("debe de ser numero positivo: ")
    x=int (input("dame otro numero"))
if y<0:
    print ("debe de ser numero positivo: ")
    y=int (input("dame otro numero"))
else:
    ra=(x+y)/2
    a=z/ra
    ra=(ra+a)/2
    ra=z/ra
print (ra)
