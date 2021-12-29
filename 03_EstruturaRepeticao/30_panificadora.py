try:
    valor = float(input('Preço do pão: '))
except:
    print('Valor inválido!')
    quit()
for i in range(1, 51):
    print(f'{i} - R${round(i*valor,2)}')