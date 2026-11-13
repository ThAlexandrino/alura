
def imp_par(num):
    if num % 2 == 1:
        return "Impar"
    elif num % 2 == 0:
        return "Par"


def mensagem(num, resultado):
    print(f"O número {num} é {resultado}")


def main():
    num = int(input("Insira um número para saber se é impar ou par: "))

    resultado = imp_par(num)
    mensagem(num, resultado)


if __name__ == "__main__":
    main()
