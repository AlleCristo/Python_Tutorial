eta = 19
patente = True

if eta >= 18 and patente:
    print("Sei maggiorenne")
    print("\nPuoi noleggiare una ferrari")
    
elif eta >= 18 and not patente:
    print("Sei maggiorenne")
    print("\nNiente patente niente ferrari")
        
else:
    print("NON sei maggiorenne")
