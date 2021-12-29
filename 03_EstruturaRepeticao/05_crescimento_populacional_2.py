try:
    popA = int(input('Digite a população do pais A: '))
    taxaA = float(input('Digite a taxa de crescimento em %: '))
    popB = int(input('Digite a população pais B: '))
    taxaB = float(input('Digite a taxa de crescimento em %: '))
except:
    print('Valor inválido!')
    quit()
ano = 0
if (popA > popB):
    if (taxaA < taxaB):
        while (popB <= popA):
            ano += 1
            popA *= (taxaA/100)
            popB *= (taxaB/100)
        print('A população de B ultrapassará a de A em', ano, 'ano.')
    else:
        print('A população de B nunca passará a população de A enquanto sua taxa de crescimento for menor.')
else:
    if (taxaA > taxaB):
        while (popA <= popB):
            ano += 1
            popA *= (taxaA/100)
            popB *= (taxaB/100)
        print('A população de A ultrapassará a de B em', ano, 'anos.')
    else:
        print('A população de A nunca passará a população de B enquanto sua taxa de crescimento for menor.')