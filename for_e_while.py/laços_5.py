projetos = ["Website", "jogo", "análise de dados", None, "aplicativo móvel"]
for i in projetos:
    if i is None:
        print("Projeto não encontrado")
        continue
    print(i)
