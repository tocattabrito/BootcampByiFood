# import
import os


# Variáveis
saldo = 0
limite = 500
extrato = ""
valor = 0
# valor_depositado = 0
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

# Telas     
def tela_deposito():
    print("\n ============= DEPÓSITO ==============\n")

def tela_saque():
    print("\n ============ SAQUE ================\n")

# def tela_extrato():
#     print("\n ============ DEPOSITO ================\n")



   

          
 

# Funções:

# limpar tela
def limpar_tela():
    os.system('clear')

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
# menu()

# saldo, extrato = depositar(saldo, valor, extrato)
# sacar()
# exibir_extrato()
# mensagem_final()

while True:
    # codição de parada do laço while que verifica a opção escolhida
    # teste = (input("Uma opção: "))
    menu() # Iniciação do programa
    opcao = input("Digite uma opção: \n==> ")
    limpar_tela()
    if opcao == "d":
        tela_deposito()
        saldo, extrato = depositar(saldo, valor, extrato)
        
        voltar = input("""
=====================================
                       
Deseja realizar outra operação? [s/n]\n==> """)
        if voltar == "s":
            limpar_tela()
        elif voltar == "n":
            opcao = "q"
            limpar_tela()
            mensagem_final()
            break
            
    elif opcao == "s":
        tela_saque()
        sacar()
        limpar_tela()
        
    elif  opcao == "e":
        exibir_extrato()
        

 # comando para encerrar a aplicação 
    elif opcao == "q":
        mensagem_final()
        break
    else:
        continue
        
       
    