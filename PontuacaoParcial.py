class PontuacaoParcial:
    def __init__(self, setsJogadorUm, setsJogadorDois):
        self.setsJogadorUm = setsJogadorUm
        self.setsJogadorDois = setsJogadorDois
        self.parcialJogadorUm = 0
        self.parcialJogadorDois = 0
    
    def pontuacao(self):
        parcias = ["Love", "Fifteen", "Thirty", "All"]
        tamanhoListaParciais = len(parcias)
        
        if self.setsJogadorUm < tamanhoListaParciais:
            self.parcialJogadorUm = parcias[self.setsJogadorUm]
        else:
            self.parcialJogadorUm = "Deuce"
        
        if self.setsJogadorDois < tamanhoListaParciais:
            self.parcialJogadorDois = parcias[self.setsJogadorDois]
        else:
            self.parcialJogadorDois = "Deuce"
    
    def getSetsJogadorUm(self):
        return self.parcialJogadorUm
    
    def getSetsJogadorDois(self):
        return self.parcialJogadorDois
        
    

