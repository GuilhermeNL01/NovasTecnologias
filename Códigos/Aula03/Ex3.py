class Carro:
    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0

    def andar(self, distancia):
        autonomia = self.combustivel * self.consumo
        distancia_possivel = min(autonomia, distancia)
        combustivel_usado = distancia_possivel / self.consumo
        self.combustivel -= combustivel_usado
        return round(distancia_possivel, 2), round(self.combustivel, 2)

    def obterGasolina(self):
        return round(self.combustivel, 2)

    def adicionarGasolina(self, quantidade):
        self.combustivel += quantidade

meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
distancia_percorrida, combustivel_restante = meuFusca.andar(100)
print("Distância percorrida:", distancia_percorrida, "km")
print("Combustível restante:", combustivel_restante, "litros")
print("Nível atual de combustível:", meuFusca.obterGasolina(), "litros")
