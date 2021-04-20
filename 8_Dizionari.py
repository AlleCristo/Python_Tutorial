
diz = {}

diz = {"nome":"Alessio", "cognome":"Cristofaro", "ortaggio":"Cipolle", "eta":18, "voti":[10, 8, 9, 7]}

print(diz, end = "\n\n")


x = diz["nome"]                         #Recupera valore   

print(x, end = "\n\n")


diz["Aggiunta"] = "Nuovo_Valore"        #Aggiunta nuovo elemento, diz[chiave] = valore

print(diz, end = "\n\n")


del diz["ortaggio"]                     #Elimina elemento per chiave

print(diz, end = "\n\n")


diz["eta"] = 19                          #Modifica valore

print(diz, end = "\n\n")


x = "eta" in diz                        #Cerca se è presente la chiave specificata nel dizionario

print(x, end = "\n\n")


x = "Alessio" in diz                    #Cerca se è presente il valore specificata nel dizionario

print(x, end = "\n\n")


x = diz.keys()                          #Restituisce tutte le chiavi presenti nel dizionario  (l'oggetto restituito è di tipo dict_keys)     

print(x, end = "\n\n")


x = diz.values()                         #Restituisce tutti i valori presenti nel dizionario   (l'oggetto restituito è di tipo dict_values) 

print(x, end = "\n\n")


x = diz.items()                          #Restituisce tutte le coppie chiave:valore presenti nel dizionario   (l'oggetto restituito è di tipo dict_items) 

print(x, end = "\n\n")


x = list(diz.keys())                    #Restituisce tutte le chiavi presenti nel dizionario in una LISTA

print(x, end = "\n\n")


x = list(diz.values())                  #Restituisce tutti i valori presenti nel dizionario in una LISTA

print(x, end = "\n\n")


x = list(diz.items())                  #Restituisce tutte le coppie chiave:valore presenti nel dizionario in una LISTA sotto forma di matrice

print(x, end = "\n\n")



for i in diz:                           #Stampa tutte le chiavi del dizionario
    print(i)

print(end = "\n\n")


for i in diz.values():                  #Stampa tutti i valori del dizionario
    print(i)

print(end = "\n\n")


for i in diz.items():                   #stampa tutte le coppie chiave:valore sotto forma di array
    print(i)

print(end = "\n\n")


x = diz.get("birra", "Non trovato")     #restutuisce il valore associato alla chiave specificata, se non lo trova restituisce cio che viene specificato dopo la virgola
                                                                                
print(x, end = "\n\n")


diz.setdefault("altezza", "1.88")       #cerca la chiave nel dizionario, SOLO SE NON é PRESENTE la aggiunge con il valore specificato di seguito

print(diz, end = "\n\n")











