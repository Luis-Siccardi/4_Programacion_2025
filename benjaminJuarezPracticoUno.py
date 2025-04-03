print("ingrese 10 numeros y se imprimiran los pares")

listanumeros = []
listaPares = []

for i in range (10):
    numUsuario = int(input("ingrese sunumero: "))
    listanumeros.append(numUsuario)
    if numUsuario % 2 == 0:
        listaPares.append(numUsuario)

print(listaPares)
print("esa es la lista de numeros pares")