#!/usr/bin/env python

import wx
from time import sleep
from threading import Thread

# Ui modules
from meter_Speed import SpeedMeter
from meter_RPM import RPMMeter
from meter_Fuel import FuelMeter
from meter_Temp import TempMeter

#DisplaySize = wx.GetDisplaySize()

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=wx.GetDisplaySize())
        MainPanel = wx.Panel(self, size=(800,600))
        MainPanel.SetBackgroundColour(wx.Colour(0,0,255))
        
        panel_KPH = wx.Panel(self, size=(500,500), pos=(0,0))
        panel_RPM = wx.Panel(self, size=(500,500), pos=(500,0))
        panel_Fuel = wx.Panel(self, size=(250,250), pos=(1000,0))
        panel_Temp = wx.Panel(self, size=(250,250), pos=(1000,250))

        #bind on esc key
        self.Bind(wx.EVT_CHAR_HOOK, self.OnKey)
        
        # Eyes burning <remove later>
        panel_KPH.SetBackgroundColour(wx.Colour(255,33,33))
        panel_RPM.SetBackgroundColour(wx.Colour(33,255,33))

        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(panel_KPH,0)
        box.Add(panel_RPM,1)
        MainPanel.SetSizer(box)
        #GridSizer
        #gs = wx.GridSizer(2,1,5,5)
        #gs.Add(self.speedmeter = speedmeter.SpeedMeter(panel))
        #gs.Add(self.speedmeter1 = speedmeter.SpeedMeter(panel1))
        
        # Add speedmeter
        self.Speed = SpeedMeter(panel_KPH)
        self.RPM = RPMMeter(panel_RPM)
        self.Fuel = FuelMeter(panel_Fuel)
        self.Temp = TempMeter(panel_Temp)
		
        self.ShowFullScreen(True)

    def OnKey(self, event):
        key_code = event.GetKeyCode()

        # Exit on escape
        if key_code == wx.WXK_ESCAPE:
            self.Close(True)
        else:
            event.Skip()

    # Called on GUI exit (X btn)
    def OnExit(self, event):
        self.Close(True)

def simulate_data(frame):
    """ TODO: this """
    while True:
        frame.Speed.Set(10)
        frame.RPM.Set(10)
        frame.Fuel.Set(10)
        frame.Temp.Set(10)
        sleep(0.1)

# Test UI only
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainWindow(None, "Main Window")
    frame.Show()

    # DEBUG
    Thread(target=simulate_data, args=frame).start()

    # Blocking
    app.MainLoop()
