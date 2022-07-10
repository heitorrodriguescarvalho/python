num = int(input('Digite um número: '))

transformacao = int(input('Em que base você quer que ele seja convertido (1. Binário; 2. Octal; 3. Hexadecimal)? '))


if transformacao == 1:
    transformado = bin(num)
    print(transformado)

elif transformacao == 2:
    transformado = oct(num)
    print(transformado)

elif transformacao == 3:
    transformado = hex(num)
    print(transformado)
else:
    print('\033[31mOpção Inválida')
