from Veiculo import Veiculo
from Automovel import Automovel
from Bicicleta import Bicicleta
from Carro import Carro
from Moto import Moto


print("---------------------------------")
print("VEÍCULO 01")
v1 = Veiculo()
v1.imprimirInformacoes()
print("----------")
print("VEÍCULO 02")
v2 = Veiculo("Gol", 4, "Bola")
v2.acelerar(20)
v2.frear(5)
v2.imprimirInformacoes()

print("---------------------------------")
print("AUTOMÓVEL 01")
a1 = Automovel()
a1.imprimirInformacoes()
print("----------")
print("AUTOMÓVEL 02")
a2 = Automovel(500.00)
a2.imprimirInformacoes()

print("---------------------------------")
print("BICICLETA 01")
b1 = Bicicleta()
b1.imprimirInformacoes()
print("----------")
print("BICICLETA 02")
b2 = Bicicleta(12, True)
b2.imprimirInformacoes()

print("---------------------------------")
m1 = Moto()
m1.imprimirInformacoes()

print("---------------------------------")
c1 = Carro()
c1.imprimirInformacoes()
