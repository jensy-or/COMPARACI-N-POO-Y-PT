class SemanaTemperaturas:
    def __init__(self, numero_semana):
        self.numero = numero_semana
        self.temperaturas = []
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    
    def ingresar_datos(self):
        print(f"\nSemana {self.numero}:")
        for dia in self.dias:
            while True:
                valor = input(f"Ingrese temperatura para {dia}: ")
                if self._es_numero(valor):
                    self.temperaturas.append(float(valor))
                    break
                else:
                    print("¡Error! Solo se permiten números")
    
    def calcular_promedio(self):
        total = 0
        for temp in self.temperaturas:
            total += temp
        return total / len(self.temperaturas)
    
    def _es_numero(self, valor):
        # Método privado para validar
        return valor.replace('.', '', 1).isdigit()

class MesTemperaturas:
    def __init__(self):
        self.semanas = []
    
    def agregar_semana(self, semana):
        self.semanas.append(semana)
    
    def calcular_promedio_mensual(self):
        total = 0
        contador = 0
        for semana in self.semanas:
            for temp in semana.temperaturas:
                total += temp
                contador += 1
        return total / contador if contador > 0 else 0

def main():
    print("=== REGISTRO MENSUAL DE TEMPERATURAS ===")
    
    mes = MesTemperaturas()
    
    for semana_num in range(1, 5):
        semana = SemanaTemperaturas(semana_num)
        semana.ingresar_datos()
        promedio = semana.calcular_promedio()
        print(f"Promedio semana {semana_num}: {promedio:.1f}°C")
        mes.agregar_semana(semana)
    
    print("\n=== RESUMEN MENSUAL ===")
    print(f"Promedio mensual: {mes.calcular_promedio_mensual():.1f}°C")

if __name__ == "__main__":
    main()