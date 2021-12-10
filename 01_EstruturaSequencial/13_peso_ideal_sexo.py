altura = float(input('Digite sua altura em metros: '))
sexo = input('Você é homem(H) ou mulher(M)? ')
if (sexo == 'H' or sexo == 'h'):
    print('Seu peso ideal é', round(((72.7*altura)-58), 2), 'kg.')
elif (sexo == 'M' or sexo == 'm'):
    print('Seu peso ideal é', round(((62.1*altura)-44.7), 2), 'kg.')
else:
    print('Sexo inválido.')