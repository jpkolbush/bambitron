from enum import Enum


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


def getConf(team):
    if team in [T.DUC, T.MEADY, T.JOE, T.NICK, T.SCOTT, T.MCCLURE]:
        return 0
    else:
        return 1


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

f = open("scores.csv", "r")
lines = f.readlines()
SCORES = []
for line in lines:
    lineSplit = line.rstrip("\n").split(",")[1:]
    SCORES.append([float(data) for data in lineSplit])
f.close()

AUTO_WEEKS_COMPLETE = len(SCORES[0])
