# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = []

for i in range(5):
    peso_pessoa = float(input(f'Digite o peso da {i+1}ª pessoa, ex: 50.90: '))
    pesos.append(peso_pessoa)

maior_peso = max(pesos)
menor_peso = min(pesos)

print(f'O maior peso lido foi: {maior_peso} kg')
print(f'O menor peso lido foi: {menor_peso} kg')
