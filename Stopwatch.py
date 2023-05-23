import time

class Cronometro:
    def __init__(self):
        self.inicio = 0
        self.fin = 0
        self.tiempo_pausado = 0
        self.tiempos_grabados = []

    def iniciar(self):
        if self.inicio == 0:
            self.inicio = time.time()
            print("Cronómetro iniciado")
        else:
            print("El cronómetro ya está en marcha")

    def detener(self):
        if self.inicio != 0 and self.fin == 0:
            self.fin = time.time()
            print("Cronómetro detenido")
        else:
            print("El cronómetro no está en marcha")

    def pausar(self):
        if self.inicio != 0 and self.fin == 0:
            if self.tiempo_pausado == 0:
                self.tiempo_pausado = time.time()
                print("Cronómetro en pausa")
            else:
                print("El cronómetro ya está en pausa")
        else:
            print("El cronómetro no está en marcha")

    def reanudar(self):
        if self.inicio != 0 and self.fin == 0:
            if self.tiempo_pausado != 0:
                tiempo_transcurrido = time.time() - self.tiempo_pausado
                self.inicio += tiempo_transcurrido
                self.tiempo_pausado = 0
                print("Cronómetro reanudado")
            else:
                print("El cronómetro no está en pausa")
        else:
            print("El cronómetro no está en marcha")

    def grabar_tiempo(self):
        if self.inicio != 0 and self.fin != 0:
            tiempo_transcurrido = self.fin - self.inicio
            self.tiempos_grabados.append(tiempo_transcurrido)
            print("Tiempo grabado:", tiempo_transcurrido)
        else:
            print("El cronómetro debe estar detenido para grabar el tiempo")

    def obtener_tiempo_total(self):
        if self.inicio != 0 and self.fin != 0:
            tiempo_total = sum(self.tiempos_grabados, 0) + (self.fin - self.inicio)
            return tiempo_total
        else:
            return 0

# Función para ingresar el tiempo manualmente
def ingresar_tiempo_manualmente():
    while True:
        try:
            tiempo = int(input("Ingrese el tiempo en segundos: "))
            return tiempo
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

# Ejemplo de uso del cronómetro
cronometro = Cronometro()
tiempo_manual = ingresar_tiempo_manualmente()

cronometro.iniciar()
tiempo_restante = tiempo_manual

while tiempo_restante > 0:
    print("Tiempo restante:", tiempo_restante)
    time.sleep(1)
    tiempo_restante -= 1

cronometro.detener()
cronometro.grabar_tiempo()

tiempo_total = cronometro.obtener_tiempo_total()
print("Tiempo total:", tiempo_total)
