# -*- coding: utf-8 -*-
################################################################################
##Author:        Carlos Asmat
##Creation Date: 2010-11-17
##Title:         SSC32 Protocol Library
##Description:   Set of functions allowing the communication with
##               Pololu devices using the Lynxmotion SSC32 protocol.
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
##      This is a small library with functions that allow to instantiate
##      and control the Lynxmotion SSC32 motor controllers using the SSC32 protocol.
##
################################################################################

#Defining values
ch = "#"
pos = "P"
spe = "S"
tim = "T"
cr = 13

maxpulse = 2400
minpulse = 650

def send_command(port, channel, position):
    """Sends a command using the SSC-32 protocol."""
    print ch + str(channel) + pos +  str(position) +  chr(cr)
    port.write(ch + str(channel) + pos +  str(position) +  chr(cr))

class Servo:
    """Servo motor object to be use with the Micro serial servo controller. It can be instantiated in order
    to control servos individually by setting position and speed."""
    def __init__(self, serialPort, pulse180, pulse90, servo_number = 0):
        """Initialize a servo controller object by assigning a serial port,
        a device number (the number of the first servo), a max and min
        rotation values corresponding to the 0 deg ans 180 deg positions respectively."""
        self.port = serialPort
        self.servo_num = servo_number
        self.max_val = pulse180
        self.min_val = pulse90

    def __compute_data(self, angle):
        a = (self.max_val - self.min_val)/90.0
        b = self.max_val-180.0*a
        return angle * a + b

    def set_pos(self, pos = 90):
        data = int(self.__compute_data(pos))
        send_command(self.port, self.servo_num, data)
        print data

    def set_speed(self, speed = 127):
        send_command_single(self.port, self.__dev_id, 0x01, self.servo_num, speed)

