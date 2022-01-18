texto = input('Texto: ').lower()
texto = texto.replace(' ', '')
teste = list(texto)
teste.reverse()
textoNovo = ''
for i in teste:
    textoNovo += i
if (texto == textoNovo): print('É um palíndromo.')
else: print('Não é um palíndromo.')