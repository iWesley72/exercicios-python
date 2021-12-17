try:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
except:
    print('Nota inválida!')
    quit()
media = (n1+n2+n3)/3
print('A média foi', round(media, 2))
if (media == 10):
    print('Aprovado com distinção!')
elif (media >= 7):
    print('Aprovado!')
else:
    print('Reprovado!')