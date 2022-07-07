sal = float(input('Qual é o salário do funcionário? '))

if sal > 1250:
    aumento = sal * 0.1
else:
    aumento = sal * 0.15

print(f'O aumento do funcionário será de R${aumento}.')
