#!/usr/bin/env python

from time import sleep
from threading import Thread
import wx
import obd

import speedmeter

# Init
obd_connection = obd.Async()
# Callback is called when data is received
#obd_connection.watch(obd.commands.RPM, callback=None)

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300,300))
        panel = wx.Panel(self)

        # Eyes burning <remove later>
        panel.SetBackgroundColour(wx.Colour(33,33,33))

        # Start
        self.btn_start_stop = wx.Button(panel, label="Start")
        self.btn_start_stop.Bind(wx.EVT_BUTTON, self.OnStartStop)

        # Add speedmeter
        self.speedmeter = speedmeter.SpeedMeter(panel)

    # Start_Stop button
    def OnStartStop(self, event):
        obd_connection.start()
        print("Started")

    # Called on GUI exit (X btn)
    def OnExit(self, event):
        self.Close(True)

# DEBUG
def test():
    speed = 0
    while frame.speedmeter:
        frame.speedmeter.Set(speed)
        speed += 1
        if speed > 199:
            speed = 0
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


