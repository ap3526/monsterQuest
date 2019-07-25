#Code created by Akash Patel CS-172-C Lab Section 069
from enemy import *
import random
#inherits enemy
class zombie(enemy):
    #initializes zombie
    def __init__(self, n, h):
        self.__name = n
        self.__health = h
        self.__maxHealth = h
    
    def __str__(self):
        return 'I am a Zombie named ' + self.__name
    
    def getName(self):
        return self.__name
    #two different attacks depending on the number generated
    def attack(self,other):
        x = random.randint(1,7)
        if x == 7:
            other.takeDamage(50)
        else:
            other.takeDamage(5)
    #returns current health
    def getHealth(self):
        return self.__health
    #takes damage when attacked
    def takeDamage(self, damage):
        self.__health = self.__health - damage
    
    #returns the enemy's max health
    def maxHealth(self):
        return self.__maxHealth
    #can set the health of the enemy
    def setHealth(self, health):
        self.__health = health

