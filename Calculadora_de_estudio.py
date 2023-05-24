def conversion(cantidad):
    inicio = 0
    intervalo = 0

    for x in range(cantidad):
        intervalo += 1
        print(f'Intervalo {intervalo}')

        while True:
            try:
                m = int(input("Ingrese minuto: "))
                if m < 0:
                    raise ValueError #Probar si da el mismo comportamiento con continue
                break
            except ValueError:
                print("Ingrese un número entero positivo para los minutos.")

        while True:
            try:
                s = int(input("Ingrese segundo: "))
                if s < 0:
                    raise ValueError
                break
            except ValueError:
                print("Ingrese un número entero positivo para los segundos.")

        print('------------------------------------')

        minutos_a_segundo = m * 60
        inicio = minutos_a_segundo + s + inicio
    
    total_horas = int(inicio / 3600)
    total_minutos = ((inicio / 3600) - int(inicio / 3600)) * 60
    total_segundos = round((total_minutos - int(total_minutos)) * 60)

    total_minutos_dos_decimales = round(total_minutos)
    return total_horas, total_minutos_dos_decimales, total_segundos


while True:
    try:
        cantidad_elementos = int(input("--- Ingrese cantidad de intervalos de tiempo --- : "))
        if cantidad_elementos <= 0:
            raise ValueError
        break
    except ValueError:
        print("Ingrese un número entero positivo para la cantidad de intervalos.")

obtener_horas, obtener_minutos, obtener_segundos = conversion(cantidad_elementos)
print(f'Las horas de video son: {obtener_horas}, Los minutos son: {obtener_minutos}, Los segundos son: {obtener_segundos}')
