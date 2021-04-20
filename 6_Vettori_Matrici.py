
#Lista Singola

elenco = []

elenco = [2, 5, 3.14, 6, "ciao"]

el1 = elenco[2:]                #el1 contiene [3.14, 6, "ciao"] ovvero gli elementi da indice 2 alla fine di elenco
el2 = elenco[:2]                #el2 contiene [2, 5, 3.14] ovvero gli elementi da inizio a indice 2 (escluso) di elenco
el3 = elenco[1:3]               #el3 contiene [5, 3.14, 6] ovvero gli elementi da indice 1 a 3 (escluso) di elenco

elRange = list(range(0, 11))    #elRange contiene tutti i numeri tra 0 e 11 (escluso)

elenco[0] = 11

elenco[-1] = "CIAO"             #Come scrivere elenco[3], possibile anche -2, -3, ...

print("\n\n")
print(elenco[0])                #Stampa il contenuto di elenco in indice 0
print(elRange)                  #Stampa l'intera lista compresa di parentesi e virgole
      
del elenco[3]                   #Elimina l'elemento 3 dalla lista e scala il resto degli indici

print("\n\n")

for i in elenco:                #Vettori con for (foreach)
    print(i)


print("\n\n")

for i in range(len(elenco)):                #Vettori con for (indici) len(elenco) = lunghezza elenco
    print(elenco[i])

#Liste & Stringhe ***********************************************************************************************************
    
print("\n\n")

frase = "ALESSIO"
listaStr = list(frase)          #Trasforma una stringa in una lista contenente come valori i caratteri della stringa

print(listaStr)

print(frase[0])                 #E' possibile trattare la stringa come un array di char

#Lista Multipla ************************************************************************************************************

matrice = []
matrice = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]         # Più chiaro così:
                                                    # matrice = [
                                                    #            [0, 1, 2],
                                                    #            [3, 4, 5], 
                                                    #            [6, 7, 8]
                                                    #           ]


for i in matrice:                           #Vettori con for (foreach)
    print("\n")
    for j in i:
        print(str(j), end = " ")            #end = " " imposta come terminatore uno spazio, di default è "\n"
    



#Tuple --> Sono vettori NON MODIFICABILI una volta instanziati e valorizzati *************************************


tupla = (3, 6, 9, 12)

tupla2 = 2, 4, 6, 8


#   tupla[0] = 33   NON POSSIBILE PERCHE' NON MODIFICABILE

#   del tupla[1]    NON POSSIBILE PERCHE' NON MODIFICABILE


print("\n\n")

print(tupla2)

print("\n")

for i in range(len(tupla)):
    print(tupla[i], end = " ") 



#ALCUNI METODI PER LE LISTE (sia singole che multiple) *************************************************************

print("\n\n")

inv = ["Torcia", "Spada", "Arco", 1]


inv.append("Frecce")                #Aggiunge elemento alla fine della lista
print(inv, end = "\n\n")


inv.insert(2, "Piccone")            #Aggiunge elemento all' indice specificato
print(inv, end = "\n\n")


inv.remove("Torcia")                #Elimina elemento specificato
print(inv, end = "\n\n")


inv.pop(-2)                         #Elimina elemento all' indice specificato
print(inv, end = "\n\n")


inv.pop()                           #Elimina ultimo elemento 
print(inv, end = "\n\n")


inv.sort()                          #Ordina gli elementi all' interno della lista sia numerica che alfabetica in modo crescente
print(inv, end = "\n\n")


inv.sort(reverse = True)            #Ordina gli elementi all' interno della lista sia numerica che alfabetica in modo decrescente
print(inv, end = "\n\n")


x = inv.index("Piccone")             #Restituisce l' indice in cui è presente l'elemento specificato (Se non trovato da ValueError)
print(x, end = "\n\n")


inv.clear()
print(inv, end = "\n\n")             #Rimuove tutti gli elementi dalla lista







































