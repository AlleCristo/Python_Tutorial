# write = riscrive ogni volta il file azzerandolo           --> w
# append = aggiunge il testo inserito al file               --> a
# read = legge il testo del file                            --> r

import os               # NON necessaria per file

os.chdir("C:\\Users\\aless\\Desktop\\Scuola\\Superiori\\Informatica\\Python\\File_Per_Es")  




string = "Ciao sono Alessio Cristofaro"

file1 = open("esempioFile.txt", "w")                    # apre/crea il file esempioFile.txt nella cartella in cui si trova il file .py che lo genera

file1.write(string)                                     # azzera il file e aggiunge la stringa al file

file1.close()



file1 = open("esempioFile.txt", "a")                

file1.write(" ho 19 anni")                             # aggiunge la stringa al file sulla stessa linea        

file1.write("\nSta programmando in Python")            # aggiunge la stringa al file a capo

file1.close()



file1 = open("esempioFile.txt", "r")

contenutoFile = file1.read()                            # torna il contenuto del file in 1 stringa

print(contenutoFile, end = "\n\n")

file1.close()



file1 = open("esempioFile.txt", "r")

contenutoPerRiga = file1.readlines()                     # torna il contenuto del file in una lista, ogni linea in un indice differente

print(contenutoPerRiga, end = "\n\n")

file1.close()


# Capire dove salvare il file -----------------------------------------------------

import os

root = os.getcwd();                         # ottiene il percorso corrente

print(root, end = "\n\n")

os.chdir("C:\\Users\\aless\\Desktop")          # modifica il percorso corrente

root = os.getcwd();             

print(root, end = "\n\n")


# Effettuare queste operazioni relative al percorso prima di lavorare con i file per stabilirne la posizione (sia dove trovarlo che dove salvarlo)





















