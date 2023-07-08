# Variáveis
saldo = 0
limite = 500
extrato = ""
valor_depositado = 0
numero_saque = 0
LIMITE_SAQUE = 3



# menu
def menu():
    print("""
======== STB-SISTEMA BANCÁRIO =========         

Menu
          
[d] Depósito
[s] Saque
[e] Extrato
[q] Sair
          
                              v.02          
=======================================   
""")
    input("Digite uma opção: \n==> ")

  
# while True:
#     opcao = menu()

#     if opcao == "d":
#         valor_depositado = float(input("Informe o valor do depósito:"))
#         saldo, extrato = depositar(saldo, valor_depositado, extrato)
    
#     elif opcao == "q":
#         break
#     else:
#         print("")


# Funções:
# depositar
def depositar(saldo, valor, extrato, /):
    
    valor = float(input("informe o valor do depósito: "))
    # verifica se foi digitado valores negativos
    if  valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
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

    return valor
                                
# extrato
def exibir_extrato():
    print("\n===============EXTRATO==================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("========================================")

# Saldação de encerramento do programa
def mensagem_final():
    print("""
Operação Finalizada!
    
Agradecemos sua visita,
tenha um excepcional dia.
          
    """)

# Chamar os métodos
menu()
saldo, extrato = depositar(saldo, valor_depositado, extrato)
sacar()
exibir_extrato()
mensagem_final()


