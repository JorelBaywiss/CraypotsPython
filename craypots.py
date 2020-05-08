from time import sleep
from random import randint
#craypots
#Starting resources
from os import system
boats=1
pots=5
money=50
#Turn counter
turn_num=0
#Weather
weather=True
#if Weather is True, it is good weather. Otherwise it is bad.
#turn is defined here
def turn():
    global weather
    #generating weather
    weather_num=randint(1,6)
    if weather_num==1 or weather_num==2 or weather_num==3:
        weather=True
    elif weather_num!=4:
        weather=False
    system("cls")
    print("TURN %s\nYou Have:\n%s Boat(s)\n%s pots\n%s money"%(turn_num,boats,pots,money))
    buy()
def buy():
    global money
    global pots
    global boats
    cont=False
    buy_list=""
    while not cont:
        buy_list=input("What would you like to buy?\nPress b to buy a boat.\nPress p to buy pots.\nPress enter to confirm your selection.\n")
        if buy_list.lower()=="p":
            #Not finished
            pass
        elif buy_list.lower()=='b':
            if money>=50:
                money-=50
                boats+=1
            else:
                print("You are too poor to buy a boat.")
        cont=input("Would you like to continue buying? (Y/N)")
        if cont.lower()=="y":
            cont=False
        elif cont.lower()=="n":
            cont==True
        else:
            #not finished
            pass
for i in range(12):
    turn_num=turn_num+1 
    turn()
system("cls")
    
    