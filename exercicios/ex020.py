from random import shuffle

a1 = str(input('Escreva o nome do primeiro aluno: '))
a2 = str(input('Do segundo: '))
a3 = str(input('Do terceiro: '))
a4 = str(input('E do quarto: '))

lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'Ordem de Apresentação:\n'
      f'1º: {lista[0].capitalize()};\n'
      f'2º: {lista[1].capitalize()};\n'
      f'3º: {lista[2].capitalize()};\n'
      f'4º: {lista[3].capitalize()}.')
