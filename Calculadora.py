
# EJEMPLO FUNCIÓN DEF

def ejemplo_funcion(numero1, numero2):
    resultado = numero1 + numero2
    return resultado


# CALCULADORA BÁSICA CON FUNCIONES

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Error: No se puede calcular módulo por cero"
    return a % b


def calculadora():
    
    print("ingrese numero a : ", end="") 
    numero_a = int(input()) 
    
    print("ingrese numero b : ", end="")
    numero_b = int(input())  
    
    print("Ingrese el tipo de operación aritmética que desea hacer (suma,resta,multiplicacion,division,modulo) : ", end="")
   
    operacion =str(input()).strip()
    if operacion == 'suma':
        resultado = sumar(numero_a, numero_b)
    elif operacion == 'resta':
        resultado = restar(numero_a, numero_b)
    elif operacion == 'multiplicacion':
        resultado = multiplicar(numero_a, numero_b)
    elif operacion == 'division':
        resultado = dividir(numero_a, numero_b)
    elif operacion == 'modulo':
        resultado = modulo(numero_a, numero_b)
    else:
        resultado = "Error: Operación no válida"
    
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    calculadora()  