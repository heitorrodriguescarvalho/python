print('-=-' * 15, '\033[31mAnalizando se o Número é Primo\033[m', '-=-' * 15)

num = int(input('Digite um número: '))
numPrimo = True
numDivisor = []

for c in range(2, num):
    if num % c == 0:
        numPrimo = False
        numDivisor.append(c)

if numPrimo:
    print(f'O número \033[33m{num}\033[34m é primo\033[0m.')

else:
    numDivisorStr = []
    for c in range(0, len(numDivisor)):
        numDivisorStr.append(str(numDivisor[c]))

    print(f'O número \033[33m{num}\033[0m \033[31mnão é primo\033[0m,'
          f' pois é divisivel pelos números: \033[34m{", ".join(numDivisorStr)}')
