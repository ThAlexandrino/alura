preco_hamburguer = 12.00
preco_batata = 7.00
preco_refri = 5.00

qtd_hamburguer =int(input("Quantos Hamburguer: "))
qtd_batata = int(input("Quantas batatas fritas: "))
qtd_refrigerante = int(input("Quantos refrigerantes: "))

valor_da_conta = float((preco_hamburguer * qtd_hamburguer) + (preco_batata *qtd_batata)+ (qtd_refrigerante*preco_refri))  
print(f"o valor da conta é R${valor_da_conta:.2f}")