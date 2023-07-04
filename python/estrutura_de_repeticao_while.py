opcao = -1

# exemplo de repetição com while
# while opcao != 0:
#     opcao = int(input("[1] Sacar \n[2] Extrado \n[0] Sair \n: "))

# if opcao == 1:
#     print("Sacando ...")
# elif opcao == 2:
#     print("Exibindo o extrado ...")


# exemplo de repetição com while/else 
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrado \n Sair \n: "))

if opcao == 1:
    print("Sacando ...")
elif opcao == 2:
    print("Exibindo o extrado ...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")