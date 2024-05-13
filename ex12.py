# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite seu salário: R$'))

reajuste_salario = salario + (salario * 0.15)

print(f'Seu novo salário com o rejuste de 15%: R${reajuste_salario}')
