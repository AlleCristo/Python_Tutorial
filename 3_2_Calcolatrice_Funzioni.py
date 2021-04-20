import math

def addizione(x, y):
    tot = x + y
    return(tot)

def sottrazione(x, y):
    tot = x - y
    return(tot)

def moltiplicazione(x, y):
    tot = x * y
    return(tot)

def divisione(x, y):
    tot = x / y
    return(tot)

def potenza(x, y):
    tot = x ** y
    return(tot)

def radice(x):
    tot = math.sqrt(x
                    )
    return(tot)


while True:
    
    print('''
___________________________________________________________________________
                                                                          |
            Programma Calcolatrice in Python                              |
                                                                          |
            Selezionare l'operazione tra quelle sotto riportate:          |
                                                                          |
            - Addizione          PREMERE [1]                              |
            - Sottrazione        PREMERE [2]                              |
            - Moltiplicazione    PREMERE [3]                              |
            - Divisione          PREMERE [4]                              |
            - Potenza            PREMERE [5]                              |
            - Radice             PREMERE [6]                              |
                                                                          |
            -USCIRE              PREMERE [0]                              |
                                                                          |
__________________________________________________________________________|
            

    ''')

    dec = int(input('Quale operazione si desidera effettuare: '))
    tot = 0
    
    if dec == 1:
        print("Hai scelto: ADDIZIONE\n")
        
        x = int(input("Primo valore: "))
        y = int(input("Secondo valore: "))

        tot = addizione(x, y)

    elif dec == 2:
        print("Hai scelto: SOTTRAZIONE\n")
                
        x = int(input("Primo valore: "))
        y = int(input("Secondo valore: "))

        tot = sottrazione(x, y)

    elif dec == 3:
        print("Hai scelto: MOLTIPLICAZIONE\n")
        
        x = int(input("Primo valore: "))
        y = int(input("Secondo valore: "))

        tot = moltiplicazione(x, y)

    elif dec == 4:
        print("Hai scelto: DIVISIONE\n")
        
        x = int(input("Primo valore: "))
        y = int(input("Secondo valore: "))

        tot = divisione(x, y)

    elif dec == 5:
        print("Hai scelto: POTENZA\n")
        
        x = int(input("Base: "))
        y = int(input("Esponente: "))

        tot = potenza(x, y)

    elif dec == 6:
        print("Hai scelto: RADICE\n")
        
        x = int(input("Valore: "))

        tot = radice(x)

    else:
        print('''

    #######################################################################################
    
                                       EXIT PROGRAM

    #######################################################################################

    ''')
        break


    print("\nIl risultato è: " + str(tot))

    input("\n\nPREMERE UN QUALSIASI TASTO PER CONTINUARE")


        
