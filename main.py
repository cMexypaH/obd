#!/usr/bin/env python

from time import sleep
from threading import Thread
import wx
import obd

import meter_Speed
import meter_RPM

# Init
#obd_connection = obd.Async()
# Callback is called when data is received
#obd_connection.watch(obd.commands.RPM, callback=None)

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(550,550))
        panel = wx.Panel(self, size=(550,550), pos=(0,0))
        panel1 = wx.Panel(self, size=(550,550), pos=(550,0))

        #bind on esc key
        self.Bind(wx.EVT_CHAR_HOOK, self.onKey)
        
        # Eyes burning <remove later>
        panel.SetBackgroundColour(wx.Colour(33,33,33))
        panel1.SetBackgroundColour(wx.Colour(33,33,33))

        #GridSizer
        #gs = wx.GridSizer(2,1,5,5)
        #gs.Add(self.speedmeter = speedmeter.SpeedMeter(panel))
        #gs.Add(self.speedmeter1 = speedmeter.SpeedMeter(panel1))
        
        # Start
        #self.btn_start_stop = wx.Button(panel, label="Start")
        #self.btn_start_stop.Bind(wx.EVT_BUTTON, self.OnStartStop)

        # Add speedmeter
        self.Speed = meter_Speed.SpeedMeter(panel)
        self.RPM = meter_RPM.SpeedMeter(panel1)
		
		
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
    speed = 0
    rpm = 0
    while True:
        frame.Speed.Set(speed)
        frame.RPM.Set(rpm)
        speed += 1
        rpm += 100
        if speed > 199:
            speed = 0
        elif rpm > 6000:
            rpm = 0
        sleep(0.2)

# Entry point
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainWindow(None, "Main Window")
    frame.Show()

    # DEBUG
    Thread(target=test).start()

    # Blocking
    app.MainLoop()


