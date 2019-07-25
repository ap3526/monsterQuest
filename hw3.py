#Code created by Akash Patel CS-172-C Lab Section 069

from dragonEnemy import *
from goblinEnemy import *
from wolfEnemy import *
from zombieEnemy import *
from hero import *
import random
import sys


def battle(h, m):
    print('You have encountered ' + m.getName())
    #print hero's and monster's name and health
    print(h.getName() + ': ' + str(h.getHealth()) + '/' + str(h.maxHealth()) + ' health')
    print(m.getName() + ':', str(m.getHealth()) + '/' + str(m.maxHealth()) + ' health')
    #fight while both sides still have health, end when one's health hits 0
    while(h.getHealth() > 0 and m.getHealth() > 0):
        print('Remaining:', h.getFireballs(), 'Fireballs', h.getPotions(), 'Potions')
        command = input('Enter command: Sword / Shield / Fireball / Potion / Exit \n')
        #uses sword attack
        if(command.lower() == 'sword'):
            print('Sword Attack!')
            hero.attack(m)
            #checks if monster is still alive after the hero attacks. If the monster is dead, break the loop and move to the next monster. Else, keep going
            if(m.getHealth() <= 0):
                m.setHealth(0)
                print(h.getName(), 'defeated', m.getName())
                break
            print(m.getName() + ' attacks you! ')
            m.attack(hero)
        if(command.lower() == 'shield'):
            print('Shield!')
            hero.shield()
            print(m.getName() + ' attacks you! ')
            m.attack(hero)
        #make sure user has fireballs before attacking. If there are no fireballs, user loses the turn and is notified. Else, attacks
        if(command.lower() == 'fireball'):
            print('Fireball Attack!')
            if(h.getFireballs() == 0):
                print('No fireballs left!')
            else:
                hero.fireballAttack(m)
            #checks if monster is still alive after the hero attacks. If the monster is dead, break the loop and move to the next monster. Else, keep going
            if(m.getHealth() <= 0):
                m.setHealth(0)
                print(h.getName(), 'defeated ', m.getName())
                break
            print(m.getName() + ' attacks you! ')
            m.attack(hero)
        #make sure user is in a condition to use potion, if they are, use it. if not, turn is lost and user is notified
        if(command.lower() == 'potion'):
            print('Potion!')
            if(h.getPotions() == 0):
                print('No Potions Left!')
            elif(h.getHealth() == h.maxHealth()):
                print('Already at Full Health!')
            else:
                hero.potionHeal()
            print(m.getName() + ' attacks you! ')
            m.attack(hero)
        #if user enters exit, exit
        if(command.lower() == 'exit'):
            print('Thanks for playing!')
            sys.exit()
        #if hero's health falls below 0, set it to 0, display hero's health and monster's health, exit since hero lost
        if(h.getHealth() <= 0):
            h.setHealth(0)
            print(h.getName(), 'was defeated by', m.getName())
            print(h.getName() + ':', str(h.getHealth()) + '/' + str(h.maxHealth()))
            print(m.getName() + ':', str(m.getHealth()) + '/' + str(m.maxHealth()))
            sys.exit()
        
        #display hero's and enemy's health after each turn
        print(h.getName() + ':', str(h.getHealth()) + '/' + str(h.maxHealth()))
        print(m.getName() + ':', str(m.getHealth()) + '/' + str(m.maxHealth()))
if __name__ == '__main__':
    fighterList = []
    print('Welcome to Adventure Battle!')
    heroName = input('What is the name of your hero? ')
    if heroName.lower() == 'exit':
        sys.exit()
    #instantiate a hero with the given name and 100 health
    hero = hero(heroName, 100)
    #ask for how many enemies the hero wants to fight
    fighters = input('How many enemies will ' + heroName + ' battle? ')
    valid = False
    if fighters.lower() == 'exit':
        sys.exit()
    else:
        while valid is False:
            try:
                fighters = int(fighters)
                valid = True
            except:
                print('Please Enter a Valid Input')
                fighters = input('How many enemies will ' + heroName + ' battle? ')
        
    #instantiate the monsters
    wolf = wolf('Baxter the Wolf', 100)
    dragon = dragon('Drogon the Dragon', 100)
    goblin = goblin('Gerald the Goblin', 100)
    zombie = zombie('Zeus the King Zombie', 100)
    #create a list of the monsters then shuffle it to add randomness
    list = [wolf, dragon, goblin, zombie]
    random.seed(0)
    random.shuffle(list)
    for x in range(fighters):
        fighterList += [list[x]]
    for x in range(0, len(fighterList)):
        print('\n')
        battle(hero, fighterList[x])
    
    
    print('You have defeated all of the enemies in the world!')
    