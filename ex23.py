# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Digite o nome da sua cidade: ')

primeiro_nome_cidade = cidade.split()[0]

if primeiro_nome_cidade.lower() == 'santo':
    print('O nome da cidade começa com "SANTO"')
else:
    print('O nome da cidade não começa com "SANTO"')
