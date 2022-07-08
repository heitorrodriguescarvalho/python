print('-=-'*20, '\033[31mAnalizando sua Categoria de Natação\033[m', '-=-' *20)

idade = int(input('Quantos anos você tem? '))

if idade > 0 and idade <= 9:
    print('Você está na categoria mirim.')

elif idade <= 14:
    print('Você está na categoria infantil.')

elif idade <= 19:
    print('Voce está na categoria junior.')

elif idade <= 20:
    print('Você está na categoria sênior.')

elif idade > 20:
    print('Você está na categoia master.')

else:
    print('O valor inserido é inválido.')
