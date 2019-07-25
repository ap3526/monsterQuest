#Code created by Akash Patel CS-172-C Lab Section 069

from enemy import *
#inherits enemy
class dragon(enemy):
    #intializes dragon
    def __init__(self, n, h):
        self.__name = n
        self.__health = h
        self.__maxHealth = h
    
    def __str__(self):
        return 'I am a Dragon named ' + self.__name
    
    def getName(self):
        return self.__name
    #dragon only has 1 attack, does 30 damage
    def attack(self, other):
        other.takeDamage(30)
    #returns current health  
    def getHealth(self):
        return self.__health
    #takes damage when attacked
    def takeDamage(self, damage):
        self.__health = self.__health - damage
    #returns dragon's max health    
    def maxHealth(self):
        return self.__maxHealth
    #can set health to a different value if needed
    def setHealth(self, health):
        self.__health = health