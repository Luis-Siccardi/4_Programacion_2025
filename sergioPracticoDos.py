### Escribe un programa que identifique y cuente los pronombres de un texto y luego imprima la cantidad que contiene el texto. ###
## importo librerias ##
import os
import nltk
from rich import print
from nltk.tokenize import word_tokenize
import re

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
pronombres_en_texto = []
pronombre_repetidos = {}

## Pido al Usuario que ngrese un texto ##
texto = str(input("Ingrese su texto >> "))

### TEXTO PEDIDO POR LA ACTIVIDAD ###
texto_lengua = ("Stéfano habita una vieja casa de barrio pobre. Él vive allí desde hace mucho tiempo. El humilde hogar es de tres piezas; dos, dan a la calle; la otra es de madera y cinc y recuadra con un patio lleno de viento. La casa tiene varias ventanas. La que está a la derecha lleva al zaguán oscuro; la de la izquierda a la otra sala. La humedad es tan antigua que ya no queda ese olor ácido y penetrante, sin embargo las huellas verdinegras perduran en las paredes y en los techos, los cuales, rujen al compás del viento. Stéfano no tuvo en su vida lo que deseaba, sin embargo, la carencia le ayudó a que él nunca se rindiera ante su destino. Lo único que le interesaba era lograr lo que soñaba.")


palabras = nltk.word_tokenize(texto_lengua.lower()) # Tokeniso cada palabra del string, es decir les doy un valor 


for token in palabras:
    if token in pronombres_personales:
        pronombres_encontrados["Pronombres Personales"].append(token)
    if token in pronombres_posesivos:
        pronombres_encontrados["Pronombres Posesivos"].append(token)
    if token in pronombres_demostrativos:
        pronombres_encontrados["Pronombres Demostrativos"].append(token)
    if token in pronombres_interrogativos:
        pronombres_encontrados["Pronombres Interrogativos"].append(token)


for clave, valores in pronombres_encontrados.items():
    pronombres_encontrados[clave] = list(set(valores))

print("Los pronombres encontrados son: ")
print()

for clave, pronombres in pronombres_encontrados.items():
    print(f"{clave}:")
    for i, pronombre in enumerate(pronombres, start=1):
        if isinstance(pronombre, str):
            print(f"{i}. {pronombre}")
            pronombres_en_texto.append(pronombre)
        else:
            print("No se encontraron mas") 
    print()

print()
print("Ahora marcare los pronombres encontrados en el texto")

for pronombre in pronombres_en_texto:
    texto_lengua = re.sub(r'\b(' + pronombre + r'|'+ pronombre.capitalize() + r')\b',lambda x: '[' + x.group(0) + ']', texto_lengua, flags=re.IGNORECASE)

print(texto_lengua)