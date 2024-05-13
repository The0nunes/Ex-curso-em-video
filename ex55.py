# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

nomes = []
idades = []
sexos = []

for i in range(4):
    nome = input(f'Digite o nome da {i+1}ª pessoa: ')
    idade = int(input(f'Digite a idade da {i+1}ª pessoa: '))
    sexo = input(f'Digite o sexo da {i+1}ª pessoa (M/F): ')

    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

idade_media = sum(idades) / len(idades)

homens = [nomes[i] for i in range(len(nomes)) if sexos[i].upper() == 'M']
idades_homens = [idades[i] for i in range(len(idades)) if sexos[i].upper() == 'M']
homem_mais_velho = homens[idades_homens.index(max(idades_homens))]

mulheres_menos_20 = sum(1 for i in range(len(nomes)) if sexos[i].upper() == 'F' and idades[i] < 20)

print(f'A média de idade do grupo é: {idade_media:.1f} anos')
print(f'O homem mais velho é: {homem_mais_velho}')
print(f'{mulheres_menos_20} mulher(es) têm menos de 20 anos')
