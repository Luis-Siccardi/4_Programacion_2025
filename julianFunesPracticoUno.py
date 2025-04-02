print("este es un programa que te dice que numeros que son pares")

#define mi poderosa funcion y lista

def numerosPares():
    Numeros =[]
#ingrese 10 numeros distintos
    for i in range(10):
        num = int(input("igresar su numero: "))
        if num ==0:
            continue
#separa los multiplo de 2 para designar los pares
        elif num%2==0:
            Numeros.append(num)
#muestra en la termial los numeros pares
    print("los numeros pares son:" ,Numeros)

numerosPares()