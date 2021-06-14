#This is a movement test for a quardruped robot
#This code is to be used with an adafruit servo driver and a RPi4
#This code relies on a four point movement cycle
#The goal is to allow the user to cycle through the poses to test basic movement
#Written by Carter Berlind 2021 for Boston University Robotics Lab


import numpy as np
import math
from adafruit_servokit import ServoKit

def inverseKin(x,y,Lua,Lfa):
    A = (1/(Lua*2))*((Lfa^2)-(Lua^2)-(x^2)-(y^2))
    R = math.sqrt((x^2)+(y^2))
    alpha = math.atan(x/y)
    omega = math.asin(A/R) + alpha
    theta = omega + math.pi
    phi =(-1* math.asin((1/Lfa)*(y+Lua*math.sin(-omega))))-omega
    return theta,phi;


class movementTest:
    def __init__(self):
        self.thetaOne = 90
        self.phiOne = 90
        self.thetaTwo = 90
        self.phiTwo = 90
        self.kit = ServoKit(channels=16)
        self.angles = np.zeros((3,4))
        self.neutralAngles = np.array([[90,90,90,90],[90,90,90,90],[90,90,90,90]])
        self.counter = 0
        self.strideLength = 2
        self.strideHeight = .5
        self.COMHeight = 5
        self.upperarmLength = 4
        self.forearmLength = 5
        self.legStance1 = inverseKin((self.strideLength/2),(-1*self.COMHeight),self.upperarmLength,self.forearmLength)
        self.legStance2 = inverseKin(0,(-1*self.COMHeight),self.upperarmLength,self.forearmLength)
        self.legStance3 = inverseKin((-1*self.strideLength/2),(-1*self.COMHeight),self.upperarmLength,self.forearmLength)
        self.legStance4 = inverseKin(0,(-1*self.COMHeight+self.strideHeight),self.upperarmLength,self.forearmLength)
        for i in range (4):
            for j in range (3):
                self.kit.servo[self.counter].angle = self.neutralAngles[j,i]
                self.angles[j,i] = self.neutralAngles[j,i]
                self.counter += 1

    def poseOne(self):
        self.thetaOne = math.degrees(self.legStance1[0])
        self.phiOne = math.degrees(self.legStance1[1])
        self.thetaTwo = math.degrees(self.legStance3[0])
        self.phiTwo = math.degrees(self.legStance3[1])
        self.angles = np.array([[90,90,90,90],[self.thetaOne,(180-self.thetaTwo),self.thetaTwo,(180-self.thetaOne)],[self.phiOne,(180-self.phiTwo),self.phiTwo,(180-self.phiOne)]])
        self.counter = 0
        for i in range (4):
            for j in range (3):
                self.kit.servo[self.counter].angle = self.angles[j,i]
                self.counter += 1

    def poseTwo(self):
        self.thetaOne = math.degrees(self.legStance2[0])
        self.phiOne = math.degrees(self.legStance2[1])
        self.thetaTwo = math.degrees(self.legStance4[0])
        self.phiTwo = math.degrees(self.legStance4[1])
        self.angles = np.array([[90,90,90,90],[self.thetaOne,(180-self.thetaTwo),self.thetaTwo,(180-self.thetaOne)],[self.phiOne,(180-self.phiTwo),self.phiTwo,(180-self.phiOne)]])
        self.counter = 0
        for i in range (4):
            for j in range (3):
                self.kit.servo[self.counter].angle = self.angles[j,i]
                self.counter += 1

    def poseThree(self):
        self.thetaOne = math.degrees(self.legStance3[0])
        self.phiOne = math.degrees(self.legStance3[1])
        self.thetaTwo = math.degrees(self.legStance1[0])
        self.phiTwo = math.degrees(self.legStance1[1])
        self.angles = np.array([[90,90,90,90],[self.thetaOne,(180-self.thetaTwo),self.thetaTwo,(180-self.thetaOne)],[self.phiOne,(180-self.phiTwo),self.phiTwo,(180-self.phiOne)]])
        self.counter = 0
        for i in range (4):
            for j in range (3):
                self.kit.servo[self.counter].angle = self.angles[j,i]
                self.counter += 1

    def poseFour(self):
        self.thetaOne = math.degrees(self.legStance4[0])
        self.phiOne = math.degrees(self.legStance4[1])
        self.thetaTwo = math.degrees(self.legStance2[0])
        self.phiTwo = math.degrees(self.legStance2[1])
        self.angles = np.array([[90,90,90,90],[self.thetaOne,(180-self.thetaTwo),self.thetaTwo,(180-self.thetaOne)],[self.phiOne,(180-self.phiTwo),self.phiTwo,(180-self.phiOne)]])
        self.counter = 0
        for i in range (4):
            for j in range (3):
                self.kit.servo[self.counter].angle = self.angles[j,i]
                self.counter += 1
