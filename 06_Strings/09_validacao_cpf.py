cpf = input('CPF: ')
cpf = list(cpf)
while '.' in cpf: cpf.remove('.')
while '-' in cpf: cpf.remove('-')

somaPrimeiroDigito = 0
contador = 10
for i in range(1, 10): 
    somaPrimeiroDigito += int(cpf[i-1])*contador
    contador += -1
somaPrimeiroDigito = somaPrimeiroDigito*10 % 11
testePrimeiroDigito = somaPrimeiroDigito == int(cpf[9])

somaSegundoDigito = 0
contador = 11
for i in range(1, 11): 
    somaSegundoDigito += int(cpf[i-1])*contador
    contador += -1

somaSegundoDigito = somaSegundoDigito*10 % 11
testeSegundoDigito = somaSegundoDigito == int(cpf[10])

if (testeSegundoDigito == True and testePrimeiroDigito == True): print('CPF válido!')
else: print('CPF inválido!')