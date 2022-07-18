print('-=-' * 15, '\033[31mSomando Valores\033[m', '-=-' * 15)

print('Digite números infinitamente e, quando quiser parar, digite "999"')

numVezes = int(0)
soma = float(0)
num = float(0)
while num != 999:
    num = float(input(f'Digite o {numVezes + 1}º número: '))
    if num != 999:
        soma += num
        numVezes += 1

if str(soma)[-1] == '0' and str(soma)[-2] == ".":
    soma = int(soma)
print(f'Você digitou \033[33m{numVezes}\033[0m números e a soma entre todos eles é \033[34m{soma}\033[0m.')
