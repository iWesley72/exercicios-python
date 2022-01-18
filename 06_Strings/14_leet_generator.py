# referência para alfabeto: https://www.ionos.com/digitalguide/online-marketing/social-media/what-is-leetspeak/

import random
fHandle = open('out.txt', 'r')
alfabeto = dict()
for linha in fHandle:
    alfabeto[linha[0]] = linha[2:len(linha)-1].split(',')
fHandle.close()

texto = input('Texto: ')
novoTexto = ''
for letra in texto.upper():
    if (letra.isalpha()):
        opcoesLetra = alfabeto.get(letra)
        novoTexto += str(opcoesLetra[random.randint(0, len(opcoesLetra)-1)]).strip()
    else:
        novoTexto += letra
print(novoTexto)