numeros = []
pares = []
for i in range (10):
    numUsuario=int(input("igrese sus numeros"))
    numeros.append(numUsuario)
    if numUsuario%2 == 0:
      pares.append(numUsuario)
print(f"los nums pares son: {pares}") ##la f habilita las llaves