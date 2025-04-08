def contar_pronombres(texto):
    pronombres = ["él", "ella", "ellos", "ellas", "lo", "la", "los", "las", "usted", "nosotros", "nosotras", ]
    texto = texto.lower()  # eso se usa para que el texto seaa minuscula
    contador = 0

    # Contamos cuántas veces aparece cada pronombre en el texto
    for pronombre in pronombres:
        if pronombre in pronombres:  # Se sumar las veces que aparece el pronombre
         contador += 1
    return contador

texto = """Stéfano habita una vieja casa de barrio pobre. Él vive allí desde hace mucho tiempo. El humilde hogar es de tres piezas; dos, dan a la calle; la otra es de madera y cinc y recuadra con un patio lleno de viento. La casa tiene varias ventanas. La que está a la derecha lleva al zaguán oscuro; la de la izquierda a la otra sala. La humedad es tan antigua que ya no queda ese olor ácido y penetrante, sin embargo las huellas verdinegras perduran en las paredes y en los techos, los cuales, crujen al compás del viento. Stéfano no tuvo en su vida lo que deseaba, sin embargo, la carencia le ayudó a que él nunca se rindiera ante su destino. Lo único que le interesaba era lograr lo que soñaba."""

#la cantidad de pronombres es igual a contar prononmbres obviamentwwe del texto
cantidad_pronombres = contar_pronombres(texto)


print(f"El texto contiene {cantidad_pronombres} pronombres.")
