
text: str = 'Bonjour'
word: str = 'le monde'
if text == 'Bonjour':
    word = '0o7'  # chiffre 0 (zéro), lettre 'o' et chiffre 7 (sept)
text += ' ' + word
print(text)

print(f'Dissection de la chaîne de caractères {repr(text)} :')
for i, c in enumerate(text):
    print(i, c)


