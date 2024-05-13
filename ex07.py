# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor_metros = float(input('Valor em metros: '))

cm = valor_metros * 100
ml = valor_metros * 1000

print(f'Valor em centímetros {cm} \nValor em milímetros {ml}')
