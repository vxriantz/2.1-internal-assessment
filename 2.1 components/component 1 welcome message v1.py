""" This component will detail a welcome message for the beginning of a pizza establishment program"""
#import library random
import random
#import random integer
from random import randint

#list of names used by BOT
bot_names = ["Anthony", "Clint", "Gamora", "Howard", "Wanda", "Jecilla", "James", "Steve", "Natasha", "Sam"]


num = randint(0,9)
name = (bot_names[num])
print(name)