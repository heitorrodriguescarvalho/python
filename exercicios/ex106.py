print('-=-' * 15, '\033[31mSistema Interativo de Ajuda em Python\033[m', '-=-' * 15)


def linhas(txt, cor):
    print(f'{cor}~\033[m' * (len(txt) + 4))
    print(f'{cor}  {txt}  \033[m')
    print(f'{cor}~\033[m' * (len(txt) + 4))


while True:
    linhas('PyHelp System', '\033[42m')
    comando = str(input('\033[1mFunção ou Biblioteca >'))
    if comando == 'stop':
        break
    print('\033[7m')
    print(help(comando))
    print('\033[m')
