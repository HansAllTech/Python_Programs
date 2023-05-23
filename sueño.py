def calcular_inicio_fin_sueno(horas_sueno):
    inicio = min(horas_sueno)
    fin = max(horas_sueno)
    return inicio, fin

def calcular_promedio_sueno(horas_sueno):
    total_horas = sum(horas_sueno)
    promedio = total_horas / len(horas_sueno)
    return promedio

# Función para ingresar las horas de sueño
def ingresar_horas_sueno():
    horas_sueno = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias_semana:
        while True:
            try:
                horas = float(input(f"Ingrese las horas de sueño para el día {dia}: "))
                horas_sueno.append(horas)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido.")

    return horas_sueno

horas_sueno = ingresar_horas_sueno()
inicio, fin = calcular_inicio_fin_sueno(horas_sueno)
promedio = calcular_promedio_sueno(horas_sueno)

print("Total de horas de sueño:", sum(horas_sueno))
print("Hora de inicio:", inicio)
print("Hora de fin:", fin)
print("Promedio de horas dormidas por día:", promedio)
