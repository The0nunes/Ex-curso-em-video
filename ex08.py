# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Digite qualquer numero: '))
i = 1

while i <= 10:
    print(f'{n} x {i} = {n * i}')
    i += 1
