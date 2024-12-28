from __future__ import annotations
from .team import Team


class Match:
    def __init__(
        self, team1: Team, team2: Team, team1Score: int = 0, team2Score: int = 0
    ):
        self.team1: Team = team1
        self.team2: Team = team2
        self.team1Score: int = team1Score
        self.team2Score: int = team2Score

    def updateWinScore(self,result:int) -> Match: #Add ways to track unties here with rivals
        self.team1.addRival(self.team2.name)
        self.team2.addRival(self.team1.name)
        self.team1.addWinResult(result)
        self.team2.addWinResult(result*-1)
        return self
   # def calculateWiner(self, team1Score) -> None:
        
    
    def updateScore(self) -> None:
        self.team1.addRival(self.team2.name)
        self.team2.addRival(self.team1.name)
        self.team1.addResult(self.team1Score, self.team2Score)
        self.team2.addResult(self.team2Score, self.team1Score)

    def addScore(self, team1Score: int, team2Score: int) -> Match:
        self.team1Score = team1Score
        self.team2Score = team2Score
        self.updateScore()
        return self

    def printMatchScore(self) -> None:
        print(
            "%s %s-%s %s"
            % (self.team1.name, self.team1Score, self.team2Score, self.team2.name)
        )
