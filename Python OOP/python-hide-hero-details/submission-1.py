class SuperHero:
    def __init__(self, name: str, __health: int, __power_level: int):
        self.name = name
        # TODO: Add the private attributes
        self.__health = __health
        self.__power_level = __power_level
    
    def __str__(self):
        return f"{self.name} has {self.get_health()} health and {self.get_power_level()} power level"

    # TODO: Add the getter and setter methods
    def get_health(self):
        return self.__health
    
    def set_health(self, new_health: int) -> None:
        if new_health >= 0 and new_health <= 100:
            self.__health = new_health
        elif new_health < 0:
            print("You can't set the health to less than 0")
        else:
            print("You can't set the health to more than 100")

    def get_power_level(self):
        return self.__power_level
    
    def set_power_level(self, new_pl: int):
        if new_pl >= 1 and new_pl <= 10:
            self.__power_level = new_pl
        elif new_pl < 1:
            print("You can't set the power level to less than 1")
        else:
            print("You can't set the power level to more than 10")

super_hero = SuperHero("Batman", 80, 9)

print(super_hero.get_health()) # this should print 80
super_hero.set_health(110) # this should print You can't set the health to more than 100
super_hero.set_health(-10) # this should print You can't set the health to less than 100
super_hero.set_health(70)

print(super_hero.get_power_level()) # this should print 9
super_hero.set_power_level(11) # this should print You can't set the power level to more than 10
super_hero.set_power_level(0) # this should print You can't set the power level to less than 1
super_hero.set_power_level(7)

# TODO: print the hero's attributes
print(super_hero)
