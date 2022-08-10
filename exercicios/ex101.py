from datetime import date

print('-=-' * 15, '\033[31mFunções para Votação\033[m', '-=-' * 15)


def voto(birthDate):
    age = int((date.today() - birthDate).days / 365.2425)
    if age < 16:
        votar = 'Negado'
    elif 15 < age > 18:
        votar = 'Opcional'
    elif age < 60:
        votar = 'Obrigatório'
    else:
        votar = 'Opcional'
    return age, votar


birthDay = int(input('Dia do Nascimento: '))
birthMonth = int(input('Mês do Nascimento: '))
birthYear = int(input('Ano do Nascimento: '))
data = voto(date(birthYear, birthMonth, birthDay))
print(f'Uma pessoa de {data[0]} anos tem o voto \033[1m{data[1]}\033[0m.')
