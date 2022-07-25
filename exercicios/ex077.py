from unidecode import unidecode

print('-=-' * 15, '\033[31mContando Vogais em Tupla\033[m', '-=-' * 15)

palavras = ('Preto', 'Branco', 'Azul', 'Amarelo', 'Verde', 'Vermelho', 'Rosa', 'Laranja', 'Marrom', 'Roxo', 'Cinza')

for pos, palavra in enumerate(palavras):
    vogais = ''
    for cont, letra in enumerate(palavra):
        if unidecode(palavra[cont].lower()) in ['a', 'e', 'i', 'o', 'u']:
            vogais = f'{vogais} {palavra[cont].upper()}'
    print(f'Em \033[33m{palavras[pos]}\033[0m há \033[34m{vogais}\033[0m')
