vel = int(input('Qual é a valocidade do carro? '))

if vel <= 80:
    print('Boa viagem!')
else:
    velUltrapassada = int(vel - 80)
    valor = int(velUltrapassada * 7)

    print(f'Encosta o carro! Você foi multado em R${valor:.2f}.')
