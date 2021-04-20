
# Roba per creare automaticamente i file con cui poi lavoreremo

import os

os.chdir("C:\\Users\\usr\\Desktop\\Scuola\\Superiori\\Informatica\\Python\\File_Per_Es\\")

f = open("File1.txt", "w")
f.close()

f = open("File2.txt", "w")
f.close()

f = open("File3.txt", "w")
f.close()

f = open("File4.txt", "w")
f.close()

# TUTORIAL DA QUA IN GIU -----------------------------------------------------------------------------------------------------------------------------


import shutil   # Copiare, Spostare, Eliminare Files

x = shutil.copy("C:\\Users\\usr\\Desktop\\Scuola\\Superiori\\Informatica\\Python\\File_Per_Es\\File1.txt", "C:\\Users\\usr\\Desktop")
                    # copia il file del primo indirizzo nel secondo indirizzo e restituisce il nuovo percorso

print("Il file è stato copiato in:\n" + x, end = "\n\n")



x = shutil.move("C:\\Users\\usr\\Desktop\\Scuola\\Superiori\\Informatica\\Python\\File_Per_Es\\File2.txt", "C:\\Users\\usr\\Desktop")
                    # sposta il file del primo indirizzo nel secondo indirizzo e restituisce il percorso del file
               
print("Il file è stato spostato in:\n" + x, end = "\n\n")


import os       # Cancellare, Rinominare Files


x = os.remove("C:\\Users\\usr\\Desktop\\Scuola\\Superiori\\Informatica\\Python\\File_Per_Es\\File3.txt")
                    # elimina il file specificato nel percorso

print("Il file è stato eliminato \n", end = "\n\n")



x = os.rename("C:\\Users\\usr\\Desktop\\Scuola\\Superiori\\Informatica\\Python\\File_Per_Es\\File4.txt", "C:\\Users\\usr\\Desktop\\Scuola\\Superiori\\Informatica\\Python\\File_Per_Es\\File4_Nuovo.txt")
                    # elimina il file specificato nel percorso

print("Il file è stato rinominato \n", end = "\n\n")
