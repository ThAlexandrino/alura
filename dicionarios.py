jogo_lista = []

def jogos():
    nome_do_jogo = input("Digite o nome do jogo: ")
    genero_do_jogo = input(f"Digite o genero do jogo {nome_do_jogo}:")
    jogo_zerado = input("Você já zerou esse jogo? :")
    finalizado = False

    if jogo_zerado == 'sim':
        finalizado = True

    elif jogo_zerado == 'não':

        finalizado = False

    dados_do_jogo = {'nome': nome_do_jogo, 'genero': genero_do_jogo, 'finalizado': finalizado}
    jogo_lista.append(dados_do_jogo)

def listar_jogos():
    for lista in jogo_lista:
        nome = lista['nome']   
        genero = lista['genero']
        finalizado = lista['finalizado']

        print(f'{nome} | {genero} | {finalizado}')




def main():
    jogos()
    listar_jogos()

if __name__ == '__main__':
    main()