while True:
    nome_usuario = input("Digite o nome do usuario:")
    senha = input ("Digite sua senha: ")
    if len(nome_usuario) <5:
        print('o Nome do usuario deve ter pelo menos 5 caracter')
        continue
    if len(senha) <8:
        print("A senha deve conter pelo menos 8 caracteres")
        continue
    print("Cadastro realizado com sucesso")
    break