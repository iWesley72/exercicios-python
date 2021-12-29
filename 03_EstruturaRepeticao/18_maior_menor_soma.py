try:
    n = int(input('Você deseja inserir quantos números: '))
except:
    print('Valor inválido!')
    quit()
valores = []
soma = 0
for n in range(1, n+1):
    try:
        valor = int(input('Digite o valor que você deseja adicionar: '))
    except:
        print('Valor inválido!')
        quit()
    valores.append(valor)
    soma += valor
    print('')
print(f'O menor valor é {min(valores, key=int)}.')
print(f'O maior valor é {max(valores, key=int)}.')
print(f'A soma de todos os {n} valores adicionados é {soma}.')
