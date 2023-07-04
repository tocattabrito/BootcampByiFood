# o código remove as vogais do texto digitado

# exemplo utilizando interável
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print() # adicionar uma quebra de linha



# exemplo utilizando a função built-in range
for numero in range(0, 11):
    print(numero, end=" ")

print("\n")

# exibindo a tabuada de 5
for numero in range(0, 51, 5):
    print(numero, end=" ")