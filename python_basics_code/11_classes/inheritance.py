import datetime


class Player:       # can be referred to as a parent class
    def __init__(self, fname, lname, birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year


class CricketPlayer(Player):        # can be referred to as child class
    def __init__(self, fname, lname, birth_year, team):
        Player.__init__(self, fname, lname, birth_year)     # this will enable us pass parent properties in the child class
        self.team = team
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores)/len(self.scores)


class TennisPlayer(Player):
    def __init__(self, fname, lname, birth_year, gwinner):
        Player.__init__(self, fname, lname, birth_year)     # initializing common properties int the parent class
        self.grand_slam_winner = gwinner
        self.aces = []

    def add_aces(self, ace):
        self.aces.append(ace)

    def get_average_aces(self):
        return sum(self.aces)/len(self.aces)


virat = CricketPlayer('virat', 'kona', 1986, 'india')
jordan = TennisPlayer('michael', 'jordan', 1994, 'yes')
jordan.add_aces(34)
jordan.add_aces(56)
jordan.add_aces(87)

print(virat.get_age())
print(jordan.get_average_aces())
print(jordan.get_age())
