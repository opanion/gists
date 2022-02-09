from collections import OrderedDict

def main():
    #list of teams with wins and losses
    sport_teams = [
        ("Royals", (23, 4)), ("Rangers", (18, 7)), ("Spurs", (15, 12)),
        ("The Blues", (30, 0)), ("Red Devils", (4, 16)), ("Rockets", (25, 1)),
        ("Sixers", (22, 10))
    ]

    sorted_teams = sorted(sport_teams, key=lambda x: x[1][0], reverse=True)

    #created ordered dictionary of teams
    teams = OrderedDict(sorted_teams)
    print(teams)

    #use pop item to remove top item
    team, win_loss = teams.popitem(False)
    print('Top team:', team, win_loss)

    #what are the next 4 top teams
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    #equality check
    a = OrderedDict({ 'a': 1, 'b': 2, 'c': 3})
    b = { 'a': 1, 'c': 3,  'b': 2}
    c = OrderedDict({ 'a': 1, 'c': 3, 'b': 2})

    print('Equality check:', a == b)
    print('Equality check:', a == c)

if __name__ == '__main__': main()