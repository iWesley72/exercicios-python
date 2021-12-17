letra = input('Digite alguma letra para testar se é uma vogal ou consoante: ')
if ('aeiou'.find(letra.lower()) != -1):
    print('É uma vogal.')
else:
    print('É uma consoante.')