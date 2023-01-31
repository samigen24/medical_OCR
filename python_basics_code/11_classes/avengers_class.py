
class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_superpower(self):
        return self.super_power

    def get_info(self):
        return f"""
        Avenger Profile:
        
        Name: {self.name}
        Age: {self.age}
        Gender: {self.gender}
        
        Has {self.weapon} weapon and {self.super_power} super Power

        """

    def __str__(self):
        return f"{self.name} is a {self.age} years old {self.gender} " \
               f"avenger with {self.super_power} as superpower and {self.weapon} as favourite weapon"

    def is_leader(self):
        return self.name == 'Captain America'


# captain_america = Avenger('Captain America', 45, 'Male', 'Super Strength', 'Shield')
# iron_man = Avenger('Iron Man', 34, 'Male', 'Technology', 'Armor')
# black_widow = Avenger('Black Widow', 29, 'Female', 'Super human', 'Batons')
# hulk = Avenger('Hulk', 42, 'Male', 'Unlimited Strength', 'None')
# thor = Avenger('Thor', 35, 'Male', 'Super Energy', 'Mjolnir')
# hawkeye = Avenger('Hawkeye', 37, 'Male', 'Fighter', 'Bow & Arrows')


# print(thor.age)
#
# print(thor.is_leader())
#
# print(captain_america.is_leader())
#
# print(captain_america.get_info())

# ..... Below is the data we need to store in the class and objects
super_heroes = ['Captain Avenger', 'Iron Man', 'Black Widow', 'Hulk', 'Thor', 'Hawkeye']
super_powers = ['Super Strength', 'Technology', 'superhuman', 'Unlimited strength', 'super Energy', 'fighting skills']
weapons = ['Shield', 'Armor', 'Batons', 'No Weapon', 'Mjolnir', 'Bow and Arrows']
ages = [110, 40, 35, 34, 10000, 30]
genders = ['M', 'M', 'F', 'M', 'M', 'M']


# we'll create a list with the class and objects
avengers = []
for name, age, gender, power, weapon in zip(super_heroes, ages, genders, super_powers, weapons):
    avengers.append(
        Avenger(name, age, gender, power, weapon)

    )

print(avengers[0].get_info())

print(avengers[4].get_info())
