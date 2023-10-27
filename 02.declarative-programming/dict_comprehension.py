
def wins_by_team(match_results):
    return {winner: {loser for team, loser in match_results if team == winner} for winner, losers in match_results}


games = [("A", "B"), ("B", "C"), ("A", "C")]
print(wins_by_team(games))
