def calcular_costo_por_hora(total_horas, costo_proyecto):
    costo_por_hora = costo_proyecto / total_horas
    return costo_por_hora

total_horas = int(input("Ingrese la cantidad total de horas del proyecto: "))
costo_proyecto = float(input("Ingrese el costo total del proyecto: "))

costo_por_hora = calcular_costo_por_hora(total_horas, costo_proyecto)
print(f"El costo por hora en el proyecto es: ${costo_por_hora:.2f}")
