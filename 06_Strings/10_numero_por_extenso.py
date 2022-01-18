valoresDezena = {'1':'dez', '2':'vinte', '3':'trinta', '4':'quarenta', '5':'cinquenta', '6':'sessenta', '7':'setenta', '8':'oitenta', '9':'noventa'}
valoresUnidade ={'1':'um', '2':'dois', '3':'três', '4':'quatro', '5':'cinco', '6':'seis', '7':'sete', '8':'oito', '9':'nove', '0':'zero'}
valoresExcessao = {'11':'onze', '12':'doze', '13':'treze', '14':'quatorze', '15':'quinze', '16':'dezesseis', '17':'dezessete', '18':'dezoito', '19':'dezenove'}
numero = input('Número de 0 até 99: ')
if (numero.isnumeric == False or int(numero) > 99): print('Valor inválido')
else:
    if (numero in valoresExcessao):
        print(valoresExcessao.get(numero))
    elif (len(numero) == 1):
        print(valoresUnidade.get(numero))
    elif (len(numero) == 2 and numero[1] == '0'):
        print(valoresDezena.get(numero[0]))
    elif (len(numero) == 2 and numero[1] != '0'):
        print(valoresDezena.get(numero[0]), 'e', valoresUnidade.get(numero[1]))
