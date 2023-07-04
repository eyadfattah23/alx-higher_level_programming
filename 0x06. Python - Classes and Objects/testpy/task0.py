#!python3
'''BATTLE 0
Sam attacks Paul and deals 9 damage
Paul is down to 10 health
Paul attacks Sam and deals 7 damage
Sam is down to 7 health
Sam attacks Paul and deals 19 damage
Paul is down to -9 health
Paul has Died and Sam is Victorious 
Game Over 
'''
class Player:
    def __init__(self, name = None, health = 0):
        self.health = health
        self.name = name
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, new_h):
        self.__health = new_h
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

p1 = Player('Sam', 14)
p2 = Player('Paul', 19)

attacks = [('sam', 9),('paul', 7),('sam', 19)]
for attack in attacks:
    if attack[0] == 'sam':
        p2.health = p2.health - attack[1]
        if p2.health <= 0:
            print(f'{p2.name} has died and {p1.name} is victorious')
            break
    
    elif attack[0] == 'paul':
        p1.health = p1.health - attack[1]
        if p1.health <= 0:
            print(f'{p1.name} has died and {p2.name} is victorious')
            break
print('Game Over') 
    