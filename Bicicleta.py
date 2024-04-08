from Veiculo import Veiculo

class Bicicleta(Veiculo):
    
    def __init__(self, numMarchas = 0, bagageiro = False):
        Veiculo.__init__(self, marca = "Não informado", qtdRodas = 0, modelo = "Não informado", velocidade = 0)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro
    
    def imprimirInformacoes(self):
        print("Marchas: " + str(self.numMarchas) + "\n")
        print("Bagageiro: " + str(self.bagageiro) + "\n")
        print("Marca: " + self.marca + "\n")
        print("Qtd de Rodas: " + str(self.qtdRodas) + "\n" )
        print("Modelo: " + self.modelo + "\n")
        print("Velocidade: " + str(self.velocidade) + " Km/h" + "\n")
