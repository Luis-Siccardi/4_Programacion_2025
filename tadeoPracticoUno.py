listaNumeros = []
listaPares = []
print("numeros pares")
for i in range (10):
    numUsuario = int(input("ingrese 10 numeros"))
    listaNumeros.append(numUsuario)
    if numUsuario % 2 == 0:
        listaPares.append(numUsuario)
print(listaPares)