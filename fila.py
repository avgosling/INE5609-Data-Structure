class Fila:

    def __init__(self):
        self.__topo = None
        self.__inicio = None
        self.__contagem = 0

    @property
    def contagem(self):
        return self.__contagem

    @contagem.setter
    def contagem(self, contagem):
        self.__contagem = contagem

    def insere(self, valor, limite_elementos):
        if(self.contagem < limite_elementos):
            temp = ElementoFila(valor)
            if not self.__inicio:
                self.__inicio = temp
                self.__topo = temp
            elif not self.__inicio.seguinte:
                self.__inicio.seguinte = temp
                self.__topo = self.__inicio.seguinte
            else:
                self.__topo.seguinte = temp
                self.__topo = self.__topo.seguinte
        else:
            raise Exception('A fila está lotada.')
        self.contagem += 1

    def remove(self):
        if self.__inicio.seguinte:
            self.__inicio = self.__inicio.seguinte
        else:
            self.__topo = None
            raise Exception('A fila está vazia.')
        self.contagem -= 1

    def elemento_topo(self):
        return self.__topo.valor

    def elemento_inicio(self):
        return self.__inicio.valor
    
class ElementoFila:

    def __init__(self, valor):
        self.__valor = valor
        self.__seguinte = None
        self.__inicio = None

    @property
    def valor(self):
        return self.__valor

    @property
    def inicio(self):
        return self.__inicio

    @property
    def seguinte(self):
        return self.__seguinte

    @valor.setter
    def valor(self):
        self.__valor = valor

    @seguinte.setter
    def seguinte(self, seguinte):
        self.__seguinte = seguinte
