n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))
n3 = float(input('Digite só mais um número: '))

n1str = str(n1)
if n1str[-1] == '0':
    n1 = int(n1)

n2str = str(n2)
if n2str[-1] == '0':
    n2 = int(n2)

n3str = str(n3)
if n3str[-1] == '0':
    n3 = int(n3)

#Verificando o maior
if n1 >= n2:
    maior = n1
else:
    maior = n2

if maior < n3:
    maior = n3

#Verificando o menor
if n1 <= n2:
    menor = n1
else:
    menor = n2

if menor > n3:
    menor = n3

print(f'O menor número é {menor} e o maior número é {maior}.')
