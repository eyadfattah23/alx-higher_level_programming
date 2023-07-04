#!python3
'''BATTLE 1
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has Died and Sam is Victorious 
Game Over
 
'''
#so basically it's like battle 0 but assign random damages and block to
#imitate a real game
import random

class Player:
    def __init__(self, name = None, health = 0, max_attack = 100, max_defense = 50):
        self.health = health
        self.name = name
        self.max_attack = max_attack
        self.max_defense = max_defense
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, new_h):
        self.__health = new_h

    @property
    def max_attack(self):
        return self.__max_attack
    @max_attack.setter
    def max_attack(self, new_a):
        self.__max_attack = new_a

    @property
    def max_defense(self):
        return self.__max_defense
    @max_defense.setter
    def max_defense(self, new_d):
        self.__max_defense = new_d


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

p1 = Player('Sam', 100)
p2 = Player('Paul', 100)
players = ('sam', 'paul')
i = 0
while True:
    if i % 2 == 0:
        x = round(random.random(), 2)
        attack1 = p1.max_attack * x
        y = round(random.uniform(0, x), 2)
        p2.health = p2.health - (attack1 - p2.max_defense* y)
        print(f'{p1.name} attacks {p2.name} and deals {round((attack1 - p2.max_defense* y), 2)}')
        print(f'{p2.name} health is {p2.health}')
        if p2.health <= 0:
            print(f'{p2.name} has died and {p1.name} is victorious')
            break
    else:
        x = round(random.random(), 2)
        attack2 = p2.max_attack * x
        y = round(random.uniform(0, x), 2)
        p1.health = p1.health - (attack2 - p1.max_defense* y)
        print(f'{p2.name} attacks {p1.name} and deals {round((attack2 - p1.max_defense* y), 2)}')
        print(f'{p2.name} health is {p2.health}')
        if p1.health <= 0:
            print(f'{p1.name} has died and {p2.name} is victorious')
            break
    i += 1

print('Game Over') 
     
