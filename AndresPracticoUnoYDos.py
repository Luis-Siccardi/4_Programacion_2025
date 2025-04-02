'''
Trabajo práctico 1 y 2
Luis Alberto Siccardi


Luego del repaso realizado la semana pasada, tenés que resolver los dos ejercicios planteados a continuación, ambos deben entregarse por GitHub y ser defendidos oralmente. 
Cada trabajo debe ser guardado en un archivo que se llame de la siguiente forma "nombrePracticoUno.py" y "nombrePracticoDos.py" usando la 

notación de camello.
Fecha de entrega: 02/04/25

Ejercicio 1: Lista de números pares.
Escribe un programa que solicite al usuario ingresar 10 números y luego imprima una lista con los números pares ingresados.

Ejercicio 2: Contar pronombres en el texto compartido por la Profesora Lorena.
Escribe un programa que identifique y cuente los pronombres de un texto y luego imprima la cantidad que contiene el texto.
'''

def contarPares(lista):
    resultado=[]
    for i in range ( len(lista) ):
        if i%2==0:
            print(lista[i])
            resultado.append(i)
    return resultado

lista=[]
for i in range(10): # <-- esoeso
    numero=int(input(f'{i+1}:'))
    lista.append(numero)
print(lista)

print(contarPares(lista))

texto='buenas tardes yo bien.'

hola=texto.split(' ')

pronombres=['yo','tu','el','esta']

print(hola)

textoFinal=''

for i in hola:
    if i in pronombres:
        textoFinal = f'{textoFinal} >>{i}<<'
    else:
        textoFinal = f'{textoFinal} {i}'

print(textoFinal)
