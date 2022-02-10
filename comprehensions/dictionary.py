def main():
    temp = [0, 12, 34 ,100]

    #use comprehension to build a dictionary
    tempdict = {t: (t*9/5) + 32 for t in temp if t < 100}
    print(tempdict)
    print(tempdict[34])
    #use comprehension to merge dicts
    team1 = {'Sarah': 30, 'Paula': 45, 'Dinah': 67}
    team2 = {'Abu': 23, 'Sam': 45, 'Aaron': 8, 'James': 55}

    new_team = { k:v for team in (team1, team2) for k,v in team.items()}
    print(new_team)
if __name__ == '__main__': main() 