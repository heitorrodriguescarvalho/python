print('-=-' * 15, '\033[31mAnalisando e Gerando Dicionários\033[m', '-=-' * 15)


def notas(lista, sit=False):
    """
    Mostra os dados das notas
    :param lista: Contém as notas
    :param sit: Indica se a situação da turma deve ser mostrada ou não
    :return: Retorna um dicionário com os dados
    """
    dados = dict()
    dados['total'] = len(lista)
    dados['maior'] = max(lista)
    dados['menor'] = min(lista)
    dados['media'] = round(sum(lista) / len(lista), 2)
    if sit:
        if dados['media'] < 6:
            dados['situacao'] = 'ruim'
        elif dados['media'] < 7:
            dados['situacao'] = 'razoável'
        else:
            dados['situacao'] = 'boa'
    else:
        dados['situacao'] = 'indefinida'
    return dados


num = list()
cont = 0
while True:
    cont += 1
    n = float(input(f'Digite o {cont}º número (ou "-1" para parar): '))
    while n < -1:
        print('\033[31mValor Inválido!\033[0m')
        n = float(input(f'Digite o {cont}º número (ou "-1" para parar): '))
    if n < 0:
        break
    else:
        num.append(n)
situacao = str(input('Deseja mostrar a situação da turma (y/n): '))
while situacao not in ['y', 'n']:
    print('\033[31mValor Inválido!\033[0m')
    situacao = str(input('Deseja mostrar a situação da turma (y/n): '))
if situacao == 'y':
    info = notas(num, sit=True)
else:
    info = notas(num)
print('\033[37m-\033[0m' * 40)
print(f'''Total de Notas: {info["total"]}
Maior Nota: {info["maior"]}
Menor Nota: {info["menor"]}
Nota Média: {info["media"]}''')
if info['situacao'] != 'indefinida':
    print(f'Situação da Turma: {info["situacao"].capitalize()}')


