import math
from adafruit_servokit import ServoKit
import time

class sevoTest:
    def __init__(self):
        self.kit = ServoKit(channels=16)
        self.kit.servo[0].angle = 90
        self.kit.continuous_servo[0].throttle = 1
        time.sleep(1)
        self.kit.continuous_servo[0].throttle = -1
        time.sleep(1)
        self.kit.continuous_servo[0].throttle = 0

    
