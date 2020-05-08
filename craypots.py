from time import sleep
from random import randint
from os import system
#craypots
#Starting resources
boats=1
pots=5
money=50
#Turn counter
turn_num=0
#Weather
weather=True
#if Weather is True, it is good weather. Otherwise it is bad.
#Turn Structure is defined here.
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
#The Buy Phase Of The Turn
def buy():
    global money
    global pots
    global boats
    cont=False
    buy_list=""
    while not cont:
        buy_list=input("What would you like to buy?\nPress b to buy a boat.\nPress p to buy pots.\nPress enter to confirm your selection.\n")
        if buy_list.lower()=="p":
            system('cls')
            #Not finished
            while 1:
                try:
                    amount_of_pots=int(input("Please put in the amount of pots you would like to buy:\n"))
                    if amount_of_pots*10>money:
                        print("Sorry, you do not have enough money.")
                    else:
                        break
                except:
                    print("Please enter a number.")
            money-=10*amount_of_pots
            pots+=amount_of_pots
        elif buy_list.lower()=='b':
            while 1:
                try:
                    amount_of_boats=int(input("Please enter the amount of boats that you would like to buy:"))
                    if amount_of_boats*50>money:
                        print("You do not have enough money.")
                    else:
                        break        
                except:
                    print("Please enter a number")
            money-=50*amount_of_boats
            boats+=amount_of_boats
        while 1:
            cont=input("Would you like to continue buying? (Y/N)")
            if cont.lower()=="y":
                cont=False
                break
            elif cont.lower()=="n":
                cont==True
                break
            else:
                print("Please enter Y or N.")            
#Making the Turns actually occur
for i in range(12):
    turn_num=turn_num+1 
    turn()
system("cls")