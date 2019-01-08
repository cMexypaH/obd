#!/usr/bin/env python

import sys

import obd

# GUI
sys.path.append('./gui/')
import wx
from main_window import MainWindow

from time import sleep

# Test thread
from threading import Thread
from math import ceil

def test_callback(response):
    print(response)

''' Commented for testing
# Init
obd_connection = obd.Async()#"\.\COM4")
# Callback is called when data is received
obd_connection.watch(obd.commands.RPM)
obd_connection.watch(obd.commands.SPEED)
obd_connection.watch(obd.commands.GET_DTC)
obd_connection.watch(obd.commands.DISTANCE_W_MIL)
obd_connection.watch(obd.commands.COOLANT_TEMP)
obd_connection.watch(obd.commands.STATUS, callback=test_callback)

#obd_connection.watch(obd.commands[1][166])
'''

# DEBUG
def test():
    kph = 0
    rpm = 0
    temp = 0
    
    while True:
        frame.Speed.Set(kph)
        frame.RPM.Set(rpm)
        frame.Temp.Set(temp)
        
        value_KPH = 100
        value_RPM = 2500
        value_TEMP = 80
        
        '''  Commented for testing
        obd_connection.stop()
        value_RPM = obd_connection.query(obd.commands.RPM)
        value_KPH = obd_connection.query(obd.commands.SPEED)
        value_TEMP = obd_connection.query(obd.commands.COOLANT_TEMP)
        value_FUEL = obd_connection.query(obd.commands.DISTANCE_W_MIL)
        #supp = obd_connection.query(obd.commands[1][166])
        rpm = value_RPM     #ne sa testvani
        kph = value_KPH     #ne sa testvani
        print("value temp: "+str(value_TEMP))
        print("value fuel: "+str(value_FUEL))
        # print("value RPM: "+str(value_RPM.magnitude))
        print("rpm: "+str(rpm))
        #print(supp)
        '''
        # Testvano i raboti
        kph_str=str(value_KPH)
        if kph_str=="None":
            kph_str="0"
        kph=int(kph_str.split()[0])
        rpm_str=str(value_RPM)
        if rpm_str=="None":
            rpm_str="0"
        rpm=ceil(float(rpm_str.split()[0]))
        temp_str=str(value_TEMP)
        if temp_str=="None":
            temp_str="0"
        temp=int(temp_str.split()[0])
        
        '''  Commented for testing
        print(obd_connection.query(obd.commands.GET_DTC))
        print(obd.commands.has_pid(1, 166))

        #for i in range(0,95):
        #print("PID " + str(i) + " --- " + str(obd_connection.query(obd.commands[1][i])))

        obd_connection.start()
        '''


# Entry point
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainWindow(None, "Main Window")
    frame.Show()

    # DEBUG
    Thread(target=test).start()

    # Blocking
    app.MainLoop()


