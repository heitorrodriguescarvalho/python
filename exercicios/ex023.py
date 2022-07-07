numStr = str(input('Digite um número de 0 a 9999: '))
num = numStr.zfill(4)

u = num[3]
d = num[2]
c = num[1]
m = num[0]

print(f"""Milhar: {m}
Centena: {c}
Dezena: {d}
Unidade: {u}""")
