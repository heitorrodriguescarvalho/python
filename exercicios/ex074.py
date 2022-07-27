from random import randint

print('-=-' * 15, '\033[31mMaior e Menor Valor em Tuplas\033[m', '-=-' * 15)

num = ((randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10)))
print(f'Os números são: {num[0]}', end="")
for n in range(1, len(num)):
    print(f', {num[n]}', end="")
print(f'\nO \033[33mmaior\033[0m número é \033[34m{max(num)}\033[0m e'
      f' o \033[33mmenor\033[0m número é \033[31m{min(num)}\033[0m.')
