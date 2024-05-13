# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número de 0 a 9999: '))

if numero >= 0 and numero <= 9999:
    unidade = numero % 10
    dezena = (numero // 10) % 10
    centena = (numero // 100) % 10
    milhar = (numero // 1000) % 10

    print(f'Unidade: {unidade}')
    print(f'Dezena: {dezena}')
    print(f'Centena: {centena}')
    print(f'Milhar: {milhar}')
else:
    print('Número fora do intervalo desejado!')