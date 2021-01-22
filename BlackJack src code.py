from random import randint
from termcolor import * 
import colorama
import os
colorama.init()
import sys

import random
class Cards():
    def __init__(self):
        self.number=random.choice([1,2,3,4,5,6,7,8,9,10,'Jack','Queen','King'])
        self.suit=random.choice(['Spade','Diamond','Club','Heart'])


i=1
d=[]
psum=0
plist=[]
csum=0
clist=[]
chip=200
bet=0



def print_table():
    print()
    cprint("COMPUTER'S HAND",'white','on_red' ,attrs=['underline'])
    print('***************')
    #print()
    print('unidentified',end='  |  ')
    print(*clist[1:] ,sep='  |  ')
    #print (csum)
    print('\n')
    print()
    cprint("PLAYER'S HAND",'white','on_blue')
    print('*************')
    print(*plist,sep='  |  ')
    cprint ('sum: ' + str(psum),'cyan')
    print()
    print('------------------------------------------------')
    print()

def print_table_c():
    print()
    cprint("COMPUTER'S HAND",'white','on_red')
    print('***************')
    print(*clist,sep='  |  ')
    cprint ('sum: ' + str(csum),'cyan')
    print('\n')
    print()
    cprint("PLAYER'S HAND",'white','on_blue')
    print('*************')
    print(*plist,sep='  |  ')
    cprint ('sum: ' + str(psum),'cyan')
    print()
    print('------------------------------------------------')
    print()
    
def start_deal():
    global psum
    global csum
    global chip
    global bet
    
    print('How much do you want to bet? (total chips:',end='')
    cprint(str(chip),'red',end='',attrs=['underline'])
    print(')\n',end='')
    while True:
        try:
            bet=int(input())
        except:
            cprint('\nEnter a valid input','red')
            continue
        else:
            break;
    
    while int(bet)>chip or int(bet)<0:
        cprint(f'\nYou only have {chip} chips ,Enter again','red')
        bet=input()
    chip=chip-int(bet)
    i=1
    while i<5:
        a=Cards()
        
        
        if(i%2!=0):
            if a.number=='Jack' or a.number=='Queen' or a.number=='King':
                psum=psum+10
            else:
                psum=psum+a.number
            plist.append(str(a.number) + ' of ' + a.suit)
            
        else:
            if a.number=='Jack' or a.number=='Queen' or a.number=='King':
                csum=csum+10
            else:
                csum=csum+a.number
            clist.append(str(a.number) + ' of ' + a.suit)
        
        d.append(a.suit+str(a.number))
        i=i+1
    print_table()
    ask()
    
def p_pick():
    global psum
    a=Cards()
    if(not a.suit+str(a.number)in d):
        if(a.number==1):
            if(psum+11>21):
                psum=psum+1
            elif(psum+11<21):
                psum=psum+11
        elif a.number=='Jack' or a.number=='Queen' or a.number=='King':
            psum=psum+10
        else:
            psum=psum+a.number
        plist.append(str(a.number) + ' of ' + a.suit)
        d.append(a.suit+str(a.number))
    else:
        p_pick()
        
def c_pick():
    global csum
    a=Cards()
    if(not a.suit+str(a.number)in d):
        if(a.number==1):
            if(csum+11>21):
                csum=csum+1
            elif(csum+11<21):
                csum=csum+11
        
        elif a.number=='Jack' or a.number=='Queen' or a.number=='King':
            csum=csum+10
            
        
        else:
            csum=csum+a.number
        clist.append(str(a.number) + ' of ' + a.suit)
        d.append(a.suit+str(a.number))
    else:
        c_pick()
        

def ask():
    global csum
    global psum
    global chip
    global bet
    w=input('***HIT OR STAND*** [h,s]\n')
    while w!='h' and w!='s':
        cprint('\nEnter a valid input','red')
        w=input('***HIT OR STAND*** [h,s]\n')
    while w=='h':
        p_pick()
        print_table()
        if(psum>21):
            cprint('YOU lOST :(','red')
            print('(current number of chips:',end='')
            cprint(chip,'cyan',end='')
            print(')')
            break;
        elif(psum==21):
            cprint('YOU WON :-)','green')            
            chip=chip+int(bet)*2
            print('(current number of chips:',end='')
            cprint(chip,'cyan',end='')
            print(')')
            break;
        w=input('***HIT OR STAND*** [h,s]\n')
        while w!='h' and w!='s':
            cprint('\nEnter a valid input','red')
            w=input('***HIT OR STAND*** [h,s]\n')
    if w=='s':
        if(csum>psum):
            print_table_c()
            cprint('YOU LOST :(','red')
            print('(current number of chips:',end='')
            cprint(chip,'cyan',end='')
            print(')')
        else:
            while(csum<=psum):
                c_pick()
                print_table_c()
                
            if csum>psum and csum<22:
                cprint ('YOU LOST :(','red')
                print('(current number of chips:',end='')
                cprint(chip,'cyan',end='')
                print(')')
            elif csum>21:
                cprint('YOU WON :-)','green')
                chip=chip+int(bet)*2
                print('(current number of chips:',end='')
                cprint(chip,'cyan',end='')
                print(')')
    if chip==0:
        cprint('GAME OVER *_*','white','on_red')
    else:
        play_again=input('Would you like to play again? [y/n]\n')
        while play_again!='y' and play_again!='n':
            cprint('\nEnter a valid input','red')
            play_again=input('Would you like to play again? [y/n]\n')
        if play_again=='y':
            psum=0
            plist[:]=[]
            csum=0
            clist[:]=[]
            i=1
            os.system('cls')
            start_deal()
    
        

print("                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("                 ******************************")
print('                 ',end='')
cprint('***||WELCOME TO BLACKJACK||***','magenta','on_white',attrs=['bold'])
print("                 ******************************")
print("                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print()

start_deal()  
input('Press Enter to exit')    
