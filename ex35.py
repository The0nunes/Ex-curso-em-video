# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

def aprovar_emprestimo(valor_casa, salario_comprador, anos):
    valor_emprestimo = valor_casa / (anos * 12)
    percentual_maximo = salario_comprador * 0.3

    if valor_emprestimo <= percentual_maximo:
        return True
    else:
        return False

valor_casa = float(input('Digite o valor da casa: R$'))
salario_comprador = float(input('Digite o salário do comprador: R$'))
anos = int(input('Em quantos anos ele vai pagar? '))

if aprovar_emprestimo(valor_casa, salario_comprador, anos):
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado!')

