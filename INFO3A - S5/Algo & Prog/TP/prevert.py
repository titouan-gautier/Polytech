def sort_prevert() :
    data: str
    with open('data_inventaire_prevert.txt', 'r') as infile: # ouverture du fichier (mode r: read)
        data = infile.read() # lecture du contenu du fichier
    data = data.replace(";","\n")
    data = data.split("\n")

    count = 1
    new_data : str = ""
    for i in data :
        if count < 10 :
            i = "0" + str(count) + ". " + i
        else : 
            i = str(count) + ". " + i
        new_data += i + "\n"
        count += 1

    print(new_data)

sort_prevert()