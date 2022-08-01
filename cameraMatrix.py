## cameraMatrix class to be used by the program
## Author: Kohei Yasui
## 02/17/2022
## CS3388B

import math
import operator
from math import *
import numpy as np
from matrix import matrix

class cameraMatrix:

    def __init__(self,window,UP,E,G,nearPlane=10.0,farPlane=50.0,theta=90.0):
        self.__UP = UP.normalize()
        self.__E = E
        self.__G = G
        self.__np = nearPlane
        self.__fp = farPlane
        self.__width = window.getWidth()
        self.__height = window.getHeight()
        self.__theta = theta
        self.__aspect = self.__width/self.__height
        self.__npHeight = self.__np*(pi/180.0*self.__theta/2.0)
        self.__npWidth = self.__npHeight*self.__aspect

        Mp = self.__setMp(self.__np,farPlane)
        T1 = self.__setT1(self.__np,self.__theta,self.__aspect)
        S1 = self.__setS1(self.__np,self.__theta,self.__aspect)
        T2 = self.__setT2()
        S2 = self.__setS2(self.__width,self.__height)
        W2 = self.__setW2(self.__height)

        self.__N = (self.__E - self.__G).removeRow(3).normalize()
        self.__U = self.__UP.removeRow(3).crossProduct(self.__N).normalize()
        self.__V = self.__N.crossProduct(self.__U)

        self.__Mv = self.__setMv(self.__U,self.__V,self.__N,self.__E)
        self.__C = W2*S2*T2*S1*T1*Mp
        self.__M = self.__C*self.__Mv

    # sets and returns the MV matrix used for the camera
    def __setMv(self,U,V,N,E):
        mv = matrix(np.identity(4))

        vec_list = [U, V, N] # order U V N in a list

        for i in range(0, 3): # iterate through the vectors to set the matrix values to appropriate numbers
            current_vector = vec_list[i]
            mv.set(i, 0, current_vector.get(0, 0))
            mv.set(i, 1, current_vector.get(1, 0))
            mv.set(i, 2, current_vector.get(2, 0))

        E = E.scalarMultiply(-1) # scalar multiply the E value by -1 and insert plain 0's to match the vectors
        U = U.insertRow(3, 0)
        V = V.insertRow(3, 0)
        N = N.insertRow(3, 0)

        dot_u = E.dotProduct(U) # find dot product of all three values to add to the last column
        mv.set(0, 3, dot_u)
        dot_v = E.dotProduct(V)
        mv.set(1, 3, dot_v)
        dot_n = E.dotProduct(N)
        mv.set(2, 3, dot_n)

        return mv

    #MP matrix to be used in the matrix
    def __setMp(self,nearPlane,farPlane):
        mp = matrix(np.identity(4))

        b = (-2 * farPlane * nearPlane) / (farPlane - nearPlane) # calculate b and a values

        a = (nearPlane + b) / nearPlane

        mp.set(0, 0, nearPlane) # replace appropriate values
        mp.set(1, 1, nearPlane)
        mp.set(3, 2, -1)
        mp.set(3, 3, 0)
        mp.set(2, 2, a)
        mp.set(2, 3, b)

        return mp
    ## sets and returns the t1 matrix to be used in the camera
    def __setT1(self,nearPlane,theta,aspect):
        t1 = matrix(np.identity(4))

        t = nearPlane * math.tan((math.pi / 180) * (theta / 2)) # find t value using the formula
        b = -1 * t

        r = aspect * t
        l = -1 * r  # negate r and t to get the rest of the values

        t1.set(0, 3, (-1 * (r+l))/2)
        t1.set(1, 3, (-1 * (t+b))/2) # set matrix indexes accordingly

        return t1

    ## sets and returns the s1 matrix to be used in the camera
    def __setS1(self,nearPlane,theta,aspect):
        s1 = matrix(np.identity(4))

        t = nearPlane * math.tan((math.pi/180) * (theta/2)) ## calculate t value
        b = -1 * t

        r = aspect * t ## set respective values again
        l = -1 * r

        s1.set(0, 0, 2/(r-l)) ## replace the matrix values
        s1.set(1, 1, 2/(t-b))

        return s1

    ## sets and returns the t2 matrix to be used in the camera
    def __setT2(self):
        t2 = matrix(np.identity(4))
        t2.set(0, 3, 1) ## sets (0,3) and (1,3) to 1 to finalize the matrix
        t2.set(1, 3, 1)
        return t2

    ## sets and returns the s2 matrix to be used in the camera
    def __setS2(self,width,height):
        s2 = matrix(np.identity(4))
        s2.set(0,0, width/2)  # replace values with half of width and height
        s2.set(1,1, height/2)
        return s2

    ## sets and returns w2 to be used in the camera
    def __setW2(self,height):
        w = matrix(np.identity(4))
        w.set(1,1,-1)
        w.set(1,3,height) ## set to -1 and height in respective indexes
        return w

        
    def worldToViewingCoordinates(self,P):
        return self.__Mv*P

    def worldToImageCoordinates(self,P):
        return self.__M*P

    def worldToPixelCoordinates(self,P):
        return self.__M*P.scalarMultiply(1.0/(self.__M*P).get(3,0))

    def viewingToImageCoordinates(self,P):
        return self.__C*P

    def viewingToPixelCoordinates(self,P):
        return self.__C*P.scalarMultiply(1.0/(self.__C*P).get(3,0))

    def imageToPixelCoordinates(self,P):
        return P.scalarMultiply(1.0/P.get(3,0))

    def getUP(self):
        return self.__UP

    def getU(self):
        return self.__U

    def getV(self):
        return self.__V

    def getN(self):
        return self.__N

    def getE(self):
        return self.__E

    def getG(self):
        return self.__G

    def getMv(self):
        return self.__Mv

    def getC(self):
        return self.__C

    def getM(self):
        return self.__M

    def getNp(self):
        return self.__np

    def getFp(self):
        return self.__fp

    def getTheta(self):
        return self.__theta

    def getAspect(self):
        return self.__aspect

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getNpHeight(self):
        return self.__npHeight

    def getNpWidth(self):
        return self.__npWidth