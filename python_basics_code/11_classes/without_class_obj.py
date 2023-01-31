import datetime

okocha = {'first_name': 'okocha',
            'last_name': 'jeje',
            'birth_year': 1988,
            'scores': []
          }
okocha['scores'].append(80)
okocha['scores'].append(100)
okocha['scores'].append(45)


def get_avg_score(player):
    return sum(player['scores'])/len(player['scores'])


print(f"Okocha's avergae score is {get_avg_score(okocha)}")


def get_age(player):
    now = datetime.datetime.now()
    return now.year - player['birth_year']


print(f"Okocha's age is {get_age(okocha)}")


# E302 expected 2 blank lines, found 1
# This means two empty lines are expected before and after a function
# standard practice


david = {'first_name': 'david',
            'last_name': 'nwaya',
            'birth_year': 1992,
            'scores': []
          }
david['scores'].append(94)
david['scores'].append(79)
david['scores'].append(68)


def get_avg_score(player):
    return sum(player['scores'])/len(player['scores'])


print(f"David's avergae score is {get_avg_score(david)}")


def get_age(player):
    now = datetime.datetime.now()
    return now.year - player['birth_year']


print(f"David's age is {get_age(david)}")
