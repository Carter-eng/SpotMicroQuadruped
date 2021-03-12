
from adafruit_servokit import ServoKit
import numpy as np


class servoPrep:
    def __init__(self):
        self.kit = ServoKit(channels=16)
        self.angles = np.zeros((3,4))
        self.neutralAngles = np.array([90,90,90,90],[135,135,135,135],[90,90,90,90])
    def servoBounds(self):
        counter = 0
        for i in range (4):
            for j in range (3):
                self.angles[j,i] = 0
                self.kit.servo[counter].angle = self.angles[j,i]
                print('Servo set to 0\n')
                value = input('press any key and enter to continue\n')
                self.angles[j,i] = 180
                self.kit.servo[counter].angle = self.angles[j,i]
                print('Servo set to 180\n')
                value = input('press any key and enter to continue\n')
                self.angles[j,i] = 90
                self.kit.servo[counter].angle = self.angles[j,i]
                print('Servo set to 90\n')
                value = input('press any key and enter to continue\n')
                self.angles[j,i] = self.neutralAngles[j,i]
                self.kit.servo[counter].angle = self.angles[j,i]
                print('Servo set to neutral angle\nThis is the angle where it stands noramlly\n')
                self.kit.servo[counter].angle = adjustAngle(self.angles[j,i])
                print('complete')
                return self.angles
    def adjustAngle(angle):
        value = input('press w to add 5 degrees, s to subtract 5, and a main the same\n')
        if value == 'a':
            return angle
        elif value == 'w':
            angle = angle + 5
            print('5 degrees were added\n')
            angle = adjustAngle(angle)
            return angle
        elif value == 's':
            angle = angle - 5
            print('5 degrees were subtracted\n')
            angle = adjustAngle(angle)
            return angle
        else:
            angle = adjustAngle(angle)
            return angle
servoPrep.servoBounds(self)
