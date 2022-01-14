def somaImposto(taxaImposto, custo):
    custoFinal = custo*(1+taxaImposto/100)
    print('R$ ' ,custoFinal)

taxaTeste = float(input('Imposto sobre produto (%): '))
custoTeste = float(input('Custo produto sem imposto: '))
somaImposto(taxaTeste, custoTeste)