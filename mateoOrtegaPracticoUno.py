Listanumero=[]#lista vacia
ListaPares=[]#lista vacia
for i in range(10):#hace un for a un rango de 10 
    numUsuario= int(input("ingrese su numeros: "))
    Listanumero.append(numUsuario)#lleva los numeros ingresados a listanumero
    if numUsuario %2 == 0:#hace el calculo para que de pares
        ListaPares.append(numUsuario)#a esos pares los manda a la listapares
print(ListaPares)#imprime listapares