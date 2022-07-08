print('-=-' * 15, '\033[31mCalculadora de IMC\033[m', '-=-' * 15)

peso = float(input('Quanto você pesa (Kg)? '))
altura = float(input('Quanto você mede (cm)? '))

imc = round(peso/altura**2, 1)

if imc < 18.5:
    print(f'Você está abaixo do peso ideal.(IMC de {imc})')

elif 18.5 >= imc <= 25:
    print(f'Você está no peso ideal.(IMC de {imc})')

elif imc <= 30:
    print(f'Você está com sobrepeso.(IMC de {imc})')

elif imc <= 40:
    print(f'Você está com obesidade.(IMC de {imc})')

elif imc > 40:
    print(f'Você está com obesidade mórbida.(IMC de {imc})')
