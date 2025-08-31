# SUMA DE MATRICES

import random 

def sumar_matrices():
    while True:
        try:
            
            n = int(input("Escriba la dimensión (n) de las matrices cuadradas: "))
            if n > 0:
                break
            else:
                print("La dimensión debe ser un número entero positivo. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    matriz_aleatoria = []
    matriz_usuario = []
    matriz_suma = []

    for i in range(n):
        fila_aleatoria = []
        fila_usuario = []
        fila_suma = []

        for j in range(n):
            num_aleatorio = random.randint(1, 100)
            fila_aleatoria.append(num_aleatorio)
            
            while True:
                try:
                    valor_usuario = int(input(f"Ingresa el valor para la matriz de usuario en la fila {i + 1} y columna {j + 1}: "))
                    fila_usuario.append(valor_usuario)
                    break 
                except ValueError:
                    print("Entrada no válida. Por favor, ingresa un número entero.")

            suma_elemento = fila_aleatoria[j] + fila_usuario[j]
            fila_suma.append(suma_elemento)

        matriz_aleatoria.append(fila_aleatoria)
        matriz_usuario.append(fila_usuario)
        matriz_suma.append(fila_suma)

    print("\n--- Resultado de la Operación ---")
    print("Matriz aleatoria generada:")
    for fila in matriz_aleatoria:
        print(fila)
    
    print("\nMatriz ingresada por el usuario:")
    for fila in matriz_usuario:
        print(fila)

    print("\nMatriz resultante (suma):")
    for fila in matriz_suma:
        print(fila)

sumar_matrices()