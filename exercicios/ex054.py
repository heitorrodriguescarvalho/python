import datetime

print('-=-' * 15, '\033[31mAnalizando se as Pessoas já Atingiram a Maioridade (21 anos)\033[m', '-=-' * 15)

# Pega as datas com dia, mês e ano separados.
currentDate = datetime.date.today()
currentDay = currentDate.day
currentMonth = currentDate.month
currentYear = currentDate.year

# Armazenam as pessoas respectivamente se elas possuem a maioridade ou não.
majority = []
nonMajority = []

for c in range(0, 7):
    birthDate = str(input(f'Digite a {c + 1}º data de nascimento (dd/mm/aaaa): '))

    # Pega o dia de nascimento.
    birthDay = birthDate[0], birthDate[1]
    birthDay = int("".join(birthDay))

    # Pega o mês de nascimento.
    birthMonth = birthDate[3], birthDate[4]
    birthMonth = int("".join(birthMonth))

    # Pega o ano de nascimento.
    birthYear = birthDate[6], birthDate[7], birthDate[8], birthDate[9]
    birthYear = int("".join(birthYear))

    # Analiza se a pessoa completou 21 anos e a coloca em sua respectiva lista.
    if currentYear - birthYear >= 22:
        majority.append(
            f'{str(birthDay).rjust(2, "0")}/{str(birthMonth).rjust(2, "0")}/{str(birthYear).rjust(2, "0")}'
        )

    elif currentYear - birthYear >= 21:
        if currentMonth - birthMonth > 0:
            majority.append(
                f'{str(birthDay).rjust(2, "0")}/{str(birthMonth).rjust(2, "0")}/{str(birthYear).rjust(2, "0")}'
            )

        elif currentMonth - birthMonth == 0:
            if currentDay - birthDay >= 0:
                majority.append(
                    f'{str(birthDay).rjust(2, "0")}/{str(birthMonth).rjust(2, "0")}/{str(birthYear).rjust(2, "0")}'
                )

            else:
                nonMajority.append(
                    f'{str(birthDay).rjust(2, "0")}/{str(birthMonth).rjust(2, "0")}/{str(birthYear).rjust(2, "0")}'
                )

        else:
            nonMajority.append(
                f'{str(birthDay).rjust(2, "0")}/{str(birthMonth).rjust(2, "0")}/{str(birthYear).rjust(2, "0")}'
            )

    else:
        nonMajority.append(
            f'{str(birthDay).rjust(2, "0")}/{str(birthMonth).rjust(2, "0")}/{str(birthYear).rjust(2, "0")}'
        )

print(f'As pessoas que nasceram nos dias \033[33m{", ".join(majority)}\033[0m, já \033[34malcaçaram a maioridade\033['
      f'0m (21 anos).\nPorém as pessoas que nasceram nos dias \033[33m{", ".join(nonMajority)},\033[0m ainda \033['
      f'31mnão alcançaram a maioridade\033[0m (21 anos).')
