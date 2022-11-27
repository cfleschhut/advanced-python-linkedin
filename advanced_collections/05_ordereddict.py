from collections import OrderedDict

sportTeams = [
    ("Royals", (18, 12)), ("Rockets", (24, 6)),
    ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
    ("Kings", (15, 15)), ("Chargers", (20, 10)),
    ("Jets", (16, 14)), ("Warriors", (25, 5))
]

sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

teams = OrderedDict(sortedTeams)
print(teams)

team, win_loss = teams.popitem(False)
print(team, win_loss)

a = OrderedDict({"a": 1, "b": 2, "c": 3})
b = OrderedDict({"a": 1, "c": 3, "b": 2})
print(a == b)
