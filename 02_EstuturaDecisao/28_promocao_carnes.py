# Só queria saber, onde saiu esse valor da picanha?
print('**TABELA DE CARNES**')
print('A - Filé Duplo')
print('B - Alcatra')
print('C - Picanha\n')
carne = input('Qual carne você deseja comprar? ')
try:
    quantidade = float(input('Quantos kg você deseja comprar? '))
except:
    print('Valor inválido!')
    quit()
formaPagamento = input('Você deseja pagar essa compra no cartão da loja?(S/n) ')
valorTotal = 0
if (carne.lower() == 'a'):
    tipoCarne = 'Filé Duplo'
    if (quantidade > 5):
        valorTotal += 5.8*quantidade
    else:
        valorTotal += 4.9*quantidade
elif (carne.lower() == 'b'):
    tipoCarne = 'Alcatra'
    if (quantidade > 5):
        valorTotal += 6.8*quantidade
    else:
        valorTotal += 5.9*quantidade
elif (carne.lower() == 'c'):
    tipoCarne = 'Picanha'
    if (quantidade > 5):
        valorTotal += 7.8*quantidade
    else:
        valorTotal += 6.9*quantidade
else:
    print('Tipo de carne inválido!')
    quit()
if (formaPagamento.lower() == 's'):
    metodo = 'Cartão'
    valorDesconto = valorTotal*0.05
elif (formaPagamento.lower() == 'n'):
    metodo = 'Dinheiro'
    valorDesconto = 0
else:
    print('Forma de pagamento inválida.')
    quit()
valorFinal = valorTotal - valorDesconto
print('\nTipo de carne:', tipoCarne)
print('Quantidade:', quantidade, 'kg.')
print('Preço total: R$', round(valorTotal, 2))
print('Forma de pagamento:', metodo)
print('Valor desconto: R$', round(valorDesconto, 2))
print('Valor a pagar: R$', round(valorFinal, 2))