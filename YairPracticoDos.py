print("Contar los pronombres en el texto compartido por la profesora lorena")
pronombres = [
    "yo", "tu", "el", "ella", "usted", "nosotros", "nosotras", "vosotros", "vosotras", 
    "ellos", "ellas", "ustedes", "me", "te", "se", "nos", "os", "lo", "la", "los", "las", 
    "le", "les", "mi", "tu", "su", "nuestro", "nuestra", "vuestro", "vuestra"]

def contar_pronombres(texto):
    palabras = texto.split()
    contador = 0
    for palabra in palabras:
        palabra = palabra.strip(",.!?¿¡")
        if palabra in pronombres:
            contador += 1
    return contador

texto = input("Ingresa un texto: ")
cantidad_pronombres = contar_pronombres(texto)
print(f"El texto contiene {cantidad_pronombres} pronombres.")