import math
class AlgebraVectorial:
    def __init__(self, a=[0,0,0], b=[0,0,0]):
        self._a = [float(x) for x in a]
        self._b = [float(x) for x in b]
    def _norma(self, v):
        return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    def _punto(self, v1, v2):
        return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]
    def esPerpendicular1(self):
        suma = [self._a[0]+self._b[0], self._a[1]+self._b[1], self._a[2]+self._b[2]]
        resta = [self._a[0]-self._b[0], self._a[1]-self._b[1], self._a[2]-self._b[2]]
        return round(self._norma(suma), 4) == round(self._norma(resta), 4)
    def esPerpendicular2(self):
        r1 = [self._a[0]-self._b[0], self._a[1]-self._b[1], self._a[2]-self._b[2]]
        r2 = [self._b[0]-self._a[0], self._b[1]-self._a[1], self._b[2]-self._a[2]]
        return round(self._norma(r1), 4) == round(self._norma(r2), 4)
    def esPerpendicular3(self):
        return round(self._punto(self._a, self._b), 4) == 0
    def esPerpendicular4(self):
        suma = [self._a[0]+self._b[0], self._a[1]+self._b[1], self._a[2]+self._b[2]]
        lhs = self._norma(suma)**2
        rhs = self._norma(self._a)**2 + self._norma(self._b)**2
        return round(lhs, 4) == round(rhs, 4)
    def esParalelo1(self):
        if self._b[0] == 0 or self._b[1] == 0 or self._b[2] == 0:
            return False
        r0 = self._a[0] / self._b[0]
        r1 = self._a[1] / self._b[1]
        r2 = self._a[2] / self._b[2]
        return round(r0, 4) == round(r1, 4) == round(r2, 4)
    def esParalelo2(self):
        cx = self._a[1]*self._b[2] - self._a[2]*self._b[1]
        cy = self._a[2]*self._b[0] - self._a[0]*self._b[2]
        cz = self._a[0]*self._b[1] - self._a[1]*self._b[0]
        return round(self._norma([cx, cy, cz]), 4) == 0
    def proyeccion_de_a_sobre_b(self):
        p = self._punto(self._a, self._b)
        n2 = self._norma(self._b)**2
        if n2 == 0:
            return [0.0, 0.0, 0.0]
        f = p / n2
        return [f * self._b[0], f * self._b[1], f * self._b[2]]
    def componente_de_a_en_b(self):
        p = self._punto(self._a, self._b)
        n = self._norma(self._b)
        if n == 0:
            return 0.0
        return p / n
if __name__ == "__main__":
    v1 = [1, 2, 3]
    v2 = [2, 4, 6]
    vec = AlgebraVectorial(v1, v2)
    print(f"¿Es paralelo?: {vec.esParalelo1()}")
    print(f"¿Es paralelo?: {vec.esParalelo2()}")
    print(f"Componente de a en b: {vec.componente_de_a_en_b():.2f}")
    print(f"Proyección de a sobre b: {vec.proyeccion_de_a_sobre_b()}")