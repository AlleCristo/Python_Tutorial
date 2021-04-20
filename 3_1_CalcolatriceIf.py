while True:
    #print("Benvenuto al programma calcolatrice in Python\n")
    #print("Di seguito trovarai le funzioni possibili:\n\n")
    #print("\t-Addizione\t\tPREMERE [1]")
    #print("\t-Sottrazione\t\tPREMERE [2]")
    #print("\t-Moltiplicazione\tPREMERE [3]")
    #print("\t-Divisione\t\tPREMERE [4]")
    #print("\t-Potenza\t\tPREMERE [5]")
    #print("\nPer terminare il programma \tPREMERE [0]")

    print('''
    Benvenuto al programma calcolatrice in Python

    Di seguito trovarai le funzioni possibili:

    -Addizione            PREMERE [1]
    -Sottrazione          PREMERE [2]
    -Moltiplicazione      PREMERE [3]
    -Divisione            PREMERE [4]
    -Potenza              PREMERE [5]
    
    -USCITA               PREMERE [0]

    ''')

    dec = input("Inserisci il numero dell' operazione desiderata: ")
    dec = int(dec)
    
    if(dec == 1):
        print("\nHai scelto: Addizione\n")
        
        x = float(input("Inserire primo valore: "))
        y = float(input("Inserire Secondo valore: "))

        tot = x + y
        
    elif(dec == 2):
        print("\nHai scelto: Sottrazione\n")
        
        x = float(input("Inserire primo valore: "))
        y = float(input("Inserire Secondo valore: "))

        tot = x - y

    elif(dec == 3):
        print("\nHai scelto: Moltiplicazione\n")
        
        x = float(input("Inserire primo valore: "))
        y = float(input("Inserire Secondo valore: "))

        tot = x * y

    elif(dec == 4):
        print("\nHai scelto: Divisione\n")
        
        x = float(input("Inserire primo valore: "))
        y = float(input("Inserire Secondo valore: "))

        tot = x / y

    elif(dec == 5):
        print("\nHai scelto: Potenza\n")
        
        x = float(input("Inserire valore: "))
        y = float(input("Inserire esponente: "))

        tot = x ** y

    elif(dec == 0):
        break

    print("\nIl risultato è: " + str(tot))

    dec2 = input("Se desideri continuare PREMERE [1] altrimenti PREMERE un tasto ")
    
    if(dec2 != '1'):
        break
    else:
        print("\n\nSi torna al Menu!\n\n")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        













        
