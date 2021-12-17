print('**LISTA DE OPERAÇÕES**')
print('1 - Adição')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('\n')
operacao = input('Digite a operação desejada: ')
try:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
except:
    print('Valor inválido!')
    quit()
if ('1234'.find(operacao) != -1):
    if (operacao == '1'):
        resultado = num1 + num2
    elif (operacao == '2'):
        resultado = num1 - num2
    elif (operacao == '3'):
        resultado = num1*num2
    else:
        resultado = num1/num2
    print('Resultado:', resultado)
    if (resultado % 2 == 0):
        print('Número par.')
    else:
        print('Número impar.')
    if (resultado > 0):
        print('Número positivo.')
    elif (resultado < 0):
        print('Número negativo.')
    else:
        print('Numero nulo.')
    if (resultado != round(resultado)):
        print('Número decimal.')
    else:
        print('Número inteiro.')
else:
    print('Operação inválida')