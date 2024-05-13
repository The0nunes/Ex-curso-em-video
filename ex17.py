# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo_graus = float(input('Digite o valor do ângulo em graus: '))

angulo_radianos = math.radians(angulo_graus)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

print(f'O seno do ângulo é: {seno:.2f}')
print(f'O cosseno do ângulo é: {cosseno:.2f}')
print(f'A tangente do ângulo é: {tangente:.2f}')
