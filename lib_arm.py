# -*- coding: utf-8 -*-
################################################################################
##Author:        Carlos Asmat
##Creation Date: 2010-11-17
##Title:         Robotic Arm Library
##Description:   
##
##Copyright: Carlos Asmat, 2010
##License:
##      This program is free software: you can redistribute it and/or modify
##      it under the terms of the GNU General Public License as published by
##      the Free Software Foundation, either version 3 of the License, or
##      (at your option) any later version.
##
##      This program is distributed in the hope that it will be useful,
##      but WITHOUT ANY WARRANTY; without even the implied warranty of
##      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##      GNU General Public License for more details.
##
##      You should have received a copy of the GNU General Public License
##      along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
##Description:
##
################################################################################

import math

def get_angles(x=100.0, y=100.0, z=100.0, L=244.0, M=325.0, N=90.0):
    """Computes the angels in degrees from x, y, z coordinates in mm"""
    
    R = math.sqrt(math.pow(x, 2) + math.pow(y, 2))
    s = R - N 
    Q = math.sqrt(math.pow(s, 2) + math.pow(z, 2)) #EQ 1
    f = math.atan2(z, s)     #EQ 2
    g = math.acos((math.pow(L, 2) + math.pow(Q, 2) - math.pow(M, 2)) / (2*L*Q))
    
    # angles
    a = f + g
    b = math.acos((math.pow(M, 2) + math.pow(L, 2) - math.pow(Q, 2)) / (2*L*M)) #EQ 7
    c = -b - a + 2* math.pi
    d = math.atan2(x, y)

    a = (180*a)/math.pi
    b = (180*b)/math.pi
    c = (180*c)/math.pi
    d = (180*d)/math.pi

    print a, ", " , b, ", ", c,", ", d
    return [a, b, c, d]

def go_home():
    """Go to home position"""
    base.set_pos(90)
    shoulder.set_pos(90)
    elbow.set_pos(180)
    wrist.set_pos(180)

def go_coordinate(x, y, z):
    """Go to coordinate x, y, z in mm"""
    h = -18 #height offset
    T = 9 #lenght offset
    
    s = get_angles(x, y, z-h, 243.0,324.0, 15.0+T)

    shoulder.set_pos(s[0])
    elbow.set_pos(s[1])
    wrist.set_pos(s[2])
    base.set_pos(s[3])

    
