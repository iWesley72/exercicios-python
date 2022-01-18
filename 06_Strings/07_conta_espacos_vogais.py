texto = input('Frase: ').lower()
texto = list(texto)
espacosBrancos = texto.count(' ')
vogais = 0
for i in ['a', 'e', 'i','o', 'u']:
    vogais += texto.count(i)
print(f'Total de espaçoes em branco: {espacosBrancos}')
print(f'Total de vogais: {vogais}')