"""This component will detail a welcome message for the beginning of a gift box establishment program"""
#import library random
import random
#import random integer
from random import randint

#list of names used by BOT
bot_names = ["David", "Rose", "Georgina", "Oliver", "Denise", "Jecilla", "James", "Steve", "Natasha", "Sam"]


def welcome():
    num = randint(0,9)
    name = (bot_names[num])
    print("***Welcome to Dream Pizza***")
    print("***My name is", name,"***")
    print("***I will be here to help you order your delicious Dream Pizza***")


def main():
    welcome()


main()