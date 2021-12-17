print('**Combustiveis**')
print('A - Alcool (R$1,90/L)')
print('G - Gasolina (R$2,50/L)\n')

combustivel = input('Digite o combustível desejado(A ou G): ')
try:
    litros = float(input('Digite quantos litros você quer abastecer: '))
except:
    print('Valor inválido!')
    quit()
if (0<litros<=20):
    if (combustivel.lower() == 'a'):
        preco = litros*1.9*0.97
        print('Valor total: R$', round(preco, 2))
    elif (combustivel.lower() == 'g'):
        preco = litros*2.5*0.96
        print('Valor total: R$', round(preco, 2))
    else:
        print('Combustível digitado inválido!')
elif (litros>20):
    if (combustivel.lower() == 'a'):
        preco = litros*1.9*0.95
        print('Valor total: R$', round(preco, 2))
    elif(combustivel.lower() == 'g'):
        preco = litros*2.5*0.94
        print('Valor total: R$', round(preco, 2))
    else:
        print('Combustível digitado inválido!')
else:
    print('Não é possível abastecer quantias nulas ou negativas.')