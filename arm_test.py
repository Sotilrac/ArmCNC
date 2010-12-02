# -*- coding: utf-8 -*-
################################################################################
##Author:        Carlos Asmat
##Creation Date: 2010-11-17
##Title:         Robotic Arm Test Program
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

import serial
import time

#Open serial port
port = serial.Serial('/dev/ttyUSB0')
port.baudrate=115200 #set an appropriate baudrate
# send_command(port, 0,1405)
# send_command(port, 1,920)
# send_command(port, 2,1160)
# send_command(port, 3,1145)

base = Servo(port, 1123, 1400, 0)
shoulder = Servo(port, 680, 957, 1)
elbow = Servo(port, 1167, 877, 2)
wrist = Servo(port, 1145, 880, 3)

x = 300.0
y = -200.0
z = -20.0

sleepD = 0.001
steps = 1

# go_home()

go_coordinate(200,100,0)
time.sleep(1)

##for y in range(0,200.0, steps):
##    go_coordinate(200.0, y, 0.0)
##    time.sleep(sleepD)
##    
##time.sleep(1.5)
##for x in range(200.0,300.0, steps):
##    go_coordinate(x, 200, 0.0)
##    time.sleep(sleepD)
##
##time.sleep(1.5)
##
##for y in range(200.0,0.0, -1*steps):
##    go_coordinate(300, y, 0.0)
##    time.sleep(sleepD)
##
##time.sleep(1.5)
##
##for x in range(300.0,200.0, -1*steps):
##    go_coordinate(x, 0.0, 0.0)
##    time.sleep(sleepD)

r = 100.0

for y in range(100.0, 300.0, steps):
    x = math.sqrt(math.pow(r, 2) - math.pow(y-200.0, 2))+200.0
    go_coordinate(x, y, 0.0)
    time.sleep(sleepD)
