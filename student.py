import pigo
import time
import random
from gopigo import *

'''
This class INHERITS your teacher's Pigo class. That means Mr. A can continue to
improve the parent class and it won't overwrite your work.
'''

class GoPiggy(pigo.Pigo):
    # CUSTOM INSTANCE VARIABLES GO HERE. You get the empty self.scan array from Pigo
    # You may want to add a variable to store your default speed
    MIDPOINT = 86
    STOP_DIST = 30
    speed = 100
    TURNSPEED = 185
    scan = [None] * 180

    # CONSTRUCTOR (I moved this to be on the top as you said)
    def __init__(self):
        print("Piggy has be instantiated!")
        # this method makes sure Piggy is looking forward
        #self.calibrate()
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.handler()

    #I'm trying to get rid of my drift going forward
    def setSpeed(selfself, X):
        self.speed = complex
        #I edited the speed to a decimal as you said
        set_left_speed(self.speed * 0.8)
        set_right_speed(self.speed)

    def getSpeed(selfself):
        return self.speed

    ##### HANDLE IT
    def handler(self):
        ## This is a DICTIONARY, it's a list with custom index values
        # You may change the menu if you'd like
        menu = {"1": ("Navigate forward", self.nav),
                "2": ("Rotate", self.rotate),
                "3": ("Dance", self.dance),
                "4": ("Calibrate servo", self.calibrate),
                "5": ("Test Scan", self.chooseBetter),
                "q": ("Quit", quit)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        #
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()

    # A SIMPLE DANCE ALGORITHM
    def dance(self):
        print("Piggy dance")
        ##### WRITE YOUR FIRST PROJECT HERE
        print("Is it clear?")
        for x in range(100, 200, 25):
            if not self.isClear():
                print("Omgorsh, it's not safe!")
                break
            print('Speed is set to: ' + str(x))
            servo(87)
            set_speed(x)
            self.encF(3)
            self.encB(3)
            self.encL(10)
            servo(20)
            self.encR(10)
            servo(120)
            self.encF(2)
            servo(87)
            self.encB(2)
            servo(20)
            self.encL(20)
            servo(20)
            self.encR(20)
            servo(120)
            self.encL(10)
            servo(20)
            servo(87)
            self.encR(10)
            servo(120)
            self.encF(1)
            servo(10)
            self.encB(1)
            servo(100)
            self.encF(2)
            servo(55)
            self.encB(2)
            servo(20)
            self.encF(3)
            servo(120)
            self.encB(3)
            servo(56)
            self.encF(1)
            servo(120)
            self.encB(1)
            servo(87)
            self.encF(1)
            self.encR(5)
            time.sleep(.1)
    # AUTONOMOUS DRIVING
    def nav(self):
        print("Piggy nav")
        ##### WRITE YOUR FINAL PROJECT HERE
        #TODO: If while loop fails, check for other paths
        #Just trying to scan for a wall
        print("Is it clear?")
        #Check that its clear
        while True:
            while self.isClear():
                #lets go forward just a little bit
                self.encF(5)
                #Trying to have my robot not stop if there is a wall and just go left or right
            answer= self.choosePath()
            if answer =="left":
                self.encL(4)
            elif answer == "right":
                self.encR(4)
##### Our new code to make the robot go forward and find openings to not just rely on previous turns
    def chooseBetter(self):
        self.flushScan()
        for x in range(self.MIDPOINT-60, self.MIDPOINT+60, 2):
            servo(x)
            time.sleep(.1)
            self.scan[x] = us_dist(15)
            time.sleep(.05)
        count = 0
        option = [0]
        for x in range(self.MIDPOINT-60, self.MIDPOINT+60, 2):
            if self.scan[x] > self.STOP_DIST:
                count += 1
            else:
                count=0
            if count> 9:
                print("Found an option from "+ str(x-20)+" to "+ str(x)+ " degrees")
                count = 0
                option.append(x)
                self.dataBase
        count = 0
        for x in option:
            print(" Choice # " + str(count) + " is@ " + str(x) + " degrees. ")
            count += 1
#########Ben and I shared the code Mr. A (you) helped create.
######Below is copied from Ben's code to select a path
########I shared him the code above to start this new process

        def dataBase(self):
            menu = {"1": (" Direction Left Four", self.leftTurn4),
                    "2": (" Direction Left Two", self.leftTurn2),
                    "3": (" Direction Forward Four", self.forward4),
                    "4": (" Direction Forward Eight", self.forward8),
                    "5": (" Direction Right Two", self.rightTurn2),
                    "6": (" Direction Right Four", self.rightTurn4),
                    "q": (" Return to testDrive", self.testDrive)
                    }
            # loop and print the menu...
            for key in sorted(menu.keys()):
                print(key + ":" + menu[key][0])
            #
            ans = input("Your selection: ")
            menu.get(ans, [None, error])[1]()

            # ans = input("Your selection: ")
            # option.get(ans, [None, error])[1]()

        def rightTurn4(self):
            self.encR(4)

        def rightTurn2(self):
            self.encR(2)

        def leftTurn4(self):
            self.encL(4)

        def leftTurn2(self):
            self.encL(2)

        def forward4(self):
            self.encF(4)

        def forward8(self):
            self.encF(8)
        #TODO figure out what option is closest to the midpoint
####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')


def quit():
    raise SystemExit


####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
