import math
class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
    def getDiscriminante(self):
        return self.__b**2 - 4 * self.__a * self.__c
    def getRaiz1(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.__b + math.sqrt(disc)) / (2 * self.__a)
    def getRaiz2(self):
        disc = self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.__b - math.sqrt(disc)) / (2 * self.__a)
if __name__ == "__main__":
    v = input("Ingrese a, b, c: ").split()
    a, b, c = [float(x) for x in v]
    eq = EcuacionCuadratica(a, b, c)
    d = eq.getDiscriminante()
    if d > 0:
        print(f"La ecuación tiene dos raíces {eq.getRaiz1():.6f} y {eq.getRaiz2():.6f}")
    elif d == 0:
        r = eq.getRaiz1()
        print(f"La ecuación tiene una raíz {int(r) if r.is_integer() else r}")
    else:
        print("La ecuación no tiene raíces reales")