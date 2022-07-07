cidade = str(input('Qual o nome da sua cidade? ')).strip().title()

cidadeDividida = cidade.split()

print(f'A cidade de {cidade} começa com "Santo": {"Santo" in cidadeDividida[0]}')
