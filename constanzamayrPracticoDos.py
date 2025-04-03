print ("Ejercicio 2: Contar pronombres")
print ("                                    ") #para que quede mas prolijo
print ("error de prueba")
#Ejercicio 2: Contar pronombres en el texto compartido por la Profesora Lorena.

#Escribe un programa que identifique y cuente los pronombres de un texto y luego imprima la cantidad que contiene el texto.

print ("Vamos a identificar los ponombres en en siguiente texto!!")
print ("                                    ")

texto='''Stéfano habita una vieja casa de barrio pobre. Él vive allí desde hace mucho tiempo. El humilde hogar es de tres piezas; dos, dan a la calle; la otra es de madera y cinc y recuadra con un patio lleno de viento. La casa tiene varias ventanas. La que está a la derecha lleva al zaguán oscuro; la de la izquierda a la otra sala. La humedad es tan antigua que ya no queda ese olor ácido y penetrante, sin embargo las huellas verdinegras perduran en las paredes y en los techos, los cuales, crujen al compás del viento. Stéfano no tuvo en su vida lo que deseaba, sin embargo, la carencia le ayudó a que él nunca se rindiera ante su destino. Lo único que le interesaba era lograr lo que soñaba.'''

print (texto)
print ("                                    ")

pronombres= ['yo', 'tú', 'él', 'ella', 'usted', 'nosotros', 'nosotras', 'vosotros', 'vosotras', 'ellos', 'ellas', 'ustedes', 'me', 'te', 'lo', 'la', 'nos', 'os', 'los', 'las', 'le', 'se', 'mi', 'mía', 'mío', 'mía', 'nuestro', 'nuestra', 'nuestros', 'nuestras', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya', 'suyos', 'suyas', 'este', 'esta', 'estos', 'estas', 'ese', 'esa', 'esos', 'esas', 'aquel', 'aquella', 'aquellos', 'aquellas', 'algo', 'alguien', 'alguno', 'alguna', 'algunos', 'algunas', 'nadie', 'ninguno', 'ninguna', 'todos', 'todas', 'mucho', 'mucha', 'muchos', 'muchas', 'poco', 'poca', 'pocos', 'pocas', 'varios', 'varias', 'cualquiera', 'bastante', 'demasiado', 'menos', 'cada', 'ningún', 'ninguna', 'que', 'cual', 'quienes', 'cuyo', 'cuya', 'cuyos', 'cuyas', 'lo que', 'lo cual', 'qué', 'cuál', 'cuáles', 'quién', 'quiénes', 'cuánto', 'cuánta', 'cuántos', 'cuántas', 'cómo', 'dónde', 'cuándo', 'por qué', 'se']

    # Dividir el texto en palabras

palabras = texto.lower().split()

    #paréntesis indican que estás llamando a un método o función
    #lower=todo a minuscula 
    #split=separa las palabras

    # Contador de pronombres encontrados

contador_pronombres = 0

    # Recorrer el texto y contar los pronombres
for i in palabras:
    if i in pronombres:
        contador_pronombres += 1

print(f"El texto contiene {contador_pronombres} pronombres.")