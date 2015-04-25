def findthrees(nu):
    s=0
    for i in nu:
        x=i%3
        if x == 0:
            s=s+i
    return s
nu=[0,4,2,6,9,8,3,12]
x=findthrees(nu)
print(x)
