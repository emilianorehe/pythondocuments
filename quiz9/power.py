a=int(input("dame un numero: "))
b=int(input("potencia que quieres que sea elevada "))

def potencia():
  x=1
  y=a
  while(x<b):
    y=y*a
    x=x+1
  return y

p=potencia()
print("la respuesta es", p)
