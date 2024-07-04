from fantasy_core import *
import copy


def generate_matches():
    ret = []
    for w in range(WEEKS_COMPLETE, 13):
        w_ret = []
        unused_teams = set([team for team in T])
        for team_idx, team in enumerate(T):
            if team not in unused_teams:
                continue
            w_ret.append([team, SCHEDULE[team_idx][w]])
            unused_teams.remove(team)
            unused_teams.remove(SCHEDULE[team_idx][w])
        ret.append(w_ret)
    return ret


def simulate():
    scores = copy.deepcopy(SCORES)
    # List of results for each team
    ret = []
    for team in T:
        ret.append(
            {
                "Team": team,
                "Wins": 0,
                "Losses": 0,
            }
        )

    # Determine Record for regular season & two week tots for playoffs
    for team_idx in range(12):
        for week in range(WEEKS_COMPLETE):
            opponent = SCHEDULE[team_idx][week]
            this_score = scores[team_idx][week]
            opp_score = scores[opponent.value - 1][week]
            if this_score > opp_score:
                ret[team_idx]["Wins"] += 1
            elif this_score < opp_score:
                ret[team_idx]["Losses"] += 1
            else:
                ret[team_idx]["Wins"] += 0.5
                ret[team_idx]["Losses"] += 0.5

    return ret


print(simulate())
print(generate_matches())
