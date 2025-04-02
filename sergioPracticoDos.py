### Escribe un programa que identifique y cuente los pronombres de un texto y luego imprima la cantidad que contiene el texto. ###
## importo librerias ##
import os
import nltk
from rich import print
from nltk.tokenize import word_tokenize

## Declaro funcion para limpiar la consola##
def clear():
    os.system('cls')

clear()
print("    ### Contador de pronombres en Python ###")

## Declaro las listas con pronombres ##
pronombres_personales= ["yo", "me", "mí", "conmigo", "tú", "te", "ti", "contigo", "él", "ella", "usted", "lo", "la", "le", "se", "sí", "nosotros", "nosotras", "vosotros", "vosotras", "ellos", "ellas", "ustedes"]
pronombres_posesivos = ["mío", "mía", "míos", "mías", "tuyo", "tuya", "tuyos", "tuyas", "suyo", "suyos", "suyas", "nuestros", "nuestras", "vuestros", "vuestras", "suyos", "suyas"]
pronombres_demostrativos = ["este", "esta", "estos", "estas", "ese", "esa", "esos", "esas", "esto", "eso", "aquello"]
pronombres_interrogativos = ["quién", "quiénes", "qué", "cuál", "cuáles"]

pronombres_encontrados = {"Pronombres Posesivos": [], "Pronombres Personales": [], "Pronombres Demostrativos": [], "Pronombres Interrogativos": []}


## Pido al Usuario que ngrese un texto ##
texto = str(input("Ingrese su texto >> "))
palabras = nltk.word_tokenize(texto.lower()) # Tokeniso cada palabra del string, es decir les doy un valor 


for token in palabras:
    if token in pronombres_personales:
        pronombres_encontrados["Pronombres Personales"].append(token)
    if token in pronombres_posesivos:
        pronombres_encontrados["Pronombres Posesivos"].append(token)
    if token in pronombres_demostrativos:
        pronombres_encontrados["Pronombres Demostrativos"].append(token)
    if token in pronombres_interrogativos:
        pronombres_encontrados["Pronombres Interrogativos"].append(token)


print("Los pronombres encontrados son:: ")
print()

for clave, pronombres in pronombres_encontrados.items():
    print(f"{clave}:")
    for i, pronombre in enumerate(pronombres, start=1):
        if isinstance(pronombre, str):
            print(f"{i}. {pronombre}")
        else:
            print("No se encontraron mas") 
    print()

print()
print(texto)

 