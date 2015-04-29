def check_banana():
    txt=open("banana.txt",'r')
    cantidad=0
    for i in txt:
        r=i.lower()
        sub=r.find('banana')
        while sub !=-1:
            cantidad=cantidad+1
            sub=r.find('banana',(sub+1))
    return(cantidad)
    close("banana.txt")
ba=check_banana()
print("las veces que se encentra la palbra banan es ",ba)
