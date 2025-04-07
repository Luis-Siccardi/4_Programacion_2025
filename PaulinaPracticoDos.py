print("Este programa cuenta cuántos pronombres hay en un texto")

texto = "Stéfano habita una vieja casa de barrio pobre. Él vive allí desde hace mucho tiempo. El humilde hogar es de tres piezas; dos, dan a la calle; la otra es de madera y cinc y recuadra con un patio lleno de viento. La casa tiene varias ventanas. La que está a la derecha lleva al zaguán oscuro; la de la izquierda a la otra sala. La humedad es tan antigua que ya no queda ese olor ácido y penetrante, sin embargo las huellas verdinegras perduran en las paredes y en los techos, los cuales, crujen al compás del viento. Stéfano no tuvo en su vida lo que deseaba, sin embargo, la carencia le ayudó a que él nunca se rindiera ante su destino. Lo único que le interesaba era lograr lo que soñaba."

pronombres = ['yo', 'tú','ella', 'él', 'nosotros', 'nosotras', 'vodotros',
                  'vosotras', 'ellos', 'ellas', 'me', 'te', 'se', 'nos', 'os',
                  'mi', 'mio', 'mia', 'míos', 'mías', 'tu', 'tuyo', 'tuya',
                  'tuyas', 'tuyos', 'su', 'suyo', 'suya', 'suyas', 'suyos',
                  'le', 'les', 'lo', 'la', 'los', 'las'] #lista de palabras que son pronombres

palabras = texto.lower().replace(".", "").replace(";", "").replace(",", "").split() #evita los signos de puntuación
print(pronombres)

contador = 0 #contar cuantas palabras estan en la lista de pronombres
for palabra in palabras:
    if palabra in pronombres:
        contador += 1

print("La cantidad de palabras es:", contador)