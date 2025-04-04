
print ("Ejercicio 1: Lista de números pares.")
print ("") #oara que quede mas prolijo

#Ejercicio 1: Lista de números pares.
#Escribe un programa que solicite al usuario ingresar 10 números y luego imprima una lista con los números pares ingresados.

print ("Hola!! Este es mi programa, vos podras ingresar solo 10 numeros y solo te devolvera los pares, pongamos lo a prueba!!")
print ("") 

numeros=[]

#range determina la cantidad de veces que se repita el bluce, q esta determinado por "cantidad_num"

for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))  # Solicita el número y lo agrega a la lista
    numeros.append(num) #ingresa en la lista vacia "numeros" el valor de num

#append es para agregar valores a listas

print(f"la lista de todos los números hasta ahora es: {numeros}") 

#chequeamos que los numeros se hayan guardado correctamente en la lista


pares=[] #lista de números vacia de pares, que ahora en el bucle determinaremos cuales son los números pares que iran aca

for num in numeros: #es un bucle que recorre la lista numeros

#num hace referencia que en cada iteración, toma el siguiente número de la lista y lo asigna a la variable num

    if num % 2 ==0: #si num dividido dos es igual a 0 se agrega a la lista pares 
      pares.append(num)
print(f"los numeros pares son: {pares}")