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
        MainPanel = wx.Panel(self, size=(800,480))
        MainPanel.SetBackgroundColour(wx.Colour(0,0,255))
        
        panel_KPH = wx.Panel(self, size=(300,300), pos=(100,90))
        panel_RPM = wx.Panel(self, size=(300,300), pos=(400,90))
        panel_Fuel = wx.Panel(self, size=(100,100), pos=(0,190))
        panel_Temp = wx.Panel(self, size=(100,100), pos=(700,190))
        
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
        self.Speed = SpeedMeter(panel_KPH, panel_KPH.GetSize())
        self.RPM = RPMMeter(panel_RPM, panel_RPM.GetSize())
        self.Fuel = FuelMeter(panel_Fuel, panel_Fuel.GetSize())
        self.Temp = TempMeter(panel_Temp, panel_Temp.GetSize())
		
        self.ShowFullScreen(True)

        # Bind OnKey event
        self.Bind(wx.EVT_CHAR_HOOK, self.OnKey)

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

