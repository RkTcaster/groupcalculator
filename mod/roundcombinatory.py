import copy
from itertools import product
from typing import List, Set

from .round import Round
from .match import Match

class RoundCombinatory:
    def __init__(self, round: Round):
        self.round = round

    def possibleMatches(self) -> List[Set[Match]]:
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