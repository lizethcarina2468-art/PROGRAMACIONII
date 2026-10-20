class Juego:
    def __init__(self, numeroDeVidas):
        self.numeroDeVidas = numeroDeVidas
        self.record = 0
    def reiniciaPartida(self):
        self.vidas = self.numeroDeVidas
    def actualizaRecord(self):
        if self.vidas > self.record:
            self.record = self.vidas
    def quitaVida(self):
        self.vidas -= 1
        if self.vidas > 0:
            return True
        else:
            return False

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas, numeroSecreto):
        super().__init__(numeroDeVidas)
        self.numeroAAdivinar = numeroSecreto
    def validaNumero(self, numero):
        if 0 <= numero <= 10:
            return True
        else:
            return False
    def juega(self):
        self.reiniciaPartida()
        print(f"Adivina un número entre 0 y 10")
        while True:
            numero = int(input())
            if not self.validaNumero(numero):
                print("Error: El número debe estar entre 0 y 10.")
                continue
            if numero == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if numero < self.numeroAAdivinar:
                        print("El número es mayor:")
                    else:
                        print("El número es menor:")
                else:
                    print("Game Over. Te quedaste sin vidas.")
                    break

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if 0 <= numero <= 10:
            if numero % 2 == 0:
                return True
            else:
                print("Error: El número ingresado es impar.")
                return False
        else:
            print("Error: El número debe estar entre 0 y 10.")
            return False

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def validaNumero(self, numero):
        if 0 <= numero <= 10:
            if numero % 2 != 0:
                return True
            else:
                print("Error: El número ingresado es par.")
                return False
        else:
            print("Error: El número debe estar entre 0 y 10.")
            return False

print("Juego Adivina Número")
juego1 = JuegoAdivinaNumero(3, 4)
juego1.juega()

print("Juego Adivina Par")
juego2 = JuegoAdivinaPar(3, 6)
juego2.juega()

print("Juego Adivina Impar")
juego3 = JuegoAdivinaImpar(3, 7)
juego3.juega()