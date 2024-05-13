# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Temperatura em graus Celsius: '))

convercao_fahrenheit = (celsius * 9 / 5) + 32

print(f'A temperatura em °C é {celsius} \nConvertendo para °F é {convercao_fahrenheit}')
