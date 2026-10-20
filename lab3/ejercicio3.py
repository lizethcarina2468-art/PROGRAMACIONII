class Sensor:
    tipo = "Genérico"
    def __init__(self, id):
        self.id = id
        self.encendido = False
    def activar(self):
        self.encendido = True
    def desactivar(self):
        self.encendido = False

class Camara(Sensor):
    tipo = "Cámara"
    def __init__(self, id, resolucion):
        Sensor.__init__(self, id)
        self.resolucion = resolucion

class SensorLuzLaser(Sensor):
    tipo = "Luz Laser"
    def __init__(self, id, alcance):
        Sensor.__init__(self, id)
        self.alcance = alcance

class VehiculoAutonomo(Camara, SensorLuzLaser):
    tipo = "Vehículo Autónomo"
    def __init__(self, id, resolucion, alcance):
        Camara.__init__(self, id, resolucion)
        SensorLuzLaser.__init__(self, id, alcance)

vehiculo = VehiculoAutonomo("AV-001", "4K", 150)
print(f"ID: {vehiculo.id}")
print(f"Tipo: {vehiculo.tipo}")
print(f"Resolución: {vehiculo.resolucion}")
print(f"Alcance: {vehiculo.alcance}m")

vehiculo.activar()
print(f"¿Está encendido?: {vehiculo.encendido}")