print('Verificaremos se é possivel formar um triâgulo com retas de determinados comprimentos. Então digite:')
r1 = float(input('O comprimento da primeira reta: '))
r2 = float(input('Da segunda: '))
r3 = float(input('E da terceira: '))

r1str = str(r1)
r2str = str(r2)
r3str = str(r3)
if r1str[-1] == '0':
    r1 = int(r1)
if r2str[-1] == '0':
    r2 = int(r2)
if r3str[-1] == '0':
    r3 = int(r3)

if r1 - r2 < r3:
    if r1 + r2 > r3:
        if r1 - r3 < r2:
            if r1 + r3 > r2:
                if r2 - r3 < r1:
                    if r2 + r3 > r1:
                        print(f'É possivel formar um triângulo com as medidas de {r1}cm, {r2}cm e {r3}cm.')
                    else:
                        print(f'Não é possivel formar um triângulo com as medidas de {r1}cm, {r2}cm e {r3}cm.')
                else:
                    print(f'Não é possivel formar um triângulo com as medidas de {r1}cm, {r2}cm e {r3}cm.')
            else:
                print(f'Não é possivel formar um triângulo com as medidas de {r1}cm, {r2}cm e {r3}cm.')
        else:
            print(f'Não é possivel formar um triângulo com as medidas de {r1}cm, {r2}cm e {r3}cm.')
    else:
        print(f'Não é possivel formar um triângulo com as medidas de {r1}cm, {r2}cm e {r3}cm.')
else:
    print(f'Não é possivel formar um triângulo com as medidas de {r1}cm, {r2}cm e {r3}cm.')
