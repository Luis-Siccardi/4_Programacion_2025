print("Ingrese 10 numeros")

Impares = []
Pares = []

for i in range (10):
    numUsuario = int(input("ingrese su numeros:"))
    Impares.append(numUsuario)
    if numUsuario  %2==0:
        Pares.append(numUsuario)

print(Impares)
print(Pares)
