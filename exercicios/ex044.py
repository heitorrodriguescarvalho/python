print('-=-' * 15, '\033[31mCalculando o Preço Final\033[m', '-=-' * 15)

valor = round(float(input('Qual foi o valor da compra? ')), 2)

f1 = valor - valor / 10
f2 = valor - valor / 20
f3 = valor
f4 = valor + valor / 5

print(f'''Essas são as formas de pagamento:
1. À vista \033[1;34mDinheiro/Cheque\033[0;0m: \033[1;33m10%\033[0;0m de Desconto; (\033[1;33mR${f1:.2f}\033[0;0m)
2. À vista no \033[1;34mCartão\033[0;0m: \033[1;33m5%\033[0;0m de Desconto; (\033[1;33mR${f2:.2f}\033[0;0m)
3. Em até \033[1;34m2x no Cartão\033[0;0m: preço normal; (\033[1;33mR${f3:.2f}\033[0;0m)
4. \033[1;34m3x ou mais\033[0;0m no cartão: \033[1;33m20%\033[0;0m de Juros. (\033[1;33mR${f4:.2f}\033[0;0m)''')

f = int(input('Qual será sua \033[0;33mforma de pagamento\033[0;0m? '))

if f == 1:
    print(f'\033[1;34mCompra realizada com sucesso\033[0;0m no valor final de \033[1;33mR${f1}\033[0;0m!')

elif f == 2:
    print(f'\033[1;34mCompra realizada com sucesso\033[0;0m no valor final de \033[1;33mR${f2}\033[0;0m!')

elif f == 3:
    print(f'\033[1;34mCompra realizada com sucesso\033[0;0m no valor final de \033[1;33mR${f3}\033[0;0m!')

elif f == 4:
    print(f'\033[1;34mCompra realizada com sucesso\033[0;0m no valor final de \033[1;33mR${f4}\033[0;0m!')

else:
    print('\033[0;31mO valor digitado é inválido.\033[0;0m')
