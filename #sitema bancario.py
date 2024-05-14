#sitema bancario

#vou criar aqui algumas credenciais de ascesso ao banco.
usuarios_senhas = [
  {"joão" : "senha123"},
  {"pedro" : "senha345"}
]

menu = """
    MENU 
  (1) Sacar
  (2) Depositar
  (3) Extrato
  (0) Sair
"""

login = input("Informe login: ").strip().lower().replace(' ', '~' )
if login == "joão":
    print("Bem vindo João!")
    print(menu)

    while True:
        opcao = input("Selecione uma opção: ")

        if opcao == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção selecionada:", opcao)
