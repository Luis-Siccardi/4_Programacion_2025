#Contar pronombres en el texto compartido por la Profesora Lorena.
#escribe un programa que identifique y cuente los pronombres de un texto
#y luego imprima la cantidad que contiene el texto.


print("Este programa cuenta cuántos pronombres hay en un texto")

def contar_pronombres(texto):
    # Lista de palabras que son pronombres
    pronombres = ["yo", "tú", "él", "ella", "nosotros", "nosotras", "vosotros", 
                  "vosotras", "ellos", "ellas", "me", "te", "se", "nos", "os", 
                  "mi", "mío", "mía", "míos", "mías", "tu", "tuyo", "tuya", 
                  "tuyos", "tuyas", "su", "suyo", "suya", "suyos", "suyas", 
                  "le", "les", "lo", "la", "los", "las"]
    
    # deja de ver el texto como texto y lo ve como palabras
    palabras = texto.split()
    
    # Contar cuántas palabras están en la lista de pronombres
    contador = 0
    for palabra in palabras:
        if palabra in pronombres:
            contador += 1
    
    return contador

# Pedir al usuario que escriba un texto
texto = input("Escribe un texto:" )


# Contar los pronombres y mostrar el resultado
cantidad = contar_pronombres(texto)
print("El texto tiene", cantidad, "pronombres.")