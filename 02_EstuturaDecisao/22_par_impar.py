try:
    numero = int(input('Digite algum número inteiro: '))
except:
    print('Valor inválido!')
    quit()
if (numero % 2 == 0):
    print(numero, 'é par.')
else:
    print(numero, 'é impar.')