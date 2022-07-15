print('-=-' * 15, '\033[31mAnalizando Quem Pesa Mais e Quem Pesa Menos\033[m', '-=-' * 15)

pesoMaior = float
pesoMenor = float
for c in range(0, 5):
    peso = round(float(input(f'Quanto a {c + 1}º pessoa pesa (Kg)? ')), 1)
    if c == 0:
        pesoMaior = peso
        pesoMenor = peso

    else:
        if peso > pesoMaior:
            pesoMaior = peso

        if peso < pesoMenor:
            pesoMenor = peso

print(f'A pessoa mais \033[34mleve\033[0m pesa \033[33m{pesoMenor}Kg\033[0m '
      f'e a pessoa mais \033[32mpesada\033[0m pesa \033[33m{pesoMaior}Kg\033[0m.')
