print('**GUIA PARA RESPONDER AS PERGUNTAS**')
print('Serão feitas 5 perguntas sobre um crime ficticio, de acordo com suas respostas será determinada sua participação no mesmo.')
print('As perguntas deverão ser respondidas com sim, usando s, ou não, usando n. \n')
contador = 0
p1 = input('Você telefonou para vitima? R: ')
if (p1 == 's'):
    contador += 1
elif (p1 == 'n'):
    contador += 0
else:
    print('Digite uma resposta válida!')
    quit()
p2 = input('Você esteve no local do crime? R: ')
if (p2 == 's'):
    contador += 1
elif (p2 == 'n'):
    contador += 0
else:
    print('Digite uma resposta válida!')
    quit()
p3 = input('Você mora perto da vitima? R: ')
if (p3 == 's'):
    contador += 1
elif (p3 == 'n'):
    contador += 0
else:
    print('Digite uma resposta válida!')
    quit()
p4 = input('Você devia para a vitima? R: ')
if (p4 == 's'):
    contador += 1
elif (p4 == 'n'):
    contador += 0
else:
    print('Digite uma resposta válida!')
    quit()
p5 = input('Já trabalhou com a vitima? R: ')
if (p5 == 's'):
    contador += 1
elif (p5 == 'n'):
    contador += 0
else:
    print('Digite uma resposta válida!')
    quit()
if (contador == 2):
    print('Sua classificação foi: suspeita.')
elif (3<=contador<=4):
    print('Sua classificação foi: cúmplice.')
elif (contador == 5):
    print('Sua classificação foi: assassino.')
else:
    print('Sua classificação foi: inocente.')