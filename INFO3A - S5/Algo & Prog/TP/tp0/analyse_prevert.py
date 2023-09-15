import string


def clean_prevert(file: string):
    data: str
    data_clean: str = ''

    with open(file, 'r') as infile:  # ouverture du fichier (mode r: read)
        data = infile.read()  # lecture du contenu du fichier

    for i in data:

        if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
            data_clean += i

    data_clean = data_clean.lower()
    return data_clean


def analyse_prevert():
    alphabet = list(string.ascii_lowercase)
    text = clean_prevert('gutenberg.txt')
    dict_frequence = {}

    for lettre in alphabet:
        frequence = 0
        for c in text:
            if c == lettre:
                frequence += 1
        res = (frequence / len(text)) * 100
        dict_frequence[lettre] = round(res, 1)

    sorted_dict_frequence = sorted(dict_frequence.items(), key=lambda x: x[1])

    return sorted_dict_frequence


print(analyse_prevert())
