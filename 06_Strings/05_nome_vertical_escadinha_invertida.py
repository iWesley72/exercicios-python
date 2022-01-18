print('Nome na vertical em escada invertida\n')
nome = input('Seu nome: ')
for i in range(len(nome), -1, -1):
    print(nome[0:i+1])