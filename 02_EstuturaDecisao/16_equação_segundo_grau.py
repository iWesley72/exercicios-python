print('**Equação do 2° Grau: AX²+BX+C=0**')
try:
    a = float(input('Digite o valor de A: '))
    b = float(input('Digite o valor de B: '))
    c = float(input('Digite o valor de C: '))
except:
    print('Valor inválido.')
    quit()
if (a == 0):
    print('A constante A deve ser diferente de 0!')
else:
    delta = b**2-4*a*c
    if (delta == 0):
        print('Existe apenas uma solução real possível.')
        x = -b/(2*a)
        print('X =', x)
    elif (delta < 0):
        print('Não existem soluções reais.')
    else:
        print('Existem duas soluções reais.')
        x1 = (-b + (delta**(1/2)))/(2*a)
        x2 = (-b - (delta**(1/2)))/(2*a)
        print('X\' =', x1)
        print('X\'\' =', x2)