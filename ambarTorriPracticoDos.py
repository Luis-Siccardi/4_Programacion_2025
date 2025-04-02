#pronombres, ejercicio 2
#función para contarb pronombres
def contar_pronombres(texto):
    pronombres = {"yo", "tú", "vos", "usted", "él", "ella", "nosotros", "nosotras", "vosotros", "vosotras", "ustedes", "ellos", "ellas", "me", "te", "se", "nos", "os", "lo", "la", "los", "las", "le", "les", "mí", "ti", "sí"}
#covertir el texto a miniscula y dividir cada palabra segun los espacio
    palabras = texto.lower().split()
#sacamos los signos de puntuacion (.,!?) para ver si las palabras coinsiden a los pronombres, y recorremos la lista de palabras, si algun pronombre de la lista esta en el texto se sumara 1 al contador 
    conteo = sum(1 for palabra in palabras if palabra.strip (".,!?")in pronombres)
#se imprime la cantidad de pronombrers
    print(f"el texto contiene {conteo}pronombres.")
    #devuelve la cantidad de pronombres
    return conteo
texto = "Para comenzar, podemos postular que toda la literatura es ficción, lo cual nos permitiría diferenciar aquellos textos que presentan un hecho real de otros en los cuales ese hecho solo es producto de la imaginación. Pero también es cierto que existen obras basadas en hechos reales que son con- sideradas literarias, tal es el caso del Diario de Ana Frank, en el que una niña judía narra sus experiencias durante la ocupación nazi en Ámsterdam, en el contexto de la Segunda Guerra Mundial. A este argumento podríamos oponer el siguiente: el autor, en este caso Ana Frank, solo tomó hechos su- cedidos en la realidad y los elaboró de acuerdo con su visión del mundo, sus ideas, sus pensamientos. El Diario de Ana Frank es literatura y, por lo tanto. la discusión no se cierra aquí: además del carácter ficcional de una obra literaria, hay otros elementos que debemos tener en cuenta para definir qué es o no es literatura."
contar_pronombres(texto)