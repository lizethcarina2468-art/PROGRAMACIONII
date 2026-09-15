import math
class MiPunto:
    def __init__(self, x=0, y=0):
        self._x=float(x)
        self._y=float(y)
    def getX(self):
        return self._x
    def getY(self):
        return self._y
    def distanciaPunto(self, p):
        return math.sqrt((self._x - p.getX())**2+(self._y - p.getY())**2)
    def distanciaCoordenadas(self, x ,y):
        return math.sqrt((self._x - x)**2+(self._y - y)**2)
if __name__ == "__main__":
    p1=MiPunto(0, 0)
    p2=MiPunto(10, 30.5)
    print(f"Distancia: {p1.distanciaPunto(p2):.2f}")