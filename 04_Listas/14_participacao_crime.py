respostas = list()

c = 0
while True:
    if (c == 0):
        resp = input('Telefonou para a vítima? (S/N): ').lower()
    elif (c == 1):
        resp = input('\nEsteve no local do crime? (S/N): ').lower()
    elif (c == 1):
        resp = input('\nMora perto da vítima? (S/N): ').lower()
    elif (c == 3):
        resp = input('\nDevia para a vítima? (S/N): ').lower()
    else:
        resp = input('\nJá trabalhou com a vítima? (S/N): ').lower()
    if (resp not in 'SsNn'):
        print('Resposta inválida! Tente novamente.')
        continue
    else:
        c += 1
        respostas.append(resp)
    if (c == 5):
        break
print('')
if (respostas.count('s') == 5):
    print('Assassino!')
elif (respostas.count('s') >= 3):
    print('Cúmplice!')
elif (respostas.count('s') == 2):
    print('Suspeito!')
else:
    print('Inocente!')