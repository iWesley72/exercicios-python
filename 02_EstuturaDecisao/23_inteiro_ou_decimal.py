try:
    numero = float(input('Digite algum número, inteiro ou decimal: '))
except:
    print('Valor inválido!')
    quit()
if (round(numero) != numero):
    print('É um número com casa decimal.')
else:
    print('É um número inteiro.')