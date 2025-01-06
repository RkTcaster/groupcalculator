from __future__ import annotations
from typing import List, Optional, Dict
import pandas as pd
from .team import Team
from .match import Match
from itertools import groupby

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
    
    def createHierarchy(self) -> Dict:
        hierarchy_dict = {}
        for team in self.teams:
            hierarchy_dict[team.name] = {
            "wins": team.wins,
            "rivals":team.rivals,
            "loss": team.loss,
            "matchWins": team.matchWins,
            "matchLoss": team.matchLoss,
            "matchRanking": 1000 +team.wins*100-team.loss*100+team.matchWins-team.matchLoss
            # "roundWin": team.roundWin,
            # "roundLoss": team.roundLoss,
            }
        return hierarchy_dict
    def round_to_hierarchy_dict(self) -> Dict:
        createDict = self.createHierarchy()
        return self.createHierarchy(createDict)

    def group_table(self,teamDict: List):
        return  [
        list(group) for _, group in groupby(teamDict, key=lambda x: x[1]["wins"])
    ]
    
    # def untie_rules(self):
    #     if len(self) == 2:
            
    
    def winEvaluation(self) -> List:        
        table_dict = self.createHierarchy()
        sorted_table = sorted(table_dict.items(), 
                              key = lambda x: (x[1]["wins"],x[1]["loss"],
                                               x[1]["matchWins"],x[1]["matchLoss"],
                                               x[1]["matchRanking"],
                                               x[1]["rivals"]),        
        reverse=True)

        grouped_table = self.group_table(sorted_table)                   
  
        return grouped_table
    

