## parametricPlane class to draw out a 2d plane.
## Author: Kohei Yasui
## 02/17/2022
## CS3388B

import math
from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

# this class implements a 2d plane to be used by the camera matrix
class parametricPlane(parametricObject):
    ## init variables like width and length
    def __init__(self, T=matrix(np.identity(4)), width=10.0, length = 10.0, color=(255,255,255), reflectance=(0.2,0.4,0.4,1.0), uRange=(0.0,1.0), vRange=(0.0,2.0*pi), uvDelta=(pi/18.0,pi/18.0)):
        super().__init__(T, color, reflectance, uRange, vRange, uvDelta) ## call parametricObject superclass
        self.__width = width
        self.__length = length

    # gets the point at u, v
    def getPoint(self,u,v):
        P = matrix(np.ones((4, 1)))
        P.set(0,0, self.__width*u) ## replace values corresponding to the formulas
        P.set(1,0, self.__length * v)
        P.set(2,0, 0)
        return P

    # setter for width
    def setWidth(self, width):
        self.__width = width

    #setter for length
    def setLength(self, length):
        self.__length = length

    #getter for width
    def getWidth(self):
        return self.__width

    #getter for length.
    def getLength(self):
        return self.__length
