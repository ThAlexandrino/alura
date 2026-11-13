pergunta_idade = int(input("Qual a sua idade: "))

def carteira():
    pergunta_carteira = input("Você tem carteira de motorista: ").lower()

    while pergunta_carteira != "sim" and pergunta_carteira != "não":

        print("não entendi nenhuma das informações, tente novamente...")
        pergunta_carteira = input("Você tem carteira de motorista: ").lower()

    if pergunta_carteira == "sim":
        carteira_de_motorista = True

    elif pergunta_carteira == "não":
        carteira_de_motorista   = False

    return carteira_de_motorista

carteirademotorista = carteira()

if pergunta_idade >= 18 and carteirademotorista == True:
    print("ótimo, pode dirigir")
elif pergunta_idade <= 18 or carteirademotorista == False:
    print("Que pena, você tem idade inferior a 18 anos ou não possue carteira de motorista")
