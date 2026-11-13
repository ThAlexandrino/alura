def verificar_estoque(nome_produto, quantidade_atual):
    if quantidade_atual == 0:
        return "Produto Esgotado!! Reposição Urgente."
    elif quantidade_atual <= -1:
        return "Quantidade invalida por ser negativo"
    elif quantidade_atual < 5:
        return "Estoque baixo! Considere repor"
    else:
        return "Estoque suficiente"
    




def main():
    nome_produto = input("Qual o nome do produto: ")
    quantidade_atual = int(input("Quantidade do produto: "))
    print(verificar_estoque(nome_produto, quantidade_atual))
if __name__ == "__main__":
    main ()