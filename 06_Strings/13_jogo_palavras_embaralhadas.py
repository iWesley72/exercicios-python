import random
fHandle = open('palavras-forca.txt', 'r')
palavras = list()
for linha in fHandle:
    palavras.append(linha[:len(linha)-1])
fHandle.close()
palavra = list(palavras[random.randint(0, len(palavras)-1)].lower())
respostaCerta = ''.join(palavra)
random.shuffle(palavra)
palavra = ''.join(palavra)

print(f'Palavra embaralhada : {palavra}')

for i in range(0, 6):
    respostaUsuario = input(f'{i+1}ª tentativa: ')
    if (respostaCerta == respostaUsuario.lower()):
        print('\nResposta certa!')
        break