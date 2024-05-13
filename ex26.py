# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o
# último nome separadamente.

nome_comleto = input('Digite seu nome completo: ')

primeiro_nome = nome_comleto.split()[0]
ultimo_nome = nome_comleto.split()[-1]

print(f'PRIMEIRO NOME: {primeiro_nome}')
print(f'ÚLTIMO NOME: {ultimo_nome}')
