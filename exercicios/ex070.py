print('-=-' * 15, '\033[31mSistema de Compras\033[m', '-=-' * 15)

# Coleta o nome e o preço do produto.
soma = 0
caros = []
novoProduto = ''
cont = 0
while novoProduto != 'n':
    novoProduto = ''
    print('\033[34mAdicionando Produto\033[0m')
    cont += 1
    nome = str(input('Digite o Nome do Produto: ')).capitalize().strip()
    valor = float(input('Digite o Preço do Produto: \033[32mR$\033[0m'))
    print('\033[37m-\033[0m' * 40)

    # Verifica se o usuário deseja adicionar mais produtos.
    while novoProduto not in ['y', 'n']:
        novoProduto = str(input('Deseja adicionar mais um produto (y/n)? ')).lower().strip()

    # Verifica os dados.
    soma += valor

    if valor > 1000:
        caros.append(nome)

    if cont == 1:
        baratoProduto = [nome]
        baratoValor = valor
    else:
        if baratoValor > valor:
            baratoValor = valor
            baratoProduto = [nome]
        elif baratoValor == valor:
            baratoProduto.append(nome)
        print(baratoProduto)

# Mostra os dados ao usuário.
print(f'1. O \033[32mvalor final\033[0m de todos os produtos é de \033[34mR${soma:.2f}\033[0m;')
print(f'2. Dos {cont} produtos, os que \033[32mcustam mais de R$1000.00\033[0m são: \033[34m{", ".join(caros)}\033[0m;')
print(f'3. O(s) produto(s) de \033[32mmenor preço\033[0m foi(ram): \033[34m{", ".join(baratoProduto)}\033[0m.')
