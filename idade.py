def idadee(idade_usuario):
    if idade_usuario == 0 and idade_usuario <= 12:
        return "Criança"
    elif idade_usuario > 13 and idade_usuario <= 18:
        return "Adolescente"
    elif idade_usuario >18:
        return "Adulto"

def mensagem(idade_usuario, resultado):
    print (f"O usuario tem {idade_usuario} e é um {resultado}")


def main():
    idade_usuario = int(input("Qual a idade do usuario: "))
    resultado = idadee(idade_usuario)
    mensagem(idade_usuario,resultado)
if __name__ == "__main__":
    main()