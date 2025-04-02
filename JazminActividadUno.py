#primero creo las listas que voy a usar
listaNumeros=[]
numerosPares=[]

#el bucle for repite la acción de pedirle al usuario que ingrese un número 10 veces
#y lo guarda en la variable numUsuario
for i in range(10):
  numUsuario=(int(input("Ingrese un número")))
  listaNumeros.append(numUsuario)    #agrega los numeros de numUsuario a la lista

for numUsuario in listaNumeros: 
  if numUsuario % 2 == 0:           #si el número da 0 se agrega a la lista 
    numerosPares.append(numUsuario) #numerosPares y dsp se imprimen
print(numerosPares)
