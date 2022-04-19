"""
    Programa que simula um sistema de vendas, com sessão para clientes e funcionários.
        - Caso seja um cliente, poderá apenas comprar os produtos.
        - Caso seja um funcionário, poderá alterar o valor dos produtos mas terá que confirmar a senha do sistema.
"""

# Lista de produtos
lista = {"agua": 2.00,
        "biscoito": 1.50, 
        "pamonha": 5.00}

# "carrinho": variavel que armazena o valor total da compra
carrinho = 0
SENHA = 123


# Lista todos os produtos da lista
def listar_produtos():
    
    for produto in lista.items():
        print(f'"{produto[0].capitalize()}" : R${produto[1]:.2f}')

# Verifica se a entrada está na lista
def insistir(pergunta):

    resposta = ''
    while resposta not in lista:
        resposta = input(pergunta).lower()

    return resposta

# Função que faz um retorno para finalizar o loop
def finalizar(cliente=True):

    resposta = input("Deseja continuar? [s/n]: ").lower()

    if resposta == 'n' or resposta == 'não':
        if cliente:
            print(f"Valor total: R${carrinho:.2f}")

        return True

# Verifica se a senha está condizente
def verificar():

    resposta = input("Digite a senha: ")

    if int(resposta) == SENHA:
        return True


# Mensagem de boas vindas
print("\nSEJA BEM VINDO AO NOSSO MERCADINHO!")

# Programa geral
while True:
    
    # Switch
    escolha = input("\nDeseja fazer compras? [s/n/sair]: ").lower()

    # Se entrada for igual a "sim", entra no menu de cliente
    if escolha == 's':
        
        # Sessão do cliente
        while True:

            print("\nDigite o nome do produto para coloca-lo no carrinho:")
            listar_produtos()

            retorno = insistir("Qual produto deseja adicionar ao carrinho: ")

            # Adicionando os produtos ao carrinho com feedbacks
            if retorno in lista:
                carrinho += lista[retorno]
                print(f'"{retorno.capitalize()}" adicionado ao carrinho!\n')
                
            else:
                print("Produto inválido!\n")
                
            if finalizar(cliente=True):
                break
    
    # Se entrada for igual a "sair", encerra o programa
    elif escolha == 'sair':
        break
    
    # Se entrada for igual a "n", uma verificação acontecerá
    else:
        # Se verificação retornar "True", poderá alterar o preço dos produtos
        if verificar():
            
            # Sessão do funcionario
            while True:
                print("\nDigite o nome do produto para alterar o seu preço:")
                listar_produtos()

                retorno = insistir("Qual produto deseja alterar o preço: ")

                # Adicionando os produtos ao carrinho com feedbacks
                if retorno in lista:
                    # Recebendo novo preço do produto
                    novo_preço = 0
                    while not isinstance(novo_preço, float) or isinstance(novo_preço, int):
                        novo_preço = float(input(f"Novo preço do(a) {retorno.capitalize()}: R$"))
                        
                    lista[retorno] = novo_preço
                    print(f'Preço do "{retorno.capitalize()}" alterado com sucesso!\n')
                    listar_produtos()
                    
                else:
                    print("Produto inválido!\n")
                
                if finalizar():
                    break
        
        # Se não retornar "True", o sistema será encerrado
        else:
            print("Senha inválida, encerrando sistema.")
            break

# Mensagem final de agradecimento
print("Obrigado por escolher o nosso mercadinho, volte sempre!")
