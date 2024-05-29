from carro import Carro

class CarroEsportivo(Carro):
    def turbo(self):
        self.velocidade += 50
        print(f"{self.modelo} atingiu {self.velocidade} km/hr com turbo \m/")