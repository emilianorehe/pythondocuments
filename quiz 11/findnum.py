import statistics
def readnum():
    fint=[]
    f = open('random_numbers.txt','r')
    lines = 0;
    total = 0;
    for line in f:
        total = total + int(line)
        lines += 1
        fint.append(int(line))
    a=statistics.stdev(fint)
    average = total/lines
    print("el promedio es ", average)
    print("el total es", total)
    print("There are",lines,"values.")
    print("la desviasion estandar es",a)
readnum()
