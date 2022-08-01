## parametricCylinder class to draw out a 3d cylinder.
## Author: Kohei Yasui
## 02/17/2022
## CS3388B

import math
from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

# parametricCylinder class for implementing a 3d cylinder to be displayed using cameraMatrix
class parametricCylinder(parametricObject):
    #  init variables like height and radius
    def __init__(self, T=matrix(np.identity(4)), height = 30.0, radius=10.0, color=(255,255,255), reflectance=(0.2,0.4,0.4,1.0), uRange=(0.0,1.0), vRange=(0.0,2.0*pi), uvDelta=(pi/18.0,pi/18.0)):
        super().__init__(T, color, reflectance, uRange, vRange, uvDelta) # call parametricObject superclass
        self.__height = height
        self.__radius = radius

    #gets the point at vector u to v
    def getPoint(self, u, v):
        P = matrix(np.ones((4,1)))
        P.set(0,0, self.__radius*math.sin(v)) # set the x, y, and z values to new values used in cylinder
        P.set(1,0, self.__radius*math.cos(v))
        P.set(2,0, self.__height*u)
        return P

    # setter for radius
    def setRadius(self, radius):
        self.__radius = radius

    #setter for height
    def setHeight(self, height):
        self.__height = height

    #getter for radius
    def getRadius(self):
        return self.__radius

    #getter for height
    def getHeight(self):
        return self.__height

