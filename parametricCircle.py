## parametricCircle class to draw out a 2d circle.
## Author: Kohei Yasui
## 02/17/2022
## CS3388B

import math
from math import *
import numpy as np
from matrix import matrix
from parametricObject import parametricObject

## This class implements the parametric circle to be displayed by the camera
class parametricCircle(parametricObject):
    ## init all variables necessary to be used in the camera
    def __init__(self, T=matrix(np.identity(4)), radius=10.0, color=(255,255,255), reflectance=(0.2,0.4,0.4,1.0), uRange=(0.0,pi), vRange=(0.0,2.0*pi), uvDelta=(pi/18.0,pi/18.0)):
        super().__init__(T, color, reflectance, uRange, vRange, uvDelta) # call the parametricObject superclass.
        self.__radius = radius

    # gets the vector point of u,v
    def getPoint(self, u, v):
        P = matrix(np.ones((4,1)))
        P.set(0,0,self.__radius*u*math.cos(v)) # replace x
        P.set(1,0, self.__radius*u*math.sin(v)) # replace y
        P.set(2,0,0) # set z to 0
        return P

    ##sets radius to new value
    def setRadius(self, radius):
        self.__radius = radius

    # gets radius
    def getRadius(self):
        return self.__radius