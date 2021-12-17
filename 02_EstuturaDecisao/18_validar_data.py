data = input('Digite uma data no formata dd/mm/aaaa (Ex: 01/01/2003): ')
try:
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])
except:
    print('Data inválida.')
    quit()

if (ano % 4 == 0): #ano bissexto
    if (mes in [1, 3, 5, 7, 8, 10, 12] and 0<dia<=31):
        print('Data válida.')
    elif (mes in [4, 6, 9, 11] and 0<dia<=30):
        print('Data válida.')
    elif (mes == 2 and 0<dia<=29):
        print('Data válida.')
    else:
        print('Data inválida.')
else:
    if (mes in [1, 3, 5, 7, 8, 10, 12] and 0<dia<=31):
        print('Data válida.')
    elif (mes in [4, 6, 8, 11] and 0<dia<=30):
        print('Data válida.')
    elif (mes == 2 and 0<dia<=28):
        print('Data válida.')
    else:
        print('Data inválida.')