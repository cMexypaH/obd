
#!/usr/bin/env python

import wx
from math import pi

# Default meter
from meter import Meter

class TempMeter(Meter):
    def __init__(self, parent):
        Meter.__init__(self, parent, 0, 60, 15)

        self.SetAngleRange(-pi/6, 7*pi/6)
        self.SetMiddleText("C°")
        self.SetZone(4800, 6000, wx.RED)
        self.SetNumberOfSecondaryTicks(4)

        # Startup value
        self.SetSpeedValue(10)

    def Set(self, response):
        print("Temp: ", response)
        self.SetSpeedValue(0)#response)

