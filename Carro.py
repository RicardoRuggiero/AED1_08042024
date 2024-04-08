from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, qtdPortas = 2):
        Automovel.__init__(self, potenciaDoMotor = 0.00)
        self.qtdPortas = qtdPortas

    def imprimirInformacoes(self):
        print("Qtd de Portas: " + str(self.qtdPortas) + "\n")
        print("Potência do Motor: " + str(self.potenciaDoMotor) + "\n")