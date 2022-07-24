print('-=-' * 15, '\033[31mTuplas com Times de Futebol\033[m', '-=-' * 15)

times = ('Palmeiras', 'Corinthians', 'Atlético-MG', 'Fluminense', 'Athletico-PR', 'Internacional', 'Flamengo',
         'Bragantino', 'São Paulo', 'Santos', 'Botafogo', 'Ceará SC', 'Goiás', 'Avaí', 'Cuiabá', 'Coritiba',
         'América-MG', 'Atlético-GO', 'Fortaleza', 'Juventude')

primeiros5 = times[0]
for c in range(1, 5):
    primeiros5 = f'{primeiros5}, {times[c]}'

ultimos4 = times[-1]
for c in range(2, 5):
    ultimos4 = f'{ultimos4}, {times[-c]}'

timesAlfabetica = ', '.join(sorted(times))

america = times.index('América-MG')

print(f'Os \033[33m5 primeiros\033[0m times da tabela do Brasileirão são: \033[34m{primeiros5}.\033[0m')
print(f'Os \033[33m4 últimos\033[0m times da tabela do Brasileirão são: \033[31m{ultimos4}.\033[0m')
print(f'Todos os times \033[33m(em ordem alfabética)\033[0m:')
for pos, time in enumerate(times):
    print(f'\033[34m{pos + 1}º {time}\033[0m')
print(f'O \033[33mAmérica-MG\033[0m está na: \033[34m{america + 1}º posição\033[0m.')
