from unidecode import unidecode

def limpar_texto(texto):
    """ Remove acentos e caracteres especiais 
     Transforma a string em letras maiúsculas."""
    
    texto_sem_acento = unidecode(texto)

    texto_maiusculo = texto_sem_acento.upper()

    return texto_maiusculo


class Exemplo:
    @classmethod 
    def etodo_de_classe(cls):
        # comportamento modificado para operar na classe, não na instância.
        pass

    @staticmethod
    def metodo_estatico():
        #metodo que nbão depende da instância ou da classe.
        pass

class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Carro: 
    def __init__(self):
        self.motor = Motor(tipo="V8")

    def ligar(self):
        print("Carro ligado com um motor", self.motor.tipo)

class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    ## #Exemplo de uso ### 
aluno1 = Aluno(nome = 'João')
aluno2 = Aluno(nome = 'Maria')

turma = Turma()
turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)

class MinhaMetaclasse(type):
    def __new__(cls, nome, bases, dct):
        
        #adiciona um novo tributo à classe
        dct['novo atributo'] = 42
        nova_classe = super().__new__(cls, nome, bases, dct)
        return nova_classe
    
    #usando a meta-classe para criar uma nova classe
class MinhaClasse(metaclass=MinhaMetaclasse):
    pass

# Testando a nova classe

objeto = MinhaClasse()
print(MinhaClasse.novo_atributo)

class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

#testando o Singleton 
s1 = Singleton()
s2 = Singleton()

print(s1 is s2) #saida deve ser: True 

from abc import ABC, abstractclassmethod, abstractmethod

class Observer(ABC): # interface observar 
    @abstractclassmethod
    def update(self, message):
        pass

class Subject: #subject (ou observable)
    _observers = []
    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observer(self, message):
        for observer in self._observers:
            observer.update(message)

class ConcreteObserver(Observer): #concrete observer
    def update(self, message):
        print(f"Recebi a mesagem: {message}")

subject = Subject()
observer1 = ConcreteObserver()
observer2 = ConcreteObserver()

subject.add_observer(observer1)
subject.add_observer(observer2)

subject.notify_observer("novo estado!")

# saída: Recebi a mesagem: novo estado!
# Recebi a mesagem: novo estado!


class Strategy(ABC): # interface Strategy
    @abstractmethod
    def execute(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Executando estratégia A")

class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Executando estratégia B")

class Context:     #contexto
    def __init__(self, strategy):
        self._strategy = strategy
    def set_strategy(self, strategy):
        self._strategy = strategy
    def execute_strategy(self):
        self._strategy.execute()

strategy_a = ConcreteStrategyA()
strategy_b = ConcreteStrategyB()

context = Context(strategy_a)
context.execute_strategy()  #saida: Executando estratégia A

context.set_strategy(strategy_b)
context.execute_strategy()   #saida: Executando estratégia B
