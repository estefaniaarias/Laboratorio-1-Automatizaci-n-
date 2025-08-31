# ESTACIÓN CLIMÁTICA

def determinar_estacion_climatica():
    
    dias_por_mes = {
        'enero': 31,
        'febrero': 29,  
        'marzo': 31,
        'abril': 30,
        'mayo': 31,
        'junio': 30,
        'julio': 31,
        'agosto': 31,
        'septiembre': 30,
        'octubre': 31,
        'noviembre': 30,
        'diciembre': 31
    }

    while True:
        mes = input("Ingrese el nombre del mes: ").lower()
        try:
            dia = int(input("Ingrese el día que desea consultar: "))
        except ValueError:
          
            print("Entrada no válida para el día. Por favor, ingrese un número.")
            continue 
        
        if mes not in dias_por_mes:
            print("Mes no válido. Por favor, ingrese un mes correcto.")
            continue

       
        max_dias = dias_por_mes[mes]

        if 1 <= dia <= max_dias:
            break
        else:
            print(f"Fecha imposible. El mes de {mes.capitalize()} solo tiene entre 1 y {max_dias} días.")
            print("Por favor, ajuste la fecha y vuelva a intentarlo.")

    # Verano: del 21 de Junio al 20 de Septiembre.
    if (mes == 'junio' and dia >= 21) or \
       (mes == 'julio') or \
       (mes == 'agosto') or \
       (mes == 'septiembre' and dia <= 20):
        estacion = "verano"
    
    # Otoño: del 21 de Septiembre al 20 de Diciembre.
    elif (mes == 'septiembre' and dia >= 21) or \
         (mes == 'octubre') or \
         (mes == 'noviembre') or \
         (mes == 'diciembre' and dia <= 20):
        estacion = "otoño"

    # Invierno: del 21 de Diciembre al 20 de Marzo.
    elif (mes == 'diciembre' and dia >= 21) or \
         (mes == 'enero') or \
         (mes == 'febrero') or \
         (mes == 'marzo' and dia <= 20):
        estacion = "invierno"

    # Primavera: del 21 de Marzo al 20 de Junio.
    elif (mes == 'marzo' and dia >= 21) or \
         (mes == 'abril') or \
         (mes == 'mayo') or \
         (mes == 'junio' and dia <= 20):
        estacion = "primavera"
    else:
        estacion = "estación no definida"
    print(f"Para el día {dia} del mes {mes.capitalize()} estaríamos en {estacion}")

determinar_estacion_climatica()