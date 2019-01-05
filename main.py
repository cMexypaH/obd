#!/usr/bin/env python

from time import sleep
from threading import Thread
from math import ceil
import wx
import obd

import meter_Speed
import meter_RPM

''' Commented for testing
# Init
obd_connection = obd.Async("\.\COM4")
# Callback is called when data is received
obd_connection.watch(obd.commands.RPM)
obd_connection.watch(obd.commands.SPEED)
obd_connection.watch(obd.commands.GET_DTC)
'''
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(550,550))
        MainPanel = wx.Panel(self)
        MainPanel.SetBackgroundColour(wx.Colour(0,0,255))
        panel = wx.Panel(self, size=(500,500), pos=(50,50))
        panel1 = wx.Panel(self, size=(500,500), pos=(550,0))

        #bind on esc key
        self.Bind(wx.EVT_CHAR_HOOK, self.onKey)
        
        # Eyes burning <remove later>
        panel.SetBackgroundColour(wx.Colour(255,33,33))
        panel1.SetBackgroundColour(wx.Colour(33,255,33))


        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(panel,1)
        box.Add(panel1,1)
        MainPanel.SetSizer(box)
        #GridSizer
        #gs = wx.GridSizer(2,1,5,5)
        #gs.Add(self.speedmeter = speedmeter.SpeedMeter(panel))
        #gs.Add(self.speedmeter1 = speedmeter.SpeedMeter(panel1))
        
        '''
        # Start
        self.btn_start_stop = wx.Button(MainPanel, label="Start")
        self.btn_start_stop.Bind(wx.EVT_BUTTON, self.OnStartStop)
        '''
        
        # Add speedmeter
        self.Speed = meter_Speed.SpeedMeter(panel,panel.GetSize())
        self.RPM = meter_RPM.SpeedMeter(panel1,panel1.GetSize())
		
		
        self.ShowFullScreen(True)

    # Start_Stop button
    def OnStartStop(self, event):
        obd_connection.start()
        print("Started")
        
    def onKey(self, event):
        """
        Check for ESC key press and exit is ESC is pressed
        """
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_ESCAPE:
            self.Close(True)
        else:
            event.Skip()

    # Called on GUI exit (X btn)
    def OnExit(self, event):
        self.Close(True)

# DEBUG
def test():
    kph = 0
    rpm = 0
    while True:
        frame.Speed.Set(kph)
        frame.RPM.Set(rpm)

        sleep(0.2)
        '''  Commented for testing
        obd_connection.stop()
        value = obd_connection.query(obd.commands.RPM)
        value_KPH =obd_connection.query(obd.commands.SPEED)
        rpm = value.value.magnitude  #ne sa testvani
        kph = value_KPH.magnitude    #ne sa testvani
        '''
        ''' Testvano i raboti
        kph_str=str(value_KPH)
        if kph_str=="None":
            kph_str="0"
        kph=int(kph_str.split()[0])
        rpm_str=str(value)
        if rpm_str=="None":
            rpm_str="0"
        rpm=ceil(float(rpm_str.split()[0]))
        '''
        '''  Commented for testing
        print(obd_connection.query(obd.commands.GET_DTC))
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


