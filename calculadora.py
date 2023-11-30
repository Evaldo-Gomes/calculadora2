# Interface da Calculadora

import calc2

#Apresentação
print('\n\t\t\t  --  Calculadora 2  --\n')

# Entrada
num1 = int(input('Informe o n1: '))
num2 = int(input('Informe o n2: '))

# Processamento
totalSoma = soma(num1, num2)
totalSub = sub(num1, num2)
totalMult = mult(num1, num2)

# Saída
print(f'Resultado da soma: {num1} + {num2} = {totalSoma}')
print(f'Resultado da subtração: {num1} - {num2} = {totalSub}')
print(f'Resultado da multiplicação: {num1} * {num2} = {totalMult}')

