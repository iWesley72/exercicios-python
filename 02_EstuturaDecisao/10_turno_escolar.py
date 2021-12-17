turno = input('Se você é do turno matutino digite M, noturno N e vespertino V: ')
if (turno.lower() == 'm'):
    print('Bom dia!')
elif (turno.lower() == 'n'):
    print('Boa noite!')
elif (turno.lower() == 'v'):
    print('Boa tarde!')
else:
    print('Valor inválido!')