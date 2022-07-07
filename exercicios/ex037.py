import unidecode

num = int(input('Digite um número: '))

transformacao = str(input('Em que base você quer que ele seja convertido (Binário, Octal ou Hexadecimal)? ')).strip().capitalize()
transformacao = unidecode.unidecode(transformacao)

if transformacao == 'Binario' or transformacao == 'Octal' or transformacao == 'Hexadecimal':
    if transformacao == 'Binario':
        transformado = bin(num)
        print(transformado)

    elif transformacao == 'Octal':
        transformado = oct(num)
        print(transformado)

    elif transformacao == 'Hexadecimal':
        transformado = hex(num)
        print(transformado)
else:
    print('\033[31mOpção Inválida')
