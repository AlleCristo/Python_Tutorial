# TROVA:
# MAX, MIN, MED (TOTALR)
# MAX, MIN, MED (X RIGA)
# MAX, MIN, MED (X COLONNA)
import random       #random.randint(0,10)

def fill():
    m = []
    
    for i in range(5):
        x = []
        
        for j in range(5):
            x.append(random.randint(0, 101))
            
        m.append(x)
       
    return(m)

def show(m):
    print("\n\n")

    for i in m:
        for j in i:
            print(j, end = " ")
        print("")
    print("\n\n")

def find_max(m):
    maxim = m[0][0]

    for i in m:
        for j in i:
            if j > maxim:
                maxim = j
                
    return maxim

def find_min(m):
    minim = m[0][0]

    for i in m:
        for j in i:
            if j < minim:
                minim = j

    return(minim)

def find_med(m):
    tot = 0

    for i in m:
        for j in i:
            tot += j

    med = tot/(len(m)*len(m[0]))
    
    return(med)

def find_max_vet(v):
    maxim = v[0]

    for i in v:
        if i > maxim:
            maxim = i

    return(maxim)

def find_min_vet(v):
    minim = v[0]

    for i in v:
        if i < minim:
            minim = i

    return(minim)

def find_med_vet(v):
    tot = 0

    for i in v:
        tot += i

    med = tot/len(v)

    return(med)

def find_max_col(m, x):
    maxim = m[0][x]
    
    for i in range(len(m)):
        if m[i][x] > maxim:
            maxim = m[i][x]

    return(maxim)

def find_min_col(m, x):
    minim = m[0][x]
    
    for i in range(len(m)):
        if m[i][x] < minim:
            minim = m[i][x]

    return(minim)

def find_med_col(m, x):
    tot = 0
    
    for i in range(len(m)):
        tot += m[i][x]

    med = tot / len(m)
    
    return(med)
    
#------------------------------------------------------------

m = fill()

show(m)

print("Totale")
print("Il valore massimo è:" + str(find_max(m)))
print("Il valore minimo è:" + str(find_min(m)))
print("Il valore medio è:" + str(find_med(m)), end = "\n\n")


for i in range(len(m)):
    print("Riga " + str(i+1))
    print("Il valore massimo è:" + str(find_max_vet(m[i])))
    print("Il valore minimo è:" + str(find_min_vet(m[i])))
    print("Il valore medio è:" + str(find_med_vet(m[i])), end = "\n\n")


for i in range(len(m)):
    print("Colonna " + str(i+1))
    print("Il valore massimo è:" + str(find_max_col(m, i)))
    print("Il valore minimo è:" + str(find_min_col(m, i)))
    print("Il valore medio è:" + str(find_med_col(m, i)), end = "\n\n")















































