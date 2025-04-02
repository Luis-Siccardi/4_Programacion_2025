#lista de numeros pares

print ("lista de numeros pares")

listaNumeros =[]
listaPares=[]

for i in range (10):
  
  numerosIngresados = int(input("ingrese un numero"))
  if numerosIngresados % 2 == 0:
      listaPares.append(numerosIngresados)

print(listaPares)



