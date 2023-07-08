numPedidos = int(input("Digite o número de pedidos: "))

for i in range(1, numPedidos + 1):
    prato = input("Informe o prato desejado: ")
    calorias = int(input("Informe a quantidade de calorias: "))
    ehVegano = False


    
    opcao_vegano = input("eh vegando: [s] sim [n] nao:\n")
    
    if opcao_vegano.lower() == "s":
      ehVegano = True
    
      print(f"Pedido {i}: {prato} (Vegano) - {calorias} calorias")
    
    elif opcao_vegano.lower() == "n":
      ehVegano = False
      print(f"Pedido {i}: {prato} (Nao-vegano) - {calorias} calorias")