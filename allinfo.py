# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 14:40:11 2018

@author: Vesko
"""
from obd import OBDCommand, Unit
from obd.protocols import ECU
from obd.utils import bytes_to_int


import obd
obd.logger.setLevel(obd.logging.DEBUG)
connection = obd.OBD("\.\COM4") # connect to the first port in the list



for i in range(0,100):
    if not obd.commands[6][i]:
        print("PID: " + str(i) + " NEMA")
    else:
        print("PID Number: " + str(i) + " Name: " + obd.commands[6][i].name)
        print(connection.query(obd.commands[1][i])) # send the command, and parse the response
        print("")

connection.close()




