print('-=-' * 15, '\033[31mFicha do Jogador\033[m', '-=-' * 15)


def ficha(nome="Desconhecido", gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Número de gols: '))
if n.isalpha() and g.isnumeric():
    ficha(n, int(g))
elif n.isalpha() and not g.isnumeric():
    ficha(n)
elif not n.isalpha() and g.isnumeric():
    ficha(gols=int(g))
else:
    ficha()
