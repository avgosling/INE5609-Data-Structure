class Pilha:

    def __init__(self):
        self.__topo = None
        self.__contagem = 0

    @property
    def contagem(self):
        return self.__contagem

    @contagem.setter
    def contagem(self, contagem):
        self.__contagem = contagem

    def push(self, valor, max_elementos):
        if(self.contagem < max_elementos):
            temp = ElementoPilha(valor)
            temp.antecessor = self.__topo
            self.__topo = temp
            self.contagem += 1
        else:
            raise Exception('Alcançou o limite.')

    def pop(self):
        self.contagem -= 1
        if(self.__topo.antecessor):
            self.__topo = self.__topo.antecessor
        else:
            raise Exception('Pilha vazia.')
    
    def elemento_topo(self):
        topo = self.__topo
        return (topo, topo.antecessor)

class ElementoPilha:

    def __init__(self, valor):
        self.__valor = valor
        self.__antecessor = None

    @property
    def valor(self):
        return self.__valor

    @property
    def antecessor(self):
        return self.__antecessor

    @valor.setter
    def valor(self):
        self.__valor = valor

    @antecessor.setter
    def antecessor(self, antecessor):
        self.__antecessor = antecessor
