# creating a class
import datetime


class CricketPlayer:
    def __init__(self, fname, lname, team, birth_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth_year
        self.team = team
        self.scores = []

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def add_score(self, score):
        self.scores.append(score)

    def get_average_score(self):
        return sum(self.scores)/len(self.scores)

    def __lt__(self, other):    # to perform comparison < or >... operator overloading
        my_score = self.get_average_score()
        other_score = other.get_average_score()
        return my_score < other_score

    def __str__(self):  # string overloading, to print a string
        return f"{self.first_name} {self.last_name}. the cricket player from {self.team}"


# creating object
okocha = CricketPlayer('okocha', 'okocha', 'mfm', 1988)
okocha.add_score(210)
okocha.add_score(150)
okocha.add_score(93)


david = CricketPlayer('david', 'nwaya', 'eyimba', 1992)
david.add_score(245)
david.add_score(130)
david.add_score(89)


print(okocha.get_age())
print(david.get_age())
print(okocha.scores)
print(okocha.get_average_score())
print(david.get_average_score())

print(okocha < david)

print(okocha)
