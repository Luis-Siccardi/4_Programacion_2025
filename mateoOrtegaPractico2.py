texto="Stéfano habita una vieja casa de barrio pobre. Él vive allí desde hace mucho tiempo. El humilde hogar es de tres piezas; dos, dan a la calle; la otra es de madera y cinc y recuadra con un patio lleno de viento. La casa tiene varias ventanas. La que está a la derecha lleva al zaguán oscuro; la de la izquierda a la otra sala. La humedad es tan antigua que ya no queda ese olor ácido y penetrante, sin embargo las huellas verdinegras perduran en las paredes y en los techos, los cuales, crujen al compás del viento. Stéfano no tuvo en su vida lo que deseaba, sin embargo, la carencia le ayudó a que él nunca se rindiera ante su destino. Lo único que le interesaba era lograr lo que soñaba."

pronombres=[
    "yo", "tú", "vos", "usted", "él", "ella", "nosotros", "nosotras", "vosotros", "vosotras", "ustedes", "ellos", "ellas", "me", "te", "se", "nos", "os", "lo", "la", "los", "las", "le", "les", "mí", "ti", "sí"
]#es una lista con todos los pronombres
palabras = texto.lower().replace(".","").replace(";","").replace(",","").split()#define la variable palabras y la pasa a texto en miuscula y remplaza los puntos y comas por nada y con el split agrega espacio a cada palabra

contador = 0#le da un valor a contador 
for palabra in palabras: #pasa palabra por palabras
    if palabra in pronombres:#recorre palabra en pronombres
        contador += 1 #contador suma los pronombres
print("cantidad de pronombres en el texto:",contador)