class Veiculo:
    
    def __init__(self, marca = "Não informado", qtdRodas = 0, modelo = "Não informado", velocidade = 0):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade
    
    def imprimirInformacoes(self):
        print("Marca: " + self.marca + "\n")
        print("Qtd de Rodas: " + str(self.qtdRodas) + "\n" )
        print("Modelo: " + self.modelo + "\n")
        print("Velocidade: " + str(self.velocidade) + " Km/h" + "\n")    

    def acelerar(self, valor = 0):
        self.valor = valor
        self.velocidade += valor

    def frear(self, valor = 0):
        self.valor = valor
        self.velocidade -= valor
    