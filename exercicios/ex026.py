frase = str(input('Digite alguma coisa: '))

fraseMin = frase.lower()

print(f"""Na frase {frase}:
A letra "A/a" aparece: {fraseMin.count('a')} vezes;
A primeira vez que a letra "A/a" aperece é na posição: {fraseMin.find('a') + 1};
A última vez que a letra "A/a" aperece é na posição: {fraseMin.rfind('a') + 1}.""")
