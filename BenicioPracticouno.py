print("bienvenido al contador de pares")
listanumeros=[]
listapares=[]
for i in range(10):
    numerosingresados=int(input("ingrese un numero"))
    listanumeros.append(numerosingresados)
    if numerosingresados % 2 ==0:
        listapares.append(numerosingresados)

print(listapares)