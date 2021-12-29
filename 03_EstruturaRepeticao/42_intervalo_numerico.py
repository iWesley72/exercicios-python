grupo1 = []
grupo2 = []
grupo3 = []
grupo4 = []
cont = 0
while True:
    try:
        num = int(input('Digite algum inteiro positivo: '))
    except:
        print('Valor inválido! Tente novamente.')
        continue
    if (num<=0):
        break
    if (1<=num<=25):
        grupo1.append(num)
    elif (26<=num<=50):
        grupo2.append(num)
    elif (51<=num<=75):
        grupo3.append(num)
    elif (76<=num<=100):
        grupo4.append(num)
    else:
        cont += 1
print(f'Existem {len(grupo1)} no intervalo [1-25].')
print(f'Existem {len(grupo2)} no intervalo [26-50].')
print(f'Existem {len(grupo3)} no intervalo [51-75].')
print(f'Existem {len(grupo4)} no intervalo [76-100].')
print(f'Existe {cont} fora desses intervalos.')
