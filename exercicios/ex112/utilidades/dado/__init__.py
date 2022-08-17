def leiadinheiro(pergunta):
    valor = str(input(pergunta))
    validade = False
    while not validade:
        validade = True
        if not valor.isnumeric():
            for pos, n in enumerate(valor):
                if not valor[pos].isdecimal() and valor[pos] not in [',', '.']:
                    validade = False
            if valor[0] in ['.', ','] or valor[-1] in ['.', ',']:
                validade = False
        if not validade:
            print('\033[31mValor Inválido\033[0m')
            valor = str(input(pergunta))
    return valor
