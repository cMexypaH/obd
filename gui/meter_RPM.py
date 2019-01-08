#!/usr/bin/env python

import wx
from math import pi

# Default meter
from meter import Meter

class RPMMeter(Meter):
    def __init__(self, parent, size):
        Meter.__init__(self, parent, 0, 6000, 500,
                size=size)

        self.SetAngleRange(-pi/6, 7*pi/6)
        self.SetMiddleText("RPM")
        self.SetZone(4800, 6000, wx.RED)
        self.SetNumberOfSecondaryTicks(4)

        # Startup value
        self.SetSpeedValue(10)

    def Set(self, response):
        print("RPM: ", response)
        self.SetSpeedValue(response)

