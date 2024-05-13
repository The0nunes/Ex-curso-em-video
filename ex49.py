# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

contador = 1
soma_numeros_pares = 0

while contador < 7:
    n = int(input(f'Digite o {contador}º número: '))
    if n % 2 == 0:
        soma_numeros_pares += n
    else:
        pass
    contador += 1
print(f'A soma dos números PARES digitados: {soma_numeros_pares}')
