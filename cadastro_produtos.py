def verificar_estoque(quantidade):
    if quantidade == 0:
        return "Produto Esgotado!! Reposição Urgente."
       
    if quantidade <5:
        return "Estoque baixo! Considere repor"
        
    else:
        return "Estoque suficiente"
        

def formatar_mensagem(nome, status):
    return f"O produto {nome} está com: {status}"



def main ():
    for i in range(3): 
        print (f"Cadastro do produto {i+1}")
        nome = input ("Nome: ")
        quantidade = int(input("Quantidade: "))
        status = verificar_estoque(quantidade)

        print (formatar_mensagem(nome, status))

if __name__ == "__main__":
    main()