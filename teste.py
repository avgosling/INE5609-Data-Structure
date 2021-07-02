from pilha import Pilha
from fila import Fila


class Teste:

    def __init__(self, limite_elementos):
        self.__pilha = Pilha()
        self.__fila = Fila()
        self.__limite_elementos = limite_elementos

    @property
    def pilha(self):
        return self.__pilha

    @property
    def fila(self):
        return self.__fila
    
    @property
    def limite_elementos(self):
        return self.__limite_elementos

    def enche_pilha(self):
        for i in range(self.limite_elementos + 1):
            try:
                self.pilha.push(i+1, self.limite_elementos)
                topo = self.pilha.elemento_topo()[0]
                antecessor = self.pilha.elemento_topo()[1]
                print('Topo: {}\nAntecessor: {}'.format(topo.valor, antecessor.valor if antecessor else antecessor))
            except Exception as exc:
                print(exc)
                break

    def esvazia_pilha(self):
        while True:
            try:
                print('Excluído: {}'.format(self.pilha.elemento_topo()[0].valor))
                self.pilha.pop()
                print('Topo: {}'.format(self.pilha.elemento_topo()[0].valor))
            except Exception as exc:
                print(exc)
                break

    def enche_fila(self):
        for i in range(1, self.limite_elementos + 2):
            try:
                self.fila.insere(i, self.limite_elementos)
                print('Fim: ', self.fila.elemento_topo())
            except Exception as e:
                print(e)
                break

    def esvazia_fila(self):
        while True:
            try:
                print('Inicio: ', self.fila.elemento_inicio())
                self.fila.remove()
            except Exception as e:
                print(e)
                break


amostra = Teste(8)
print('**** Pilha ****\n')
print('Adicionando elemento na pilha...')
amostra.enche_pilha()
print('\nEsvaziando pilha...')
amostra.esvazia_pilha()
print('\n')
print('--------------- Fila ---------------\n')
print('Inserindo elementos na fila...')
amostra.enche_fila()
print('\nEsvaziando a fila.... \n')
amostra.esvazia_fila()
