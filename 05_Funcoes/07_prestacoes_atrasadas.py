def valorPagamento(vPrestacao, diasEmAtraso, conjuntoPrestacoes):
    if (diasEmAtraso == 0):
        novoValor = vPrestacao
    else :
        novoValor = vPrestacao*(1.03+0.001*diasEmAtraso)
    conjuntoPrestacoes.append(novoValor)

pagamentos = []

while True:
    try:
        prestacao = float(input('Valor prestação: '))
        if(prestacao == 0): break
        dias = int(input('Dias em atraso: '))
    except:
        print('Valor inválido! Digite novamente.')
        continue
    if (prestacao < 0 or dias < 0):
        print('Valor inválido! Digite novamente!')
        continue
    else:
        valorPagamento(prestacao, dias, pagamentos)

print('Relatório')
print(f'Quantidade de parcelas pagas no dia: {len(pagamentos)}')
print(f'Valor total de parcelas pagas no dia: R$ {sum(pagamentos)}')
    