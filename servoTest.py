import math
from adafruit_servokit import ServoKit
import keyboard

class sevoTest:
    def __init__(self):
        self.kit = ServoKit(channels=16)
        self.kit.servo[0].angle = 90
        self.kit.servo[1].angle = 90
        self.kit.servo[2].angle = 90

    def on_press(key):
        while 1 == 1:
            if key.char in ['q']:
                self.self.kit.servo[0].angle += 5
            if key.char in ['a']:
                self.self.kit.servo[0].angle += -5
            if key.char in ['w']:
                self.self.kit.servo[1].angle += 5
            if key.char in ['s']:
                self.self.kit.servo[1].angle += -5
            if key.char in ['e']:
                self.self.kit.servo[2].angle += 5
            if key.char in ['d']:
                self.self.kit.servo[2].angle += -5
        
