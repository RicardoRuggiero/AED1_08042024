from Veiculo import Veiculo

class Automovel(Veiculo):

    def __init__(self, potenciaDoMotor = 0.00):
        Veiculo.__init__(self, marca = "Não informado", qtdRodas = 0, modelo = "Não informado", velocidade = 0)
        self.potenciaDoMotor = potenciaDoMotor

    def imprimirInformacoes(self):
        print("Potência do Motor: " + str(self.potenciaDoMotor) + "\n")
        print("Marca: " + self.marca + "\n")
        print("Qtd de Rodas: " + str(self.qtdRodas) + "\n" )
        print("Modelo: " + self.modelo + "\n")
        print("Velocidade: " + str(self.velocidade) + " Km/h" + "\n")  
