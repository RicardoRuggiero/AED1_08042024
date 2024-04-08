from Automovel import Automovel

class Moto(Automovel):
    def __init__(self, partidaEletrica = False):
        Automovel.__init__(self, potenciaDoMotor = 0.00)
        self.partidaEletrica = partidaEletrica

    def imprimirInformacoes(self):
        print("Partida Elétrica: " + str(self.partidaEletrica) + "\n")
        print("Potência do Motor: " + str(self.potenciaDoMotor) + "\n")