### Escribe un programa que solicite al usuario ingresar 10 números y 
### luego imprima una lista con los números pares ingresados.
import os

os.system('cls')

print("Ingrese 10 numeros al azar y le dire cuales son pares")

numerosPares = []
for i in range(10):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    if numero % 2 == 1:
        numerosPares.append(numero)

print(f"Los numeros pares son: {numerosPares}")