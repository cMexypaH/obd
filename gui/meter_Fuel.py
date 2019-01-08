#!/usr/bin/env python

import wx
from math import pi

# Default meter
from meter import Meter

class FuelMeter(Meter):
    def __init__(self, parent, size):
        Meter.__init__(self, parent, 0, 100, 20,
                size=size,
                ticks=["F", "", "", "", "", "E"])

        self.SetAngleRange(-pi/2.5, pi/2.5)
        self.SetMiddleText("fuel")
        self.SetZone(80, 100, wx.RED)
        
        self.SetNumberOfSecondaryTicks(1)
        
        self.SetTicksFont(wx.Font(8,
            wx.FONTFAMILY_SWISS,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL))

        # Startup value
        self.SetSpeedValue(10)

    def Set(self, response):
        #print("Fuel: ", response)
        self.SetSpeedValue(0)#response.value)

