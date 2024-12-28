class Team:
    def __init__(
        self,
        name: str,
        wins: int = 0,
        loss: int = 0,
        matchWins: int = 0,
        matchLoss: int = 0,
        roundWin: int = 0,
        roundLoss: int = 0,
        rivals: list = [],
    ):
        self.name: str = name
        self.wins: int = wins 
        self.loss: int = loss 
        self.matchWins: int = matchWins 
        self.matchLoss: int = matchLoss 
        self.roundWin: int  = roundWin 
        self.roundLoss: int  = roundLoss 
        self.rivals: list = rivals

    def addWinResult(self, result: int) -> None:
        if result == 1:
            self.wins += 1
        else:
            self.loss += 1
    
    def addResult(self, ownMatches: int, rivalMatches: int) -> None: #Round updater 
        self.matchWins += ownMatches
        self.matchLoss += rivalMatches
        if ownMatches > rivalMatches:
            self.wins += 1
        else:
            self.loss += 1

    def addRival(self, oponent: str) -> None:
        self.rivals.append(oponent)
