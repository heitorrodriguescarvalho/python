i = int(input('Digite o número de início: '))
f = int(input('Digite o número final da contagem: '))
p = int(input('Digite o passo da contagem: '))

if p < 0:
    for c in range(i, f - 1, p):
        print(c)

else:
    for c in range(i, f + 1, p):
        print(c)

print('\033[1;32mA contagem chegou ao fim.')
