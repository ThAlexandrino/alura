segundos = 10
while segundos > 0:
    if segundos % 2 == 0:
        print(f"Faltam apenas {segundos} segundos - Não perca essa oportunidade")
        segundos -= 1
    elif segundos % 2 ==1:
        print(f"a contagem continua: {segundos} restantes")
        segundos -= 1
print("Aproveite a promoção agora")