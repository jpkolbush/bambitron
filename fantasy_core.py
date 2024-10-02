from enum import Enum
import requests
import json
import os


class T(Enum):
    KOLBUSH = 1
    MEADY = 2
    JOE = 3
    NICK = 4
    LOGAN = 5
    MCCLURE = 6
    STEVE = 7
    JAMES = 8
    BRYCE = 9
    HUNYAR = 10
    DUC = 11
    SCOTT = 12

HUMAN_READABLE_NAME_MAP = {
    "jason kolbush": "Bush",
    "jonathan eady matty cooper": "Meady",
    "joe maenza": "Joe",
    "nick seidler": "Nick",
    "logan jackson": "Logan",
    "tommy  mcclure": "McClure",
    "steven marsh": "Steve",
    "james davis": "James",
    "bryce bailey": "Bryce",
    "jason h": "Hunyar",
    "tommy lam": "Duc",   
    "scott donaghy": "Scott"
}

def getConf(team):
    if team in [T.DUC, T.MEADY, T.JOE, T.NICK, T.SCOTT, T.MCCLURE]:
        return 0
    else:
        return 1
def fetch_league_data():
    url = "https://lm-api-reads.fantasy.espn.com/apis/v3/games/ffl/seasons/2024/segments/0/leagues/550501?scoringPeriodId=0&view=modular&view=mNav&view=mMatchupScore&view=mScoreboard&view=mSettings&view=mTopPerformers&view=mTeam"
    
    params = {
        'view': 'mMatchup',
        'view': 'mTeam',
        'view': 'mRoster',
        'view': 'mSettings',
    }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None

def process_league_data(league_data):
    member_dict = {member['id']: f"{member.get('firstName', '')} {member.get('lastName', '')}" for member in league_data['members']}

    team_to_member = {}
    for team in league_data['teams']:
        team_id = team.get('id')
        owner_ids = team.get('owners', [])
        team_to_member[team_id] = ', '.join([member_dict.get(owner_id, f"Unknown Owner ({owner_id})") for owner_id in owner_ids]) if owner_ids else f"Unknown Owner (Team ID: {team_id})"

    scores = {}
    for week in league_data['schedule']:
        home_team_id, away_team_id = week['home']['teamId'], week['away']['teamId']
        home_score, away_score = week['home']['totalPoints'], week['away']['totalPoints']
        if home_score == 0 and away_score == 0:
            break
        
        scores.setdefault(home_team_id, []).append(home_score)
        scores.setdefault(away_team_id, []).append(away_score)

    return team_to_member, scores

def generate_scores_csv():
    league_data = fetch_league_data()
    if league_data:
        team_to_member, scores = process_league_data(league_data)

        # Sort scores based on the enum value
        sorted_scores = []
        for team_id, score_list in scores.items():
            team_name = team_to_member[team_id].replace(',', '').lower()
            index = list(HUMAN_READABLE_NAME_MAP.keys()).index(team_name)
            sorted_scores.append((team_id, score_list, index))
        sorted_scores.sort(key=lambda x: x[2])
        sorted_scores = [(team_id, score_list) for team_id, score_list, _ in sorted_scores]

        # Create a dictionary to map team names to their scores
        team_scores = {HUMAN_READABLE_NAME_MAP[team_to_member[team_id].replace(',', '').lower()]: score_list 
                       for team_id, score_list in sorted_scores}

        with open("scores.csv", "w") as f:
            for team_name, team_scores in team_scores.items():
                score_str = ",".join(map(str, team_scores))
                f.write(f"{team_name},{score_str}\n")


SCHEDULE = [
    [
        T.HUNYAR,
        T.BRYCE,
        T.STEVE,
        T.LOGAN,
        T.JAMES,
        T.SCOTT,
        T.DUC,
        T.NICK,
        T.MEADY,
        T.MCCLURE,
        T.JOE,
        T.STEVE,
        T.HUNYAR,
    ],
    [  # 2
        T.SCOTT,
        T.DUC,
        T.JOE,
        T.NICK,
        T.MCCLURE,
        T.HUNYAR,
        T.STEVE,
        T.JAMES,
        T.KOLBUSH,
        T.BRYCE,
        T.LOGAN,
        T.DUC,
        T.JAMES,
    ],
    [
        T.MCCLURE,
        T.SCOTT,
        T.MEADY,
        T.DUC,
        T.NICK,
        T.BRYCE,
        T.LOGAN,
        T.HUNYAR,
        T.STEVE,
        T.JAMES,
        T.KOLBUSH,
        T.NICK,
        T.STEVE,
    ],
    [  # 4
        T.DUC,
        T.MCCLURE,
        T.SCOTT,
        T.MEADY,
        T.JOE,
        T.STEVE,
        T.JAMES,
        T.KOLBUSH,
        T.BRYCE,
        T.LOGAN,
        T.HUNYAR,
        T.JOE,
        T.BRYCE,
    ],
    [  # 5
        T.BRYCE,
        T.STEVE,
        T.JAMES,
        T.KOLBUSH,
        T.HUNYAR,
        T.MCCLURE,
        T.JOE,
        T.SCOTT,
        T.DUC,
        T.NICK,
        T.MEADY,
        T.JAMES,
        T.MCCLURE,
    ],
    [  # 6
        T.JOE,
        T.NICK,
        T.DUC,
        T.SCOTT,
        T.MEADY,
        T.LOGAN,
        T.HUNYAR,
        T.STEVE,
        T.JAMES,
        T.KOLBUSH,
        T.BRYCE,
        T.HUNYAR,
        T.LOGAN,
    ],
    [  # 7 (8 on espn.com)
        T.JAMES,
        T.LOGAN,
        T.KOLBUSH,
        T.HUNYAR,
        T.BRYCE,
        T.NICK,
        T.MEADY,
        T.MCCLURE,
        T.JOE,
        T.SCOTT,
        T.DUC,
        T.KOLBUSH,
        T.JOE,
    ],
    [
        T.STEVE,
        T.HUNYAR,
        T.LOGAN,
        T.BRYCE,
        T.KOLBUSH,
        T.DUC,
        T.NICK,
        T.MEADY,
        T.MCCLURE,
        T.JOE,
        T.SCOTT,
        T.LOGAN,
        T.MEADY,
    ],
    [  # 9 / 10
        T.LOGAN,
        T.KOLBUSH,
        T.HUNYAR,
        T.JAMES,
        T.STEVE,
        T.JOE,
        T.SCOTT,
        T.DUC,
        T.NICK,
        T.MEADY,
        T.MCCLURE,
        T.SCOTT,
        T.NICK,
    ],
    [
        T.KOLBUSH,
        T.JAMES,
        T.BRYCE,
        T.STEVE,
        T.LOGAN,
        T.MEADY,
        T.MCCLURE,
        T.JOE,
        T.SCOTT,
        T.DUC,
        T.NICK,
        T.MCCLURE,
        T.KOLBUSH,
    ],
    [
        T.NICK,
        T.MEADY,
        T.MCCLURE,
        T.JOE,
        T.SCOTT,
        T.JAMES,
        T.KOLBUSH,
        T.BRYCE,
        T.LOGAN,
        T.HUNYAR,
        T.STEVE,
        T.MEADY,
        T.SCOTT,
    ],
    [
        T.MEADY,
        T.JOE,
        T.NICK,
        T.MCCLURE,
        T.DUC,
        T.KOLBUSH,
        T.BRYCE,
        T.LOGAN,
        T.HUNYAR,
        T.STEVE,
        T.JAMES,
        T.BRYCE,
        T.DUC,
    ],
]

# Delete scores.csv if it exists
if os.path.exists("scores.csv"):
    os.remove("scores.csv")

generate_scores_csv()

f = open("scores.csv", "r")
lines = f.readlines()
SCORES = []
for line in lines:
    lineSplit = line.rstrip("\n").split(",")[1:]
    SCORES.append([float(data) for data in lineSplit])
f.close()

AUTO_WEEKS_COMPLETE = len(SCORES[0])
