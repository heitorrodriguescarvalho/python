brasil = list()
estado = dict()

for c in range(0, 3):
    estado['nome'] = str(input('Nome do Estado: ')).strip().capitalize()
    estado['sigla'] = str(input('Sigla do Estado: ')).strip().upper()
    brasil.append(estado.copy())
for uf in brasil:
    for n in uf.values():
        print(n, end=" ")
    print()
