import moeda

print('-=-' * 15, '\033[31mFormatando Moedas em Python\033[m', '-=-' * 15)
num = float(input('Digite um preço: R$'))
print(f'A metade de R${num} é R${moeda.moeda(moeda.metade(num))}')
print(f'O dobro de R${num} é R${moeda.moeda(moeda.dobro(num))}')
print(f'R${moeda.moeda(num)} com aumento de 20% é R${moeda.moeda(moeda.aumentar(num, 20))}')
print(f'R${moeda.moeda(num)} com desconto de 10% é R${moeda.moeda(moeda.diminuir(num, 10))}')
