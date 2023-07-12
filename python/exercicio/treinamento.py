# import
import os
import textwrap

# constantes
LIMITE_SAQUE = 3
AGENCIA = "0001"


# variáveis
saldo = 0
limite = 500
extrato = ""
valor = 0
numero_saque = 0
usuarios = []
contas = []

# MÉTODOS:

# menu
def menu():
    print("""
======== STB-SISTEMA BANCÁRIO =========         

Menu
          
[d] Depósito    [nc] Nova Conta
[s] Saque       [lc] Listar Conta
[e] Extrato     [nu] Novo Usuário
[q] Sair
          
                              v.02          
=======================================   
""")
          
# criar usuário
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Já existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data nascimento (dd-mm-aaaa): ")
    endereco = input("informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

# criar conta
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado, fluxo de criação de conta encerrado!")

# listar contas
def listar_contas(conta):
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        # print(contas)
        print("=" * 25)
        print(textwrap.dedent(linha))


# Pesquisar usuário
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# depositar
def depositar(saldo, valor, extrato, /):
    
    valor = float(input("informe o valor do depósito:\nR$ "))
    
    # verifica se foi digitado valores negativos
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        input("\nAperte Enter para continuar...")
        limpar_tela()
        tela_deposito()
        print("""
Deposito realizado com sucesso!
        """)
        
    else:
        print("Operação falhou! O valor informado é inválido.")
        
    return saldo, extrato

# sacar
def sacar():
    global saldo,limite,extrato, numero_saque, LIMITE_SAQUE

    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque >= LIMITE_SAQUE

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite")

    elif excedeu_saque:
        print("Operação falhou! Número máximo de saques excedido.")    
#   Verifica se foi digitado valores negativos
    elif valor > 0:
        saldo -= valor
        extrato+= f"Saque: R$ {valor:.2f}\n"
        numero_saque += 1

    return saldo, extrato
                                
# extrato
def exibir_extrato():
    print("\n===============EXTRATO==================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"""\nSaldo:  R$ {saldo:.2f}""")
    print("========================================")

# MENSAGEM
# Saldação de encerramento do programa
def mensagem_final():
    print("""
Operação Finalizada!
    
Agradecemos sua visita,
tenha um excepcional dia.
          
    """)

# TELAS 

def limpar_tela():
    os.system('clear')

def tela_deposito():
    print("\n ============= DEPÓSITO ==============\n")

def tela_saque():
    print("\n ============== SAQUE ================\n")



# Funcionalidades do menu
while True:
   
    menu() # Iniciação do programa
    opcao = input("Digite uma opção: \n==> ")
    limpar_tela()
   
    # Chama o método depositar()
    if opcao == "d":
        tela_deposito()
        saldo, extrato = depositar(saldo, valor, extrato)     
        voltar = input("""
=====================================
                       
Deseja realizar outra operação? [s/n]\n==> """)
        # Verifica se o usuário deseja realizar outra operação
        if voltar == "s":
            limpar_tela()
        elif voltar == "n":
            opcao = "q"
            limpar_tela()
            mensagem_final()
            break
   
    # chama o método sacar
    elif opcao == "s":
        tela_saque()
        sacar()
        limpar_tela()
    
    # chama o método  exibir_extrado    
    elif  opcao == "e":
        exibir_extrato()

    # chama o método criar conta
    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    # chama o método que cria um novo usuário
    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "lc":
        listar_contas(contas) # ---->  ATENÇÃO <---- buscar a causa do erro
        
    # comando para encerrar a aplicação 
    elif opcao == "q":
        mensagem_final()
        break
    else:
        continue
        
       
    