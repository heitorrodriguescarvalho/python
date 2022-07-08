print('-=-'*20, '\033[31mAnalisando Notas\033[m', '-=-' *20)
n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite sua outra nota: '))

media = (n1 + n2) / 2

if n1 >= 0 and n1 <= 10 and n2 >= 0 and n2 <= 10:

    if media < 5:
        print(f'Infelizmente, você foi reprovado, pois sua média foi {media} pontos.')

    elif 5 <= media < 7:
        print(f'Nem tudo está perdido! Você pegou recuperação com uma nota média de {media} pontos.')

    elif media >= 7:
        print(f'Parábens, você foi aprovado com uma nota média de {media} pontos.')

else:

    print('Valores Inválidos')