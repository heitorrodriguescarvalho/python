print('-=-' * 15, '\033[31mValidando Expressões Matemáticas\033[m', '-=-' * 15)

mat = str(input('Digite a expressão: '))
aberto = 0
fechado = 0
real = True
for c in range (0, len(mat)):
    if mat[c] == '(':
        aberto += 1
    elif mat[c] == ')':
        fechado += 1
    if aberto - fechado == -1:
        real = False
if aberto - fechado == 0 and real:
    print('A expressão está correta!')
else:
    print('A expressão está errada!')
