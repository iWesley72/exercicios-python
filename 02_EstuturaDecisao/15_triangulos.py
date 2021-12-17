try:
    lado1 = float(input('Digite o tamanho do primeiro lado: '))
    lado2 = float(input('Digite o tamanho do segundo lado: '))
    lado3 = float(input('Digite o tamanho do terceiro lado: '))
except:
    print('Valor inválido')
    quit()
if (lado1 + lado2 > lado3 and lado2 + lado3 > lado1):
    print('É um triângulo possível.')
    if (lado1 == lado2 != lado3):
        print('É um triângulo isósceles.')
    elif (lado1 == lado2 == lado3):
        print('É um triângulo equilatero.')
    else:
        print('É um triângulo escaleno.')
else:
    print('Não é um triângulo possível.')