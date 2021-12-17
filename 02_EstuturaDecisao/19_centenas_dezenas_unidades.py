# importei a função floor para conseguir arredondar o valor das centenas, dezenas e unidades para o menor possível, para que não quando fosse extrair eles não tivesse casas decimais e nem fosse algum valor maior que o correto
from math import floor
try:
    num = int(input('Digite um número inteiro menor que 1000: '))
except:
    print('Valor inválido!')
    quit()
centena = floor(num/100)
dezena = floor((num - centena*100)/10)
unidade = floor((num - centena*100 - dezena*10))
msg = ''
if (centena > 0):
    if (centena == 1):
        msg += str(centena) + ' centena'
    else:
        msg += str(centena) + ' centenas'
if (dezena > 0):
    if (centena > 0):
        msg += ', '
    if (dezena == 1):
        msg += str(dezena) + ' dezena'
    else:
        msg += str(dezena) + ' dezenas'
if (unidade > 0):
    if (dezena > 0 or centena > 0):
        msg += ' e '
    if (unidade == 1):
        msg += str(unidade) + ' unidade'
    else:
        msg += str(unidade) + ' unidades'
print(msg)