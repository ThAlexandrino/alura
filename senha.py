import os
senha_correta = 123
usuario_correto = "th"

usuario_tentativa = input("Digite o nome do usuario: ")

senha_tentativa = int(input("Digite a senha: "))



while usuario_tentativa != usuario_correto or senha_tentativa != senha_correta:
    os.system ("cls")
    print("Usuario ou senha incorreta...")

    usuario_tentativa = input("Digite o nome do usuario: ")

    senha_tentativa = int(input("Digite a senha: "))


    

print("Entrada confirmada")