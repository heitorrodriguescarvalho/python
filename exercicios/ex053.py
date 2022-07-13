from unidecode import unidecode

print('-=-' * 15, '\033[31mAnalizando se a Frase é um Palíndromo\033[m', '-=-' * 15)

# O módulo unidecode retira a acentuação da frase.
frase = unidecode(str(input('Digite uma \033[33mfrase\033[0m: '))).lower().replace(' ', '')
fraseLength = len(frase)
fraseReverseList = []

for c in range(0, fraseLength):
    fraseReverseList.append(frase[fraseLength - c - 1])

fraseReverse = "".join(fraseReverseList)

if fraseReverse == frase:
    print('A frase \033[34mé um palíndromo\033[0m. ')

else:
    print('A frase \033[31mnão é um palíndromo\033[0m.')
