# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Número 01: '))
n2 = float(input('Número 02: '))
n3 = float(input('Número 03: '))

if n1 > n2 and n1 > n3:
    print('O "Número 01" é o maior')
elif n2 > n1 and n2 > n3:
    print('O "Número 02" é o maior')
else:
    print('O "Número 03" é o maior')
