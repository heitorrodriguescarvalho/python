nome = str(input('Digite um nome e sobrenome: ')).title().split()
print(f"""No nome {' '.join(nome)}:
O primeiro nome é: {nome[0]};
O último nome é: {nome[len(nome) - 1]}""")
