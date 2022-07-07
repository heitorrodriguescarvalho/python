from random import choice
a1 = str(input('Escreva o nome do primeiro aluno: '))
a2 = str(input('Do segundo: '))
a3 = str(input('Do terceiro: '))
a4 = str(input('E do quarto: '))
lista = [a1, a2, a3, a4]

sorteado = choice(lista)

print(f'{sorteado.capitalize()} vai apagar o quadro hoje!')
