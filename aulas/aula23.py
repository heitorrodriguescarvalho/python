try:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    n = n1 / n2
except ZeroDivisionError:
    print('Não é possível dividir números por zero.')
except (ValueError, TypeError):
    print('Ocorreu um problema com o tipo do dado.')
except:
    print('Ocorreu um erro desconhecido.')
else:
    print(f'A divisão resulta em {round(n, 2)}')
finally:
    print('Volte Sempre!')
