def reconocer_pronombres(texto):
    pronombres = ["yo", "mí", "me", "conmigo", "nosotros", "nosotras", "nos", "tú", "vos", "usted", "te", "le", "vosotros",
                  "vosotras", "ustedes","os","les", "él", "ella","ello","le", "la","lo","se","sí","ellos","ellas","les","los",
                  "las","se","sí","consigo", "mío", "mía", "nuestro", "nuestra","míos","mías","nuestros","nuestras","tuyo","tuya",
                  "vuestro","vuestra","suyo", "suya","tuyos", "tuyas","vuestros","vuestras","suyo","suya","suyo","suyos","suyas",
                  "este","ese","aquel","estos","esos","aquellos","esta",
                  "esa", "aquella", "estas", "esas", "aquellas","esto","eso","aquello","quien","que","quienes","que","el que",
                  "el cual","la que","la cual","los que","los cuales","las que","las cuales","cuyo","cuya","cuyos","cuyas","cuanto",
                  "cuanta","cuantos","cuantas","qué","quién",
                  "cuál","cuánto","cuánta","qué","quiénes", "cuáles", "cuántos", "cuántas", "bastante", "quienquiera", "cualquiera",
                  "alguno", "todo", "tanto", "poco", "demasiado", "otro", "mucho", "ninguno", "alguna", "toda", "tanta", "poca", 
                  "demasiada","otra", "mucha", "ninguna", "bastantes", "quienesquiera", "cualesquiera", "algunos", "todos", "tantos",
                  "pocos", "demasiados", "otros", "muchos", "varios", "algunas", "todas", "tantas", "pocas", "demasiadas", "otras",
                  "muchas","varias", "alguien", "algo", "más", "menos", "nadie", "nada", "cada"]

    palabras = texto.split()  # Dividir el texto en palabras

    contador_pronombres = {}  # Diccionario para almacenar los pronombres y sus cantidades
    for palabra in palabras:
        if palabra in pronombres:
            if palabra in contador_pronombres:
                contador_pronombres[palabra] += 1
            else:
                contador_pronombres[palabra] = 1

    return contador_pronombres

# Texto de ejemplo
texto = """
Stéfano habita una vieja casa de barrio pobre. Él vive allí desde hace mucho tiempo. El humilde hogar es de tres piezas; dos, dan a la calle; la otra es de madera y cinc y recuadra con un patio lleno de viento. La casa tiene varias ventanas. La que está a la derecha lleva al zaguán oscuro; la de la izquierda a la otra sala. La humedad es tan antigua que ya no queda ese olor ácido y penetrante, sin embargo las huellas verdinegras perduran en las paredes y en los techos, los cuales, crujen al compás del viento. Stéfano no tuvo en su vida lo que deseaba, sin embargo, la carencia le ayudó a que él nunca se rindiera ante su destino. Lo único que le interesaba era lograr lo que soñaba.
"""

# Contar los pronombres en el texto
resultado = reconocer_pronombres(texto)

for pronombre, cantidad in resultado.items():
    print(f"{pronombre} : {cantidad}")

# Imprimir la cantidad total de pronombres
total = sum(resultado.values())
print(f"Cantidad total de pronombres: {total}")
