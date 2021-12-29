contador = 0
soma = 0
for i in range(1, 6):
    contador += 1
    try:
        valor = int(input('Digite algum valor a ser adicionado: '))
    except:
        print('Valor inválido!')
        quit()
    soma += valor
print('Soma dos valores:', soma)
print('Média dos valores:', (soma/contador))