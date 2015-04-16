num=int(input("dame un numero "))

def fibo(num):
  if (num==0):
    return 0
  elif (num==1):
    return 1
  else: return fibo(num-1)+fibo(num-2)

a=fibo(num)
print("el fibonaci es ", a)
