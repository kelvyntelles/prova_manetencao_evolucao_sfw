class Partida:
    valorSet = 15
    valorGame = 1
    
    def __init__(self, jogadorUm, jogadorDois):
        self.jogadorUm = jogadorUm
        self.jogadorDois = jogadorDois
        self.vencedorJogo = ""
        self.gamesJogadorUm = 0
        self.gamesJogadorDois = 0
    
    def getJogadorUm(self):
        return self.jogadorUm
    
    def setJogadorUm(self, jogador):
        self.jogadorUm = jogador
    
    def getJogadorDois(self):
        return self.jogadorDois
    
    def setJogadorUm(self, jogador):
        self.jogadorDois = jogador
    
    def getVencedorJogo(self):
        return self.vencedorJogo
    
    def setSetsJogadorUm(self):
        self.gamesJogadorUm += self.valorSet
    
    def getSetsJogadorUm(self):
        return self.gamesJogadorUm
    
    def setSetsJogadorDois(self):
        self.gamesJogadorDois += self.valorSet
    
    def getSetsJogadorDois(self):
        return self.gamesJogadorDois
    
    def setGames(self, setsJogadorUm, setsJogadorDois):
        if setsJogadorUm > setsJogadorDois:
            self.gamesJogadorUm += self.valorGame
        else:
            self.gamesJogadorDois += self.valorGame
    
    def setVencedorJogo(self, gamesJogadorUm, gamesJogadorDois):
        if self.gamesJogadorUm > self.gamesJogadorDois:
            self.vencedorJogo = self.jogadorUm
        else:
            self.vencedorJogo = self.jogadorDois

