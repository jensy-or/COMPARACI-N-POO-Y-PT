# Función para validar número
def es_numero(valor):
    try:
        float(valor)
        return True
    except:
        return False

# Función principal de ingreso de datos
def ingresar_temperaturas():
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temps = []
    
    i = 0
    while i < 7:
        temp = input(f"Ingrese temperatura para el {dias[i]}: ")
        
        if es_numero(temp):
            temps.append(float(temp))
            i += 1
        else:
            print("¡Error! Debe ingresar solo números")
    
    return temps

# Función para calcular promedio
def calcular_promedio(temps):
    total = 0
    contador = 0
    
    while contador < len(temps):
        total += temps[contador]
        contador += 1
    
    return total / len(temps)

# Programa principal
def main():
    print("=== REGISTRO MENSUAL DE TEMPERATURAS ===")
    print("Ingrese datos para 4 semanas\n")
    
    # Variables para almacenar todas las temperaturas
    todas_temps = []
    semana_actual = 1
    
    while semana_actual <= 4:
        print(f"\nSEMANA {semana_actual}")
        temps_semana = ingresar_temperaturas()
        promedio = calcular_promedio(temps_semana)
        
        print(f"\nPromedio semana {semana_actual}: {promedio:.1f}°C")
        
        # Agregar temperaturas al registro mensual
        for temp in temps_semana:
            todas_temps.append(temp)
        
        semana_actual += 1
    
    # Calcular promedio mensual
    if len(todas_temps) > 0:
        prom_mensual = calcular_promedio(todas_temps)
        print("\n=== RESUMEN MENSUAL ===")
        print(f"Promedio mensual: {prom_mensual:.1f}°C")
    else:
        print("\nNo se ingresaron datos")

# Iniciar programa
main()