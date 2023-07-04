while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break           # parar a execução

    if numero % 2 == 0:
        continue        # pular na execução
    
    print(numero)