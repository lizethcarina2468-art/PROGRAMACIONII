import math
class Vector:
    def __init__(self, v=[0,0,0]):
        self._v = [float(x) for x in v]
    def sumar(self, vec2):
        return Vector([self._v[0]+vec2._v[0], self._v[1]+vec2._v[1], self._v[2]+vec2._v[2]])
    def multiplicarEscalar(self, r):
        return Vector([float(r)*self._v[0], float(r)*self._v[1], float(r)*self._v[2]])
    def longitud(self):
        return math.sqrt(self._v[0]**2 + self._v[1]**2 + self._v[2]**2)
    def normal(self):
        m = self.longitud()
        if m == 0:
            return Vector([0,0,0])
        return Vector([self._v[0]/m, self._v[1]/m, self._v[2]/m])
    def productoPunto(self, vec2):
        return self._v[0]*vec2._v[0] + self._v[1]*vec2._v[1] + self._v[2]*vec2._v[2]
    def productoVectorial(self, vec2):
        cx = self._v[1]*vec2._v[2] - self._v[2]*vec2._v[1]
        cy = self._v[2]*vec2._v[0] - self._v[0]*vec2._v[2]
        cz = self._v[0]*vec2._v[1] - self._v[1]*vec2._v[0]
        return Vector([cx, cy, cz])
    def mostrar(self):
        return f"({round(self._v[0],2)}, {round(self._v[1],2)}, {round(self._v[2],2)})"
if __name__ == "__main__":
    a = Vector([1, 2, 3])
    b = Vector([4, 5, 6])
    print(f"Suma: {a.sumar(b).mostrar()}")
    print(f"Escalar: {a.multiplicarEscalar(3).mostrar()}")
    print(f"Longitud: {a.longitud():.2f}")
    print(f"Normal: {a.normal().mostrar()}")
    print(f"Producto punto: {a.productoPunto(b)}")
    print(f"Producto vectorial: {a.productoVectorial(b).mostrar()}")