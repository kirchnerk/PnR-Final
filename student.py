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
    TURNSPEED = 185
    scan = [None] * 180
    LEFT_SPEED = 190
    RIGHT_SPEED = 190

    turn_track = 0
    TIME_PER_DEGREE = 0.00466667
    TURN_MODIFIER = 1

    ##This method starts my robot
    # CONSTRUCTOR (I moved this to be on the top as you said)
    def __init__(self):
        print("Piggy has be instantiated!")
        # this method makes sure Piggy is looking forward
        #self.calibrate()
        # let's use an event-driven model, make a handler of sorts to listen for "events"
        while True:
            self.stop()
            self.handler()

    ###this method gives me the menu when I type in python3 student.py
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
        menu.get(ans,[None, error])[1]()

    ##This method is my dance method
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

##### MY NEW TURN METHODS because enR and encL just don't cut it
        #takes a number of degrees and turns accordingly
    #this method defines turning right through degrees
    def turnR(self, deg):
        self.turn_track += deg
        print("The exit is " + str(self.turn_track) + "degrees away.")
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER,
                      self.RIGHT_SPEED * self.TURN_MODIFIER)
        right_rot()
        time.sleep(deg * self.TIME_PER_DEGREE)
        self.stop()
        self.setSpeed(self.LEFT_SPEED * self.RIGHT_SPEED)
    #this method defines turning left through degrees
    def turnL(self, tt):
        ##adjust the tracker so we know how many degrees away our exit is
        self.turn_track -= deg
        print("The exit is " + str(self.turn_track) + "degrees away.")
        #slow done for more exact turning
        self.setSpeed(self.LEFT_SPEED * self.TURN_MODIFIER,
                      self.RIGHT_SPEED * self.TURN_MODIFIER)
        #do turn stuff
        left_rot()
        #use our experiments to calculate the time needed to turn
        time.sleep(deg * self.TIME_PER_DEGREE)
        self.stop()
        self.setSpeed(self.LEFT_SPEED * self.RIGHT_SPEED)

    ##adjusts robot motors when turning right or left
    def setSpeed(self, left, right):
        print("Left speed: " + str(left))
        print("Right speed: " +str(right))
        set_left_speed(int(left))
        set_right_speed(int(right))
        time.sleep(0.05)


    # AUTONOMOUS DRIVING
    #Central logic loop of my navigation
    def cruise(self):
        # do i check is Clear before?
        servo(self.MIDPOINT)
        time.sleep(0.5)
        fwd()
        while True:
            if us_dist(15) < self.STOP_DIST:
                break
            time.sleep(0.5)
        self.stop()

    def nav(self):
        ##main app loop
        while True:
            ###I copied this code from the board in class
            ####I'm trying to speed up my robot
            if(self.isClear()):
                print("It looks clear ahead of me. I'm going to cruise")
                self.cruise()
            #TODO:Insert a method that backs away from a wall if it's too close
            #TODO:self.backUpCheck
            #TODO: Replace choosePath with a method that's smarter

            answer= self.choosePath()
            #TODO: Replace '45' with a variable representing a smarter option
            if answer =="left":
                self.turnL(30)
            elif answer == "right":
                self.turnR(30)

##### Our new code to make the robot go forward and find openings to not just rely on previous turns
        ###this method is my scanning method to make sure my robot doesn't smash into things or get stuck
    def chooseBetter(self):
        self.flushScan()
        ###Tryig to speed up the scan
        for x in range(self.MIDPOINT-60, self.MIDPOINT+60, 5):
            servo(x)
            time.sleep(.1)
            self.scan[x] = us_dist(15)
            time.sleep(.05)
        count = 0
        option = [0]
        for x in range(self.MIDPOINT-60, self.MIDPOINT+60, 5):
            if self.scan[x] > self.STOP_DIST:
                count += 1
            else:
                count=0
            if count> 9:
                print("Found an option from "+ str(x-20)+" to "+ str(x)+ " degrees")
                count = 0
                option.append(x)
                self.dataBase()

#########Ben and I shared the code Mr. A (you) helped create.
######Below is copied from Ben's code to select a path
########I shared him the code above to start this new process
            #this method is basically a remote control for my robot
    def dataBase(self):
        menu = {"1": (" Direction Left Four", self.leftTurn4),
                "2": (" Direction Left Two", self.leftTurn2),
                "3": (" Direction Forward Four", self.forward4),
                "4": (" Direction Forward Eight", self.forward8),
                "5": (" Direction Right Two", self.rightTurn2),
                "6": (" Direction Right Four", self.rightTurn4)}
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        ans = input("Your selection: ")
        menu.get(ans, [None, error])[1]()
        ####BELOW is the Movements my robot will do when selecting an option.  FOR EXAMPLE: Direction Left Four is self.encL(4)
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
        # ans = input("Your selection: ")
        # option.get(ans, [None, error])[1]()
####################################################
############### STATIC FUNCTIONS

def error():
    print('Error in input')

def quit():
    raise SystemExit
####################################################
######## THE ENTIRE APP IS THIS ONE LINE....
g = GoPiggy()
