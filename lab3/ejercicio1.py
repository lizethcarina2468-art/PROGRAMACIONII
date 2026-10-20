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
    def juega(self):
        self.reiniciaPartida()
        print("Adivina un número entre el 0 y el 10:")  
        while True:
            numero = int(input())
            
            if numero == self.numeroAAdivinar:
                print("Acertaste!!")
                self.actualizaRecord()
                break
            else:
                if self.quitaVida():
                    if numero < self.numeroAAdivinar:
                        print("El número es mayor. Inténtalo de nuevo:")
                    else:
                        print("El número es menor. Inténtalo de nuevo:")
                else:
                    print("Game Over")
                    break

juego = JuegoAdivinaNumero(3, 5)
juego.juega()