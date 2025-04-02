#Ejercicio 1: Lista de números pares.
#Escribe un programa que solicite al usuario ingresar 10 números y luego imprima una lista con los números pares ingresados.

print("ingrese 10 numeros y te dire cuales son pares")

listnumeros = []
listpares = []

#rage=el rango que le das y se utiliza con el for normalmente

for i in range(10):
    num=int(input("ingrese un numero:"))
    listnumeros.append(num)

  
    if num%2 == 0:
     listpares.append(num)
print(listpares)
