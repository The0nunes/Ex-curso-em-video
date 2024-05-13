'''
Elabore um programa que calcule o valor a ser
pago por um produto, considerando o seu preço
normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2% no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

preco_produto = float(input('Valor do produto: R$'))

print('\nO pagamento será:')
print('[1] - à vista dinheiro/cheque: 10% de desconto')
print('[2] - à vista no cartão: 5% de desconto')
print('[3] - em até 2% no cartão: preço normal')
print('[4] - 3x ou mais no cartão: 20% de juros\n')


pagamento = input('O pagamento será: ')

if pagamento == '1':
    calculo_produto = (preco_produto) - preco_produto * 0.10
    print(f'O preço do produto será: R${calculo_produto}')
elif pagamento == '2':
    calculo_produto = (preco_produto) - preco_produto * 0.05
    print(f'O preço do produto será: R${calculo_produto}')
elif pagamento == '3':
    print(f'O preço do produto será: R${preco_produto}')
elif pagamento == '4':
    calculo_produto = (preco_produto) + preco_produto * 0.20
    print(f'O preço do produto será: R${calculo_produto}')
else:
    print('Não foi possível realizar o pagamento, tente novamente')
