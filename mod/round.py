from __future__ import annotations
from typing import List, Optional, Dict
import pandas as pd
from .team import Team
from .match import Match

class Round:  # Change Name to Round/RoundState/other
    def __init__(
        self, matches: Optional[List[Match]] = [], teams: Optional[List[Team]] = []
    ):
        self.matches: List[Match] = matches
        self.teams: List[Team] = teams

    def createTeams(self, teamInfo: Dict[str, str | int]) -> None:
        self.teams = [Team(*attributes) for attributes in zip(*teamInfo.values())]
    
    def updateTeams(self) -> Round:
        self.teams = [team for match in self.matches for team in (match.team1, match.team2)]
        return self
    
    def createRound(self, roundMatches: List[List[str]]) -> None:
        for matches in roundMatches:
            team1 = None
            team2 = None
            for team in self.teams:
                if team.name == matches[0]:
                    team1 = team
                if team.name == matches[1]:
                    team2 = team
            self.matches.append(Match(team1=team1, team2=team2))

    def printRoundScore(self) -> None:
        for match in self.matches:
            match.printMatchScore()

    def createDf(self, dictForDf: Dict) -> pd.DataFrame:
        roundDf = pd.DataFrame(dictForDf)
        roundDf["wins_loss"] = roundDf.wins - roundDf.loss
        roundDf = roundDf.sort_values(by="wins_loss", ascending=False)

        return roundDf

    def createDict(self) -> Dict:
        dictForDf = {
            "name": [],
            "wins": [],
            "loss": [],
            "matchWins": [],
            "matchLoss": [],
            "roundWin": [],
            "roundLoss": [],
        }
        for team in self.teams:
            dictForDf["name"].append(team.name)
            dictForDf["wins"].append(team.wins)
            dictForDf["loss"].append(team.loss)
            dictForDf["matchWins"].append(team.matchWins)
            dictForDf["matchLoss"].append(team.matchLoss)
            dictForDf["roundWin"].append(team.roundWin)
            dictForDf["roundLoss"].append(team.roundLoss)

        return dictForDf

    def roundToDf(self) -> pd.DataFrame:
        createDict = self.createDict()

        return self.createDf(createDict)
