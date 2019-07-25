#Code created by Akash Patel CS-172-C Lab Section 069

from enemy import *
import random

class hero(enemy):
    #instantiates hero, gives hero 10 fireballs, 6 potions, and takes off the shield
    def __init__(self, n, h):
        self.__name = n
        self.__maxHealth = h
        self.__health = h
        self.__fireballs = 10
        self.__potions = 6
        self.__shield = False
        
    def __str__(self):
        return 'I am '+ self.__name
    
    def getName(self):
        return self.__name
    #turns off shield, attacks, subtracts one from total fireballs
    def fireballAttack(self, other):
        self.__shield = False
        other.takeDamage(40)
        self.__fireballs -= 1
    #turns off shield, heals hero, subtracts one from total potions
    def potionHeal(self):
        self.__shield = False
        self.__health = self.__health + 25
        self.__potions -= 1
    #activates shield   
    def shield(self):
        self.__shield = True
    
    #turns off shield, does 15 damage
    def attack(self, other):
        self.__shield = False
        other.takeDamage(15)
    #returns current health of hero
    def getHealth(self):
        return self.__health
    
    #takes damage, if shield is on, only take half damage
    def takeDamage(self, damage):
        if self.__shield is True:
            self.__health = self.__health - (damage / 2)
        else:
            self.__health = self.__health - damage
    #returns number of potions left
    def getPotions(self):
        return self.__potions
    #returns number of fireballs left
    def getFireballs(self):
        return self.__fireballs
    #can set health i f needed
    def setHealth(self, h):
        self.__health = h
    #returns max health
    def maxHealth(self):
        return self.__maxHealth