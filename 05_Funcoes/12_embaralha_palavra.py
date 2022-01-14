import random

def embaralhaPalavra(palavra):
    palavra = palavra.upper()
    novaPalavra = ''
    letras = list(palavra)
    for i in range(1, len(palavra)):
        letra = random.choice(letras)
        novaPalavra += letra
        letras.remove(letra)
    print(novaPalavra)

embaralhaPalavra('Python')