# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

entrada = input('Digite qualquer coisa: ')

tipo_primitivo = type(entrada)

print(f'Tipo primitivo {tipo_primitivo}')
print(f'Informações {dir(entrada)}')

