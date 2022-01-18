import random
fHandle = open('palavras-forca.txt', 'r')
palavras = list()
for linha in fHandle:
    palavras.append(linha[:len(linha)-1])
fHandle.close()

palavra = list(palavras[random.randint(0, len(palavras)-1)].lower())
resposta = '_'*len(palavra)
erros = 0
while erros <= 6:
    letra = input('Digite uma letra: ').lower()
    if (letra not in palavra):
        erros += 1
        print(f'Você errou pela {erros}ª vez!\n')
        continue
    else:
        contador = palavra.count(letra)
        for i in range(0, contador):
            indice = palavra.index(letra)
            resposta = resposta[:indice] + letra + resposta[indice+1:]
            palavra[indice] = '#'
        print(resposta)
        print('')
    if ('_' not in resposta):
        print('Parabéns! Você acertou!')
        break