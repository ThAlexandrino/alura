def converter(celsius):
    fareheit = (celsius* 9/5 ) + 32
    return fareheit

def mensagem(resultado_converter, celsius):
    return (f"está fazendo {resultado_converter}° fh e {celsius}° graus")


def main():
    celsius = float(input("Quantos graus celsius faz: "))


    resultado_converter = converter(celsius)

    
    print(mensagem(resultado_converter,celsius))

if __name__ == "__main__":
    main()