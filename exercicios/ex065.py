print('-=-' * 15, '\033[31mTirando a Média de Valores\033[m', '-=-' * 15)

print('\033[31mAviso:\033[0m para \033[33mparar\033[0m digite \033[34m"stop"\033[0m')

# Coleta os números digitados pelo usuário.
parar = str('')
num = []
while parar != 'Y':
    valor = str(input('Digite um número inteiro ou "stop": ')).strip().lower()
    if valor.isnumeric():
        num.append(int(valor))
    elif valor == 'stop':
        parar = 'Y'
    else:
        print('\033[31mDigite um valor válido!\033[0m')

# Tira a média dos valores.
numSomados = sum(num)
media = numSomados / len(num)
if str(media)[-1] == '0' and str(media)[-2] == '.':
    media = int(media)

# encontra o maior e o menor valor.
c = int(1)
maior = num[0]
menor = num[0]
while c < len(num):
    if num[c] > maior:
        maior = num[c]
    elif num[c] < menor:
        menor = num[c]
    c += 1

# Mostra as informações.
print('Os números digitados foram:')
c = int(1)
print('\033[34m', num[0], end="")
while c < len(num):
    print(',\033[34m', num[c], end="")
    c += 1
print(f'\n\033[0mA \033[33mmédia\033[0m dos valores é \033[32m{media}\033[0m,'
      f' o maior valor é \033[32m{maior}\033[0m e o menor é \033[32m{menor}\033[0m.')
