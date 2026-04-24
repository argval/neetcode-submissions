class SuperHero:
    def __init__(self, name: str, __health: int, __power_level: int):
        self.name = name
        # TODO: Add the private attributes
        self.__health = __health
        self.__power_level = __power_level
    
    def __str__(self):
        return f"{self.name} has {self.health} health and {self.power_level} power level"

    # TODO: Add the getter and setter methods
    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, new_health) -> str:
        if new_health >= 0 and new_health <= 100:
            self.__health = new_health
        elif new_health < 0:
            print("You can't set the health to less than 0")
        else:
            print("You can't set the health to more than 100")

    @property
    def power_level(self):
        return self.__power_level
    
    @power_level.setter
    def power_level(self, new_pl: int) -> None:
        if new_pl >= 1 and new_pl <= 10:
            self.__power_level = new_pl
        elif new_pl < 1:
            print("You can't set the power level to less than 1")
        else:
            print("You can't set the power level to more than 10")

super_hero = SuperHero("Batman", 80, 9)

print(super_hero.health) # this should print 80
super_hero.health = 110 # this should print You can't set the health to more than 100
super_hero.health = -10 # this should print You can't set the health to less than 100
super_hero.health = 70

print(super_hero.power_level) # this should print 9
super_hero.power_level = 11 # this should print You can't set the power level to more than 10
super_hero.power_level = 0 # this should print You can't set the power level to less than 1
super_hero.power_level = 7

# TODO: print the hero's attributes
print(super_hero)
