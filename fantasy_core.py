from enum import Enum


class T(Enum):
    KOLBUSH = 1
    JON = 2
    JOE = 3
    NICK = 4
    MATTY = 5
    MCCLURE = 6
    STEVE = 7
    LAMES = 8
    BRYCE = 9
    HUNYAR = 10
    DUC = 11
    SCOTT = 12


def getConf(team):
    if team in [T.DUC, T.SCOTT, T.JOE, T.NICK, T.SCOTT, T.MCCLURE]:
        return 0
    else:
        return 1


SCHEDULE = [
    [
        T.MATTY,
        T.BRYCE,
        T.STEVE,
        T.HUNYAR,
        T.LAMES,
        T.MCCLURE,
        T.NICK,
        T.JON,
        T.SCOTT,
        T.JOE,
        T.DUC,
        T.HUNYAR,
        T.MATTY,
    ],
    [
        T.SCOTT,
        T.JOE,
        T.DUC,
        T.MCCLURE,
        T.NICK,
        T.HUNYAR,
        T.BRYCE,
        T.KOLBUSH,
        T.MATTY,
        T.STEVE,
        T.LAMES,
        T.NICK,
        T.MCCLURE,
    ],
    [
        T.NICK,
        T.JON,
        T.MCCLURE,
        T.SCOTT,
        T.DUC,
        T.STEVE,
        T.LAMES,
        T.HUNYAR,
        T.BRYCE,
        T.KOLBUSH,
        T.MATTY,
        T.DUC,
        T.NICK,
    ],
    [  # 4
        T.JOE,
        T.MCCLURE,
        T.SCOTT,
        T.DUC,
        T.JON,
        T.BRYCE,
        T.KOLBUSH,
        T.MATTY,
        T.STEVE,
        T.LAMES,
        T.HUNYAR,
        T.JON,
        T.JOE,
    ],
    [  # 5
        T.KOLBUSH,
        T.LAMES,
        T.HUNYAR,
        T.BRYCE,
        T.STEVE,
        T.DUC,
        T.MCCLURE,
        T.NICK,
        T.JON,
        T.SCOTT,
        T.JOE,
        T.STEVE,
        T.KOLBUSH,
    ],
    [  # 6
        T.DUC,
        T.NICK,
        T.JOE,
        T.JON,
        T.SCOTT,
        T.KOLBUSH,
        T.MATTY,
        T.STEVE,
        T.LAMES,
        T.HUNYAR,
        T.BRYCE,
        T.SCOTT,
        T.JON,
    ],
    [  # 7 (8 on espn.com)
        T.BRYCE,
        T.HUNYAR,
        T.KOLBUSH,
        T.LAMES,
        T.MATTY,
        T.JOE,
        T.DUC,
        T.MCCLURE,
        T.NICK,
        T.JON,
        T.SCOTT,
        T.MATTY,
        T.BRYCE,
    ],
    [
        T.HUNYAR,
        T.MATTY,
        T.BRYCE,
        T.STEVE,
        T.KOLBUSH,
        T.SCOTT,
        T.JOE,
        T.DUC,
        T.MCCLURE,
        T.NICK,
        T.JON,
        T.BRYCE,
        T.HUNYAR,
    ],
    [
        T.STEVE,
        T.KOLBUSH,
        T.LAMES,
        T.MATTY,
        T.HUNYAR,
        T.NICK,
        T.JON,
        T.SCOTT,
        T.JOE,
        T.DUC,
        T.MCCLURE,
        T.LAMES,
        T.STEVE,
    ],
    [
        T.LAMES,
        T.STEVE,
        T.MATTY,
        T.KOLBUSH,
        T.BRYCE,
        T.JON,
        T.SCOTT,
        T.JOE,
        T.DUC,
        T.MCCLURE,
        T.NICK,
        T.KOLBUSH,
        T.LAMES,
    ],
    [
        T.MCCLURE,
        T.SCOTT,
        T.JON,
        T.NICK,
        T.JOE,
        T.MATTY,
        T.STEVE,
        T.LAMES,
        T.HUNYAR,
        T.BRYCE,
        T.KOLBUSH,
        T.JOE,
        T.SCOTT,
    ],
    [
        T.JON,
        T.DUC,
        T.NICK,
        T.JOE,
        T.MCCLURE,
        T.LAMES,
        T.HUNYAR,
        T.BRYCE,
        T.KOLBUSH,
        T.MATTY,
        T.STEVE,
        T.MCCLURE,
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
