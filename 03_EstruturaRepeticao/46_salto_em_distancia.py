tentativas = []
while True:
    nome = input('Atleta: ')
    if (nome == ''):
        break
    else:
        for i in range(1, 6):
            while True:
                try:
                    tentativas.append(float(input(f'{i}° salto (m): ')))
                except:
                    print('Valor inválido! Digite novamente.')
                    continue
                break
        maiorSalto = max(tentativas)
        menorSalto = min(tentativas)
        tentativas.remove(maiorSalto)
        tentativas.remove(menorSalto)
        print(f'\nMelhor salto: {maiorSalto} m')
        print(f'Pior salto: {menorSalto} m')
        print(f'Média dos demais saltos: {round(sum(tentativas)/3, 2)} m\n')
        print(f'Resultado final: ')
        print(f'{nome}: {round(sum(tentativas/3, 2))} m.')