import csv

m = {"Alessio":[1,2,3], "Leonardo":[4, 5, 6], "Eleonora":[7, 8, 9]}

#Scrittura da Dizionario a CSV

with open(".\\File_Per_Es\\fileProva.csv", "w", newline = "") as csv_file_2:
    
    writer = csv.writer(csv_file_2, delimiter = ',')

    for people in m:
        v = []
        v.append(people)
        
        for value in m[people]:     

            v.append(value)

        writer.writerow(v)
            
                        
    

m2 = {}

#Lettura da CSV a Dizionario

with open(".\\File_Per_Es\\fileProva.csv", "r") as csv_file:
    
    reader = csv.reader(csv_file)

    #next(reader)                    #skippa la prima linea che potrebbe contenere l'intestazione

    for line in reader:
        
        vet = []
        key = ""
        
        for index in range(len(line)):
            
            if index == 0:
                key = str(line[index])
            else:
                vet.append(int(line[index]))

        m2[key] = vet

    
    print(m2)

    if m2 == m:
        print("yes")
                
    
