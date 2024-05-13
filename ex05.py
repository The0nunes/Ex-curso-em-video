# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt

n = float(input('Digite um número: '))

dobro = n * 2
triplo = n * 3
raiz_quadrada = sqrt(n)

print(f'Dobro: {dobro}')
print(f'Triplo: {triplo}')
print(f'Raíz quadrada: {raiz_quadrada:.2f}')