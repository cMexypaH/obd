
#!/usr/bin/env python

import wx
from math import pi

# Default meter
from meter import Meter

class TempMeter(Meter):
    def __init__(self, parent, size):
        Meter.__init__(self, parent, 0, 60, 15,
                size=size,
                ticks=["120","","90","","60"])

        self.SetAngleRange(-pi/2.5, pi/2.5)
        self.SetMiddleText("C°")
        self.SetZone(0, 5, wx.RED)
        self.SetNumberOfSecondaryTicks(2)
        self.SetMiddleTextFont(wx.Font(5,
            wx.FONTFAMILY_SWISS,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_BOLD))
        self.SetTicksFont(wx.Font(6,
            wx.FONTFAMILY_SWISS,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL))
        self.ClearBackground()

        # Startup value
        self.SetSpeedValue(10)

    def Set(self, response):
        #print("Temp: ", response)
        if response>=120:
           value=120
        if response<=60:
           value=60
        else: 
           value=response
        self.SetSpeedValue(120-int(value))
        self.SetMiddleText(str(response)+"C°")

