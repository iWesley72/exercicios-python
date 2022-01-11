vetor = list()
letras = 'aeiou'
consoantes = list()
contador = 0
for i in range(0, 10):
    while True:
        caractere = input(f'Digite o {i+1}° caractere: ')
        if (caractere.isnumeric() == True or caractere.rstrip() == '' or len(caractere)>1): 
            print('Caractere não pode: ser um número, não ser preenchido ou ser preenchido com mais de um valor.')
            continue
        else: break
    vetor.append(caractere)
    if (caractere.lower() not in letras):
        contador += 1
        consoantes.append(caractere)
print(f'Conjunto de caracteres digitado: {vetor}')
print(f'Total de consoantes: {contador}')
print(f'Conjunto de consoantes digitado: {consoantes}')