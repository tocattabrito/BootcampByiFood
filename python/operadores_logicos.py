
saldo = 1000
saque = 200
limite = 100

print(saldo >= saque)
# >>> True
print(saque <= limite)
# >>> False

print('Operador and (E)')
print(saldo >= saque and saque <= limite)
# >>> False

print('Operador or (OU)')
print(saldo >= saque or saque <= limite)
# >>> True

print("Operador not (Negação)")
print(not 1000 > 1500)
# >>> True

contatos_emergencia = [] # lista vazia
print(not contatos_emergencia)
# >>> True

print(not "saque 1500;")
# >>> False

print(not "")
# >>> True

# Parênteses
# podem ser usados para agrupar expressões em operadores lógicos.
# O resultado da avaliação de uma subexpressão entre parênteses é considerado antes
# do restante dos operandos, mesmo que estejam separados por outros operadores:

saldo = 1000
saque = 250
limite = 200
conta_especial = True

saldo >= saque and saque <= limite or conta_especial and saldo >= saque
# >>> True

(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saldo)
# >>> True

