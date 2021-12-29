notas = []
notas.append(float(input('Digite a nota: ')))
contador = 1
notas.append(float(input('Digite outra nota: ')))
contador += 1
while True:
    p = input('Deseja adicionar outra nota?(S/N): ').lower()
    if (p == 's'):
        notas.append(float(input('Digite outra nota: ')))
        contador += 1
    elif (p == 'n'):
        break
    else:
        print('Não entendemos o que você digitou.')
media = sum(notas)/contador
print(f'A média final é {round(media, 2)}')