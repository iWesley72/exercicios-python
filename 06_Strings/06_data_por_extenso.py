print('Data por extenso\n')
data = input('Data de Nascimento(dd/mm/aaaa): ')
data = data.split('/')
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

meses = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}
if (mes not in meses):
    print('Data inválida!')
elif (mes in [1, 3, 5, 7, 8, 10, 12] and 1<=dia<=31 == False):
    print('Data inválida!')
elif (mes in [4, 7, 9, 11] and 1<=dia<=30 == False):
    print('Data inválida!')
elif (mes == 2 and ano % 4 == 0 and 1<=dia<=29 == False):
    print('Data inválida!')
elif (mes == 2 and ano % 4 != 0 and 1<=dia<=28 == False):
    print('Data inválida!')
else:
    print(f'Você nasceu em {dia} de {meses.get(mes)} de {ano}')