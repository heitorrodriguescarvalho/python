nome = str(input('Digite seu nome e sobrenome: ')).strip()

nomeSemEspacos = nome.replace(' ', '')
nomeDividido = nome.split()

print(f"""Em maiúsculo: {nome.upper()}
Em minúsculo: {nome.lower()}
Contagem de letras: {len(nomeSemEspacos)}
Contagem de letras do primeiro nome: {len(nomeDividido[0])}""")
