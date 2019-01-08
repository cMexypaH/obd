#!/usr/bin/env python

import wx
from math import pi

# Default meter
from meter import Meter

class SpeedMeter(Meter):
    def __init__(self, parent, size):
        Meter.__init__(self, parent, 0, 200, 10,
                size=size)

        self.SetAngleRange(-pi/6, 7*pi/6)
        self.SetMiddleText("Km/h")
        self.SetZone(180,200, wx.RED)
        self.SetNumberOfSecondaryTicks(4)

        # Startup value
        self.SetSpeedValue(10)

    def Set(self, response):
        #print("Fuel: ", response)
        #print("FuelMag: ", response.value.magnitude )
        self.SetSpeedValue(response)

