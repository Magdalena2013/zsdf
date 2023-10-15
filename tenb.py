players = []
heal_power = 15

class characters():
    Name = ''
    Hp = 0
    Armor = 0
    Damage = 0

    def __init__ (self, name, hp, armor, damage):
        self.Name = name
        self.Hp = hp
        self.Armor = armor
        self.Damage = damage


class game(characters):
    def heal(self):
        global heal_power
        self.Hp += heal_power
        print(self.Name , ' have hp = ', self.Hp, 'left')

    def attack (self, Damage):
            if self.Hp - Damage > 0 :
                if self.Armor >=0:
                    self.Armor = self.Armor - Damage
                    self.Hp = self.Hp - Damage/2
                else:
                    self.Hp = self.Hp - Damage
                print(self.Name , ' hp left ', self.Hp, ' armor left ', self.Armor)
                return True
            else:
                print(self.Name, ' died')
            return False

while 1:
    try:
        confirmation = input('Enter any key to start')
        break
    except:
        print('Wrong data input')
        continue

hp = int(input('Enter players hp'))
armor = int(input('Enter players armor'))
damage = int(input('Enter players damage power'))
for i in range(0,2):
    name = input('Enter player name')
    players.append(game(name, hp, armor, damage))

alive = True
player1 = players[0]
player2 = players[1]

concurrent_player = player1
next_player = player2

while alive:
    print('Turn to choose for', concurrent_player.Name )
    print('enter 1 for attack')
    print('enter 2 for heal')
    print('enter 3 for continue')
    move = int(input())

    if move == 1:
        alive = next_player.attack(concurrent_player.Damage)
    elif move == 2:
        concurrent_player.heal()
    elif move == 3:
        continue
    else:
        print('Wrong data')
        continue

    if concurrent_player == player1:
        next_player = player1
        concurrent_player = player2
    else:
        next_player = player2
        concurrent_player = player1
