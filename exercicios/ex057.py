print('-=-' * 15, '\033[31mVerificando se o Sexo é Válido\033[m', '-=-' * 15)

sexo = str('')
sexo = str(input('Digite o seu sexo (M/F): ')).upper().strip()
while sexo not in ['M', 'F']:
    sexo = str(input('\033[31mSexo Inválido.\033[0m Informe um sexo válido \033[34m(M/F)\033[33m:\033[0m ')).upper().strip
if sexo == 'M':
    print('\033[33mSexo \033[34mMasculino\033[33m registrado.')
else:
    print('\033[33mSexo \033[34mFeminino\033[33m registrado.')
