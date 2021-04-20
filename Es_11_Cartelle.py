import os
import shutil

x = os.getcwd()                                     # restituisce il percorso di lavoro

print("\n\nStiamo lavorando in: \n" + x, end = "\n\n")


x = os.listdir()                                     # restituisce una lista contenente nomi completi di file e cartelle contenuti nella cartella di lavoro corrente se non specificato

print("\n\nLa cartella in cui stai lavorando contiene:")
for i in x:
    print(i)
    

x = os.chdir("C:\\Users\\usr\\Desktop\\Scuola\\Superiori\\Informatica\\Python\\File_Per_Es") 
                                                     # modifica il percorso di lavoro    
x = os.getcwd()

print("\n\nStiamo lavorando in: \n" + x, end = "\n\n")


os.makedirs("Esercizio_Con_Cartelle")               # crea una cartella nel percorso corrente

x = os.listdir()    

print("\n\nLa cartella in cui stai lavorando contiene:")
for i in x:
    print(i)


os.rename("Esercizio_Con_Cartelle", "Esercizio_Con_Cartelle_Rinominata")     # rinomina una cartella nel percorso corrente se non specificato

x = os.listdir()

print("\n\nLa cartella in cui stai lavorando contiene:")
for i in x:
    print(i)


shutil.move("C:\\Users\\usr\\Desktop\\Scuola\\Superiori\\Informatica\\Python\\File_Per_Es\\Esercizio_Con_Cartelle_Rinominata", "C:\\Users\\usr\\Desktop")
                    # sposta la cartella dal primo percorso al secondo con tutti i file interni ad essa

x = os.listdir()

print("\n\nLa cartella in cui stai lavorando contiene:")
for i in x:
    print(i)


x = shutil.copytree("C:\\Users\\usr\\Desktop\\Scuola\\Superiori\\Informatica\\Python\\File_Per_Es", "C:\\Users\\usr\\Desktop\\lezione_21" )
                    # copia la cartella del primo percorso al secondo con tutti i file interni ad essa
                    
print("\n\nCartella copiatacon relativi file in: \n" + x, end = "\n\n")

    
shutil.rmtree("C:\\Users\\usr\\Desktop\\lezione_21")
                    # elimina la cartella con tutti i file interni ad essa
                    
print("\n\nCartella eliminata ", end = "\n\n")



































