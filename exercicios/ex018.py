from math import radians, sin, cos ,tan
ang = int(input('Digite um ângulo: '))
print(f'Seu seno é {sin(radians(ang)):.2f}\n'
      f'Seu cosseno é {cos(radians(ang)):.2f}\n'
      f'Sua tangente é {tan(radians(ang)):.2f}')
