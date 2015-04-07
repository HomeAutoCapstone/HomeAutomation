__author__ = 'AtwoodWang'

import math

def distance(x1,x2,y1,y2):
    x=abs(x1-x2)
    y=abs(y1-y2)
    D=math.sqrt(x*x+y*y)
    return D
