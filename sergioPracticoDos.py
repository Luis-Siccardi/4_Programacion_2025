import nltk, os

def clear():
    os.system('cls')

clear()
print("    ### Contador de pronombres en Python ###")

pronombres = ["yo", "tu", "el", "ella", "usted", "nosotros", "nosotras", "vosotros", "ellos", "ellas", "ustedes", "me", "te", "lo", "la", "nos", "os", "los", "las", "le", "les", "se"]
texto = str(input("Ingrese su texto >> "))
palabras = nltk.word_tokenize(texto.lower())

pronombres_encontrados = [pronombre for pronombre in pronombres if pronombre in pronombres]
print(palabras)