print('{:<17} {:<8} {:<10}'.format('Produto', 'Código', 'Preço'))
print('{:<17} {:<8} {:<10}'.format('Cachorro Quente', '100', 'R$ 1,20'))
print('{:<17} {:<8} {:<10}'.format('Bauru Simples', '101', 'R$ 1,30'))
print('{:<17} {:<8} {:<10}'.format('Bauru com ovo', '102', 'R$ 1,50'))
print('{:<17} {:<8} {:<10}'.format('Hamburguer', '103', 'R$ 1,20'))
print('{:<17} {:<8} {:<10}'.format('Cheeseburguer', '104', 'R$ 1,30'))
print('{:<17} {:<8} {:<10}'.format('Refrigerante', '105', 'R$ 1,00'))

print('Para encerrar o pedido digite \'0\'.')
valorTotal = 0
while True:
    pedido = input('Código do produto: ')
    if (pedido == '0'):
        break
    elif (pedido == '100'):
        preco = 1.2
    elif (pedido == '101'):
        preco = 1.3
    elif (pedido == '102'):
        preco = 1.5
    elif (pedido == '103'):
        preco = 1.2
    elif (pedido == '104'):
        preco = 1.3
    elif (pedido == '105'):
        preco = 1
    else:
        print('Código inválido! Tente novamente.')
        continue
    while True:
        try:
            qtd = int(input('Quantidade: '))
        except:
            print('Valor inválido! Tente novamente.')
            continue
        if (qtd<0):
            print('A quantidade deve ser um inteiro positivo, ou igual a zero se mudou de ideia com relação ao produto. Tente novamente!')
            continue
        break
    valorTotal += preco*qtd
print(f'Valor total do pedido: R$ {round(valorTotal, 2)}')