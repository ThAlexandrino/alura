pergunta_idade = int(input("Qual a sua idade: "))

def estudante():
    pergunta_estudante = input("Você é estudante: ").lower()

    while pergunta_estudante != "sim" and pergunta_estudante != "não":
        print ("Não consegui identificar, tente novamente.")
        pergunta_estudante = input("Você é estudante: ").lower()

    if pergunta_estudante == "sim":
        estudando_mesmo = True

    elif pergunta_estudante == "não":
        estudando_mesmo = False

    return estudando_mesmo

meia_entrada = estudante ()

if pergunta_idade < 18 or meia_entrada == True:
    print("Você tem direito a meia entrada")

elif pergunta_idade >= 18 and meia_entrada == False:
    print("Você não tem direito a meia entrada")


