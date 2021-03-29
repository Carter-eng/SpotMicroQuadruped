
from adafruit_servokit import ServoKit
import numpy as np



def servoBounds():
    kit = ServoKit(channels=16)
    angles = np.zeros((3,4))
    neutralAngles = np.array([[90,90,90,90],[135,135,135,135],[90,90,90,90]])
    counter = 0
    for i in range (4):
        for j in range (3):
            angles[j,i] = 0
            kit.servo[counter].angle = angles[j,i]
            print('Servo set to 0\n')
            value = input('press any key and enter to continue\n')
            angles[j,i] = 180
            kit.servo[counter].angle = angles[j,i]
            print('Servo set to 180\n')
            value = input('press any key and enter to continue\n')
            angles[j,i] = 90
            kit.servo[counter].angle = angles[j,i]
            print('Servo set to 90\n')
            value = input('press any key and enter to continue\n')
            angles[j,i] = neutralAngles[j,i]
            kit.servo[counter].angle = angles[j,i]
            print('Servo set to neutral angle\nThis is the angle where it stands noramlly\n')
            kit.servo[counter].angle = adjustAngle(angles[j,i])
            print('complete')
            
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

    
servoBounds()
