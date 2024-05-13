# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
# atingiram a maioridade e quantas já são maiores.

from datetime import datetime

idades = []

maiores_idade = 0
menores_idade = 0

for i in range(7):
    data_pessoa = input(f'Digite a data de nascimento da {i+1}ª pessoa (DD/MM/AAAA): ')
    data_nascimento = datetime.strptime(data_pessoa, '%d/%m/%Y')

    idade = datetime.now().year - data_nascimento.year

    idades.append(idade)

    if idade >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1

print(f'{maiores_idade} pessoas são maiores de idade.')
print(f'{menores_idade} pessoas são menores de idade.')
