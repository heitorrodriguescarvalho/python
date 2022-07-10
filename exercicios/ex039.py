import datetime

ano = datetime.datetime.now().date().year

nasc = int(input('Em que ano você nasceu? '))

if ano - nasc == 18:
    print('Está na hora de se alistar')

elif ano - nasc < 18:
    print(f'Você só tem que se alistar daqui {18 - (ano - nasc)} anos.')

elif ano - nasc > 18:
    print(f'Se você não se alistou, já se passaram {(ano - nasc) - 18} anos que você devia ter se alistado')
