#define la funcion
def numPares():
  Numeros = []#crea la lista numeros

  for i in range(10):
    num = int(input("Ingrese un número: "))
    if num == 0:
        continue
        
    elif num % 2 == 0:#dice que si el resultado de la division es 0 es un numero par
        Numeros.append(num)

  print("numeros pares ingresados: ", Numeros)

numPares() 