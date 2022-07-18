from emoji import emojize

print('-=-' * 15, '\033[31mSequência de Fibonacci\033[m', '-=-' * 15)

num = int(input('Quantos \033[33mnúmeros da sequência\033[0m devem ser \033[34mmostrados\033[0m? '))

cont = int(2)
sequencia = [0, 1]
print(emojize(":seta_para_a_direita:", language="pt"), sequencia[-2], end=" ")
print(emojize(":seta_para_a_direita:", language="pt"), sequencia[-1], end=" ")
while cont < num:
    cont += 1
    sequencia.append(sequencia[-2] + sequencia[-1])
    print(emojize(":seta_para_a_direita:", language="pt"), sequencia[-1], end=" ")
