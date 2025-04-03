print ("lista de numeros pares")
numeros = []
pares = []

for i in range (10):
    usuario = int(input("Ingrese un numero:"))
    numeros.append(usuario)
    if usuario%2 == 0:
        pares.append(usuario)

print(f"Lista completa: {numeros}")
print(f"Lista de pares: {pares}")