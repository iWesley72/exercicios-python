vetorA = list()
for i in range(0, 10):
    while True:
        try:
            vetorA.append(int(input(f'Digite o {i+1}° valor: '))**2)
        except:
            print('Valor inválido! Digite novamente.')
            continue
        break
print(f'A soma do quadrado dos elementos {sum(vetorA)}.')