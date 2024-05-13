# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco_produto = float(input('Qual o preço do produto? R$'))

novo_preco = preco_produto - (preco_produto * 0.05)

print(f'Novo preço com desconto de 5%: R${novo_preco:.2f}')
