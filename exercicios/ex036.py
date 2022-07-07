print('-=-' *20, '\033[1;31mAprovando Finaciamento\033[m', '-=-' *20)

valor = float(input('Qual é o valor da casa? '))
valor = round(valor, 2)
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos você vai pagar a casa? '))
meses = int(anos*12)

mensal = (valor/anos)/12

if mensal > salario/10*3:
    print('Infelizmente o seu Financiamento foi negado devido ao alto valor.')
else:
    print(f'Parabéns, o seu Financiamento de {meses} meses foi aprovado.')
    print(f'Você pagará o impréstimo em prestações de R${mensal:.2f}')
    print(f'R${valor:.2f} foi depositado na sua conta temporariamente.')
