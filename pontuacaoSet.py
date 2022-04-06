class PontuacaoSet:
    valorPonto = 15

    def __init__(self):
        self.pontosJogador1 = 0
        self.pontosJogador2 = 0
    
    def getPontosJogador1(self):
        return self.pontosJogador1
    
    def setPontosJogador1(self):
        self.pontosJogador1 += valorPonto

    def getPontosJogador2(self):
        return self.pontosJogador2
        
    def setPontosJogador2(self):
        self.pontosJogador2 += valorPonto
