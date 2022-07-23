lanche = 'suco', 'sorvete', 'hamburguer'
for pos, comida in enumerate(lanche):
    print(f'Para o meu lanche, comprarei um {comida} na posição {pos}.')
del lanche

print('Mais tarde...')
lanche = 'pastel', 'refrigerante'
for pos, comida in enumerate(lanche):
    print(f'Também comprarei um {comida} na posição {pos}.')
