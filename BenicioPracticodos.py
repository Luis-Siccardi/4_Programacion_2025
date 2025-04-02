texto="Stéfano habita una vieja casa de barrio pobre. Él vive allí desde hace mucho tiempo. El humilde hogar es de tres piezas; dos, dan a la calle; la otra es de madera y cinc y recuadra con un patio lleno de viento. La casa tiene varias ventanas. La que está a la derecha lleva al zaguán oscuro; la de la izquierda a la otra sala. La humedad es tan antigua que ya no queda ese olor ácido y penetrante, sin embargo las huellas verdinegras perduran en las paredes y en los techos, los cuales, crujen al compás del viento. Stéfano no tuvo en su vida lo que deseaba, sin embargo, la carencia le ayudó a que él nunca se rindiera ante su destino. Lo único que le interesaba era lograr lo que soñaba."
texto=texto.lower()
pronombres=["yo", "tú", "él", "ella", "usted", "ustedes", "nosotros", "nosotras", "ellos", "ellas"]
contador=0
for pronombre in pronombres:
    contador += texto.count(pronombre)
print(f"el texto contiene {contador} pronombres.")