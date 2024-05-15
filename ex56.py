# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


while True:
    resposta = input('Digite seu sexo, apenas resposta "M" ou "F": ').upper()
    if resposta == 'M' or resposta == 'F':
        print('Valor correto')
        break
    else:
        print('Valor inválido, por favor digite novamente.')
