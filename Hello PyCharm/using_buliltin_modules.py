import random


# Using Random Module
class Dice:
    def roll(self):
        x = random.randint(1,6)
        y = random.randint(1,6)
        return x,y


for i in range(3):
    print(random.random())  # generates a random floating-point value between 0-1

for i in range(3):
    print(random.randint(30,50))  # random value between 2 passed arguments

members = ['John', 'Sarah', 'Alex', 'Jonah']
leader = random.choice(members)  # chooses an item from list randomly
print(leader)

dice = Dice()
print(dice.roll())
