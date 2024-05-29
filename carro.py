class Carro: 
    def __init__(self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0 

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"{self.modelo} acelerou para {self.velocidade} km/hr.")

    