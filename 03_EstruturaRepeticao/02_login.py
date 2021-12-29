usuario = senha = ''
while (usuario == senha):
    usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')
    if(usuario == senha):
        print('A senha deve ser diferente do nome de usuário.')
    else:
        print('Usuário e senha válidos.')