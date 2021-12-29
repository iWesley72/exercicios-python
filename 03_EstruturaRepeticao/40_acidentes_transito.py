# indice de acidentes = numero de acidentes / numero de veiculos

maiorIndice = 0
menorIndice = 0
codMaiorIndice = 0
codMenorIndice = 0
totalVeiculos = 0
totalAcidentes = 0
contador = 0
acidenteAte2000 = 0
for i in range(1, 6):
    while True:
        try:
            codigoCidade = int(input('Código da cidade: '))
            nVeiculos = int(input('Qtd. veículos de passeio: '))
            nAcidentes = int(input('Qtd. acidentes de trânsito: '))
        except:
            print('Valor inválido! Tente novamente.')
            continue
        indice = round(nAcidentes/nVeiculos)
        break
    totalAcidentes += nAcidentes
    totalVeiculos += nVeiculos
    if (maiorIndice == 0):
        maiorIndice = indice
        codMaiorIndice = codigoCidade
    elif (maiorIndice < indice):
        maiorIndice = indice
        codMaiorIndice = codigoCidade
    
    if (menorIndice == 0):
        menorIndice = indice
        codMenorIndice = codigoCidade
    elif (menorIndice > indice):
        menorIndice = indice
        codMenorIndice = codigoCidade

    if (nVeiculos < 2000):
        contador += 1
        acidenteAte2000 += nAcidentes

mediaVeiculos = round(totalVeiculos/5)
mediaAcidentes = round(totalAcidentes/5)
mediaAcidentesAte2000 = round(acidenteAte2000/contador)

print(f'A cidade com o código {codMenorIndice} teve o menor indice, sendo {menorIndice} acidentes por veículo.')
print(f'A cidade com o código {codMaiorIndice} teve o maior indice, sendo {maiorIndice} acidentes por veículo.')
print(f'A média de veículos das 5 cidades somadas foi {mediaVeiculos} veículos por cidade.')
print(f'A média de acidentes de trânsito nas cidades com menos de 2000 veículos foi de {mediaAcidentes} acidentes por veículo.')
