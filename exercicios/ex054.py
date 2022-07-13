import datetime

print('-=-' * 15, '\033[31mAnalizando se as Pessoas já Atingiram a Maioridade (21 anos)\033[m', '-=-' * 15)

idadeList = []
for c in range(0, 7):
    idade = str(input(f'Digite a {c}º idade (dd/mm/aaaa): '))
