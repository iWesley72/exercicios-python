print('Instruções:')
print('Digite a temperatura em °C, caso não queira inserir mais nenhuma temperatura digite \'X\'\n')
temperaturas = []
contador = 1
while True:
    temperaturas.append(input('Digite a temperatura: '))
    if (temperaturas[contador-1] == 'X' or temperaturas[contador-1] == 'x'):
        break
    try:
        float(temperaturas[contador-1])
    except:
        print('Valor inválido! Tente novamente')
        continue
    contador += 1
temperaturas.pop()
print(f'Maior temperatura: {max(temperaturas)} °C.')
print(f'Menor temperatura: {min(temperaturas)} °C.')
media = sum(float(i) for i in temperaturas) / contador
print(f'Temperatura média: {round(media, 2)} °C.')
