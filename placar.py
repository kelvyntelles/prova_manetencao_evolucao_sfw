class Placar:
    def __init__(self):
        self.resultado = resultado 
    
    def setResultado(self, pontosJogador1, pontosJogador2):
        resultado = ""
        if (self.pontosJogador1 == self.pontosJogador2 and self.pontosJogador1 < 3):
            if (self.pontosJogador1==0):
                resultado = "Love"
            if (self.pontosJogador1==1):
                resultado = "Fifteen"
            if (self.pontosJogador1==2):
                resultado = "Thirty"
            resultado += "-All"
        if (self.pontosJogador1==self.pontosJogador2 and self.pontosJogador1>2):
            resultado = "Deuce"

