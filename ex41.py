# Refaça o DESAFIO 34 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais – ISÓSCELES: dois lados iguais, um diferente – ESCALENO: todos os lados diferentes

def forma_triangulo(a, b, c):
    return a < b + c and b < a + c and c < a + b

def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

lado1 = float(input('Digite o comprimento da primeira reta: '))
lado2 = float(input('Digite o comprimento da segunda reta: '))
lado3 = float(input('Digite o comprimento da terceira reta: '))

if forma_triangulo(lado1, lado2, lado3):
    tipo = tipo_triangulo(lado1, lado2, lado3)
    print(f'As retas podem formar um triângulo do tipo: {tipo}.')
else:
    print('As retas não podem formar um triângulo.')
