#!/usr/bin/env python

import wx
from math import pi

# Default meter
from meter import Meter

class FuelMeter(Meter):
    def __init__(self, parent):
        Meter.__init__(self, parent, 0, 100, 20,
                ticks=["F", "", "", "", "", "E"])

        self.SetAngleRange(-pi/6, pi/6)
        self.SetMiddleText("fuel")
        self.SetZone(80, 100, wx.RED)
        #self.SetFontSize(15, 20)

        # Startup value
        self.SetSpeedValue(10)

    def Set(self, response):
        print("Fuel: ", response)
        self.SetSpeedValue(0)#response.value)

