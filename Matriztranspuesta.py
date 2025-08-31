# MATRIZ TRANSPUESTA

def crear_matriz_transpuesta():
   
    while True:
        try:
            
            n = int(input("Escriba el parámetro n para definir el tamaño de la matriz cuadrada: "))
           
            if n > 0:
                break
            else:
                
                print("El tamaño de la matriz debe ser un número entero positivo. Inténtalo de nuevo.")
        except ValueError:
            
            print("Entrada no válida. Por favor, ingresa un número entero.")

    
    matriz = []

    for i in range(n):
       
        fila = []
        
        for j in range(n):
            
            while True:
                try:
                    
                    valor = int(input(f"Dime el dato en la fila {i + 1} y la columna {j + 1}: "))
                    
                    fila.append(valor)
                    
                    break
                except ValueError:
                    
                    print("Entrada no válida. Por favor, ingresa un número entero.")
       
        matriz.append(fila)

    
    print("Su matriz es:", matriz)

    transpuesta = []
    
    for i in range(n):
       
        fila_transpuesta = []
        for j in range(n):
          
            fila_transpuesta.append(matriz[j][i])
       
        transpuesta.append(fila_transpuesta)

   
    print("La transpuesta de la matriz es:", transpuesta)

crear_matriz_transpuesta()

