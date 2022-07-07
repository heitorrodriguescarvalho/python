n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

if n1 > n2:
    print(f'O primeiro valor é maior ({n1})')

elif n1 == n2:
    print(f'Não há número maior, ambosos valors são iguais. ({n1})')

else:
    print(f'O segundo valor é maior.({n2})')
