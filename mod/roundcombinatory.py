import copy
from itertools import product
from typing import List, Set

from .round import Round
from .match import Match

class RoundCombinatory:
    def __init__(self, round: Round):
        self.round = round

    def possibleMatchResult(self) -> List[Set[Match]]: 
        possibleResult = [1,-1]
        matchWinLossCombination = [
            [
                copy.deepcopy(match).updateWinScore(result)
                for result in possibleResult
            ]
            for match in self.round.matches
        ]
        roundCombinations = list(product(*matchWinLossCombination))
        roundCombinationsList = [list(combination) for combination in roundCombinations]        
        roundCombinationInRoundFormat = [Round(matches=possibleRound).updateTeams() for possibleRound in roundCombinationsList]
        
        return roundCombinationInRoundFormat
    
    def possibleMatches(self) -> List[Set[Match]]: #need to update this method in addScore and teams 
        possibleResults = [[2, 0], [2, 1], [1, 2], [0, 2]]
        matchResultsCombinations = [
            [
                copy.deepcopy(match).addScore(result[0], result[1])
                for result in possibleResults
            ]
            for match in self.round.matches
        ]
        roundCombinations = list(product(*matchResultsCombinations))
        roundCombinationsList = [list(combination) for combination in roundCombinations]        
        roundCombinationInRoundFormat = [Round(matches=possibleRound, teams=self.round.teams) for possibleRound in roundCombinationsList]
        
        return roundCombinationInRoundFormat