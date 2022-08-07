print('-=-' * 15, '\033[31mUm Print Especial\033[m', '-=-' * 15)


def write(txt):
    for c in range(0, len(txt)):
        print('\033[37m-\033[0m' * (len(txt[c]) + 4))
        print(f'  {txt[c]}')
        print('\033[37m-\033[0m' * (len(txt[c]) + 4))


texts = list()
while True:
    texts.append(str(input('Digite o texto: ')))
    addMore = str(input('Deseja adicionar mais textos (y/n): ')).strip().lower()
    while addMore not in ['y', 'n']:
        print('\033[31mValor Inválido\033[0m')
        addMore = str(input('Deseja adicionar mais textos \033[31m(y/n)\033[0m: ')).strip().lower()
    if addMore == 'n':
        break
write(texts)
