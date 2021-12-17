try:
    ano = int(input('Digite algum ano para testar: '))
except:
    print('Ano inválido!')
    quit()
if (ano % 4 == 0):
    print(ano, 'é um ano bissexto!')
else:
    print(ano, 'não é um ano bissexto.')