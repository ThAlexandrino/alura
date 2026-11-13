import os

restaurantes = [{'nome': 'Pizzaria Suprema', 'categoria': 'Pizza', 'ativo': False},
                {'nome': 'Sandubalu', 'categoria': 'Hamburguer', 'ativo': True},
                {"nome": 'Crocs', 'categoria': 'Salgados', 'ativo': False}]
def exibir_nome_do_programa():
    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝  
    """)

def opcao():
    print("1. Cadastrar Restaurante", "2. Listar Restaurantes", "3. Ativar Restaurante", "4. Sair", sep="\n")

def usuario_escolha():
    digitar_escolha = int(input("Digite a opção: "))
    return digitar_escolha

def voltar_ao_app():
    input("\nDigite a tecla enter para voltar ao menu   ")
    main()


def exibir_subtitulos(nome):
    os.system("Cls")
    print("*" * len(nome))
    print(nome)
    print("*" * len(nome) )


def cadastro_restaurantes():
    exibir_subtitulos("Bem-vindo ao cadastro de restaurantes")

    nome_do_restaurante = input ("Digite o nome do Restaurante: ")
    categoria = input (f"Digite a categoria do {nome_do_restaurante}: ")
    dados_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)

    print(f"O restaurante {nome_do_restaurante} Foi cadastrado com sucesso!!!")
    voltar_ao_app()
def listar_restaurantes():
    exibir_subtitulos("Listando Restaurantes")

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}")
    for restaurante in restaurantes:
        nome_lista_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'

        print(f"- {nome_lista_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {ativo}")


    voltar_ao_app()

def finalizar_app():
    os.system("Cls")
    print("Finalizando app")

def opcao_invalida():
    print("Opção invalida")
    voltar_ao_app()



def alternar_estado_restaurante():
    exibir_subtitulos('Alternando estado do restaurante')

    nome_do_restaurante = input("Digite o nome do restaurante para alternar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'o Restaurante {nome_do_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")
    voltar_ao_app()



def escolha_usuario(escolha):
    try:
        match escolha:
            case 1:
                cadastro_restaurantes()
            case 2: 
                listar_restaurantes()
            case 3:
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
            opcao_invalida()

def main():
    os.system("Cls")
    exibir_nome_do_programa()
    opcao()
    escolha = usuario_escolha()
    escolha_usuario(escolha)
    


if __name__ == "__main__":
    main()