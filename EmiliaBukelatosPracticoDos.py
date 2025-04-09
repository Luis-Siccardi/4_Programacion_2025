# Texto proporcionado
texto = """Stéfano habita una vieja casa de barrio pobre. Él vive allí desde hace mucho tiempo. El humilde hogar es de tres piezas; dos, dan a la calle; la otra es de madera y cinc y recuadra con un patio lleno de viento. La casa tiene varias ventanas. La que está a la derecha lleva al zaguán oscuro; la de la izquierda a la otra sala. La humedad es tan antigua que ya no queda ese olor ácido y penetrante, sin embargo las huellas verdinegras perduran en las paredes y en los techos, los cuales, crujen al compás del viento. Stéfano no tuvo en su vida lo que deseaba, sin embargo, la carencia le ayudó a que él nunca se rindiera ante su destino. Lo único que le interesaba era lograr lo que soñaba."""

# Lista de pronombres personales comunes en español
pronombres = ["yo", "tú", "él", "ella", "nosotros", "nosotras", "vosotros", "vosotras", "ellos", "ellas", "me", "te", "se", "nos", "os", "le", "les", "lo", "los", "la", "las"]
palabras= texto.lowe().replace(".", "").replace(",","").replace(";","").split()

contador=0
for palabra in palabras:
    if palabra in pronombres:
        contador += 1

print("Cantidad de pronombres en el texto:"contador)