Listanumero=[]
ListaPares=[]
for i in range(10):
    numUsuario= int(input("ingrese su numeros: "))
    Listanumero.append(numUsuario)
    if numUsuario %2 == 0:
        ListaPares.append(numUsuario)
print(ListaPares)