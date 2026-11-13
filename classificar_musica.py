
def verificar_acesso(nivel_usuario, status_pagamento):
    if nivel_usuario == "admin":
        print("Acesso total")
    if status_pagamento == "pago":
        print("Acesso liberado")
    else:
        print("Acesso negado")

        
def main():
    nivel_usuario = input("Qual seu nivel de usuario:")
    status_pagamento = input("Qual seu status de pagamento: ")
    verificar_acesso(nivel_usuario, status_pagamento)


if __name__ == '__main__':
    main()