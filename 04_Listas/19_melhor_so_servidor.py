votos = [0]*6
sistemas = {0:'Windows Server', 1:'Unix', 2:'Linux', 3:'Netware', 4:'Mac OS', 5:'Outro'}

print('Enquete: Qual o melhor sistema operacional para servidores?')
print('1 - Windows Server\n2 - Unix\n3 - Linux\n4 - Netware\n5 - Mac OS\n6 - Outro')

while True:
    try:
        voto = int(input('Número do sistema operacional: '))
    except:
        print('Sistema operacional inválido! Tente novamente.')
        continue
    if (voto == 0):
        break
    elif (voto < 0 or voto > 6):
        print('Sistema operacional inválido! Tente novamente.')
        continue
    else:
        votos[voto-1] += 1
        continue

print('{:<19} {:<5} {:<3}'.format('Sistema Operacional', 'Votos' , '%'))
print('{:<19} {:<5} {:<3}'.format('-'*19, '-'*5, '-'*3))

for i in range(0, 6):
    porcentagem = round(votos[i]/sum(votos)*100, 2)
    print('{:<19} {:<5} {:<3}'. format(sistemas[i], votos[i], str(porcentagem)+'%'))

print('{:<19} {:<5} {:<3}'.format('-'*19, '-'*5, '-'*3))
print('{:<19} {:<5}'.format('Total', sum(votos)))

indiceMaisVotado = votos.index(max(votos))
maiorQtdVotos = max(votos)
porcentagem = round(maiorQtdVotos/sum(votos)*100, 2)

print(f'O Sistema Operacional mais votado foi o {sistemas[indiceMaisVotado]}, com {maiorQtdVotos} votos, correspondendo a {porcentagem}% dos votos.')