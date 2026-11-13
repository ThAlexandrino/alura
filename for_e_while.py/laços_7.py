estoque_inicial = 5
while estoque_inicial >0:
    estoque_inicial -= 1
    print(f"Vendo realizada!! Estoque restante {estoque_inicial}")
    if estoque_inicial == 0:
        print("Estoque esgotado")
        break