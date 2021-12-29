while True:
    n = input('Digite o valor: ')
    if (n.isnumeric() == True):
        if(int(n) <= 0):
            print('O valor de ser um inteiro positivo não nulo!')
            continue
    else:
        print('O valor de ser um inteiro positivo não nulo!')
        continue
    break
m = ''
for i in range(len(n)-1, -1, -1):
    m += n[i]
print(m)