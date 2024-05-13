# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar
# ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá
# mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

data_nascimento = input('Digite sua data de nascimento (DD/MM/AAAA): ')

data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')

data_atual = datetime.now()
idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))

if idade == 18:
    print('Hora de se alistar.')
elif idade > 18:
    tempo = idade - 18
    print(f'Está atrasado para o alistamento, deveria ter se alistado há {tempo} ano(s).')
else:
    tempo = 18 - idade
    print(f'Ainda não é hora de se alistar, faltam {tempo} ano(s).')
