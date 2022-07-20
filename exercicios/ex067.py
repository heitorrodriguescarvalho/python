print('-=-' * 15, '\033[31mTabuada\033[m', '-=-' * 15)

print('\033[31mCaso deseja parar, digite um valor negativo!\033[0m')
print('\033[37m-\033[0m' * 45)

while True:
    num = int(input('Deseja ver a tabuada de qual valor? '))
    if num >= 0:
        for c in range(0, 11):
            print(f'{num} x {c:2} = {num * c:2}')
    else:
        break
print('\033[31mPrograma Interrompido!\033[0m')
