def print_3_volte():
    print("Ciao")
    print("Ciao")
    print("Ciao\n\n")

def somma(a, b):
    tot = a+b
    print(tot)

def somma2(a, b = 3):
    tot = a+b
    return(tot)
    

x = int(input("Numero: "))
y = int(input("Numero: "))

print_3_volte()
tot = somma2(x, y)

print(tot)
