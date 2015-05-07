def calculate_e(n):
    a = n
    e = (1+1/a)**a
    return float(e)

x = int(input("el nuemmro decimal "))

num = calculate_e(x)

print("lo que se estimula de e es :",num)
