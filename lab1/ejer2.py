import random
import time
class Cronometro:
    def __init__(self):
        self.__inicia = time.time() * 1000
        self.__finaliza = self.__inicia
    def get_inicia(self):
        return self.__inicia
    def get_finaliza(self):
        return self.__finaliza
    def inicia(self):
        self.__inicia = time.time() * 1000
    def detener(self):
        self.__finaliza = time.time() * 1000
    def lapsoDeTiempo(self):
        return self.__finaliza - self.__inicia
if __name__ == "__main__":
    tamanio = 100000
    numeros = [random.uniform(0, 100000) for _ in range(tamanio)]
    crono = Cronometro()
    crono.inicia()
    n = len(numeros)
    for i in range(n - 1):
        indice_mini = i
        for j in range(i + 1, n):
            if numeros[j] < numeros[indice_mini]:
                indice_mini = j
        numeros[i], numeros[indice_mini] = numeros[indice_mini], numeros[i]
    crono.detener()
    tiempo_ms = crono.lapsoDeTiempo()
    print(f"Tiempo de ejecución:")
    print(f"{tiempo_ms:.2f} milisegundos.")