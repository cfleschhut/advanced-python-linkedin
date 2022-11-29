def celsius_fahrenheit_dict():
    ctemps = [0, 12, 34, 100]

    temp_dict = {t: (t * 9/5 + 32) for t in ctemps if t < 100}
    print(temp_dict, temp_dict[12])


celsius_fahrenheit_dict()


def merge_dicts():
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}

    # new_team = team1 | team2
    new_team = {k: v for team in (team1, team2) for k, v in team.items()}
    print(new_team)


merge_dicts()
