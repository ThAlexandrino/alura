def plano_cartesiano(x, y):
    if x > 0 and y > 0:
        return "Primeiro quadrante"
    elif x < 0 and y > 0:
        return "Segundo quadrante"
    elif x < 0 and y < 0:
        return "Terceiro quadrante"
    elif x > 0 and y < 0:
        return "Quarto quadrante"
    else:
        return "Ponto localizado no eixo ou margem"

def mensagem(x,y,resultado):
    print(f"Com os valores {x} e {y} você se encontra no: {resultado}")

def main():
    x = float(input("Digite a coordenada X: "))
    y = float(input("Digite a coordenada Y: "))
    resultado = plano_cartesiano(x,y)
    mensagem(x,y,resultado)
if __name__ == "__main__":
    main()