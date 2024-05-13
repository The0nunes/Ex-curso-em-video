'''
A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

- até 9 anos: mirim
- até 14 anos: infantil
- até 19 anos: júnior
- até 20 anos: sênior
- acima de 20: master
'''
from datetime import datetime

data_nascimento = input('Digite sua data de nascimento (DD/MM/AAAA): ')

data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
data_atual = datetime.now()
idade = data_atual.year - data_nascimento.year - ((data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day))

if idade <= 9:
    print('mirim')
elif idade <= 14:
    print('infantil')
elif idade <= 19:
    print('junior')
elif idade <= 20:
    print('sênior')
else:
    print('master')