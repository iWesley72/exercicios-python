contador = 0
idades = []
while True:
    try:
        idades.append(int(input('Digite a idade: ')))
    except:
        print('Valor inválido!')
        continue
    contador += 1
    p = input('Você quer adicionar mais alguma idade?(S/N): ').lower()
    if (p == 's'):
        continue
    elif (p == 'n'):
        break
    else:
        print('Não entendemos o que você digitou.')
media = sum(idades)/contador
print(f'A média da idade é {round(media)}!')
if (0<media<=25):
    print('É um grupo jovem.')
elif (25<media<=60):
    print('É um grupo adulto.')
elif (60<media):
    print('É um grupo idoso.')