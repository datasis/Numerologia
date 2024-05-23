import json
import os

# Dicionário para armazenar os clientes
clientes = {}

# Nome do arquivo para salvar os dados
arquivo_clientes = "clientes.json"

def carregar_dados():
    global clientes
    if os.path.exists(arquivo_clientes):
        with open(arquivo_clientes, 'r') as arquivo:
            clientes = json.load(arquivo)
            print("Dados carregados com sucesso.")
    else:
        print("Nenhum dado encontrado, iniciando com lista de clientes vazia.")

def salvar_dados():
    with open(arquivo_clientes, 'w') as arquivo:
        json.dump(clientes, arquivo, indent=4)
        print("Dados salvos com sucesso.")

def cadastrar_cliente():
    codigo = input("Digite o código do cliente: ")
    nome = input("Digite o nome do cliente: ")
    data_nascimento = input("Digite a data de nascimento do cliente (dd/mm/aaaa): ")
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o e-mail do cliente: ")
    rede_social = input("Digite a rede social do cliente: ")
    cidade = input("Digite a cidade do cliente: ")
    estado = input("Digite o estado do cliente: ")

    clientes[codigo] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "telefone": telefone,
        "email": email,
        "rede_social": rede_social,
        "cidade": cidade,
        "estado": estado
    }
    salvar_dados()

def visualizar_cliente():
    codigo = input("Digite o código do cliente que deseja visualizar: ")
    cliente = clientes.get(codigo)
    
    if cliente:
        for chave, valor in cliente.items():
            print(f"{chave}: {valor}")
    else:
        print("Cliente não encontrado.")

def listar_clientes():
    if clientes:
        for codigo, dados in clientes.items():
            print(f"\nCódigo: {codigo}")
            for chave, valor in dados.items():
                print(f"{chave}: {valor}")
    else:
        print("Nenhum cliente cadastrado.")

# Carregar os dados ao iniciar o programa
carregar_dados()

while True:
    print("\nMenu:")
    print("1. Cadastrar Cliente")
    print("2. Visualizar Cliente")
    print("3. Listar Clientes")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        visualizar_cliente()
    elif opcao == "3":
        listar_clientes()
    elif opcao == "4":
        salvar_dados()
        break
    else:
        print("Opção inválida, tente novamente.")