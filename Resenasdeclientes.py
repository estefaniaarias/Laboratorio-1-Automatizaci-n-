import string 

def procesar_resenas():
    resenas = [] 
    print("Por favor, ingrese al menos 3 reseñas. Para terminar, presione Enter sin escribir nada.")
    
    while True:
        resena_actual = input(f"Ingrese la reseña #{len(resenas) + 1}: ")
        
        if not resena_actual and len(resenas) >= 3:
            break
        
        elif not resena_actual and len(resenas) < 3:
            print(f"Debe ingresar al menos 3 reseñas. Lleva {len(resenas)}.")
       
        elif resena_actual:
            resenas.append(resena_actual)

    frecuencias = {} 
    signos_puntuacion = string.punctuation

    for resena in resenas:
        resena_procesada = resena.lower()
        
        for signo in signos_puntuacion:
            resena_procesada = resena_procesada.replace(signo, " ")
        
        palabras = resena_procesada.split()

        for palabra in palabras:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    lista_frecuencias = list(frecuencias.items())

    lista_frecuencias.sort(key=lambda item: item[1], reverse=True)
    
    print("\n--- Las 3 palabras más frecuentes son: ---")
   
    for palabra, frecuencia in lista_frecuencias[0:3]:

        print(f"'{palabra}': {frecuencia} veces")

procesar_resenas()