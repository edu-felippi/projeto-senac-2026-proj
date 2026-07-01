from heroi import Heroi

class Mago(Heroi):

    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.poder_magico = 30

    def atacar(self):
        self.poder_magico += 10
        return self.poder_magico