soma = num = int(0)
while True:
    num = int(input('Digite um número: '))
    if num == int(999):
        break
    soma += num
print(soma)
