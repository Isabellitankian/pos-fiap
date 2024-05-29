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