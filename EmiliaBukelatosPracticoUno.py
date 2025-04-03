# Solicitar al usuario que ingrese 10 números
print("Hola! Ingresa 10 numeros y este programa te dira cuales son los pares")
numeros = []
for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

# Filtrar los números pares
numeros_pares = [num for num in numeros if num % 2 == 0]

# Imprimir la lista de números pares
print("Números pares ingresados:", numeros_pares)