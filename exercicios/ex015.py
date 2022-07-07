dias = int(input('Quantos dias o carro será alugado? '))
km = float(input('Quantos quilômetros rodados? '))
print(f'O valor do aluguel é de R${dias*60+km*0.15:.2f}')