class EcuacionLineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = float(a)
        self.__b = float(b)
        self.__c = float(c)
        self.__d = float(d)
        self.__e = float(e)
        self.__f = float(f)
    def tieneSolucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0
    def getX(self):
        det = self.__a * self.__d - self.__b * self.__c
        return (self.__e * self.__d - self.__b * self.__f) / det
    def getY(self):
        det = self.__a * self.__d - self.__b * self.__c
        return (self.__a * self.__f - self.__e * self.__c) / det
if __name__ == "__main__":
    v = input("Ingrese a, b, c, d, e, f: ").split()
    a, b, c, d, e, f = [float(x) for x in v]
    eq = EcuacionLineal(a, b, c, d, e, f)
    if eq.tieneSolucion():
        print(f"x = {eq.getX()}, y = {eq.getY()}")
    else:
        print("La ecuación no tiene solución")