# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario_funcionario = float(input('Digite seu salário: R$'))

if salario_funcionario > 1250:
    novo_salario = salario_funcionario * 0.10 + salario_funcionario
    print(f'Reajustado 10%: R${novo_salario:.2f}')
else:
    novo_salario = salario_funcionario * 0.15 + salario_funcionario
    print(f'Reajustado 15%: R${novo_salario:.2f}')

