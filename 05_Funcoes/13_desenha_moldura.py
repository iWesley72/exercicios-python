def desenharMoldura(linhas=1, colunas=1):
    if (linhas > 20):
        linhas = 20
    elif (colunas > 20):
        colunas = 20
    
    print('+' + '-'*colunas + '+')
    #print(('|' + ' '*colunas + '|\n')*linhas)
    for i in range(linhas):
        print(('|' + ' '*colunas + '|'))
    print('+' + '-'*colunas + '+')
desenharMoldura(20,20)