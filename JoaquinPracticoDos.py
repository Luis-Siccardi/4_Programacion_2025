pronombres = [
    "yo", "tú", "él", "ella", "usted", "nosotros", "nosotras", "vosotros", "vosotras", 
    "ellos", "ellas", "ustedes", "me", "te", "se", "nos", "os", "lo", "la", "los", "las", 
    "le", "les", "mi", "tu", "su", "nuestro", "nuestra", "vuestro", "vuestra"
]#crea una lista con todos los pronombres

def contar_pronombres(texto):
    palabras = texto.split()#deja de identificar todo como texto sino como palabras separadas
    contador = 0
    for palabra in palabras:
        palabra = palabra.strip(",.!?¿¡")#elimina todos los caracteres que esten dentro del parentecis
        if palabra in pronombres:
            contador += 1
    return contador
#Le pide al usuario que ingrese el texto
texto = input("Ingresa un texto: ")
cantidad_pronombres = contar_pronombres(texto)
print(f"El texto contiene {cantidad_pronombres} pronombres.")

