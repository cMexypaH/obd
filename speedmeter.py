#!/usr/bin/env python

from math import pi

import wx
import wx.lib.agw.speedmeter as SM

class SpeedMeter(SM.SpeedMeter):

   def __init__(self, parent):
       SM.SpeedMeter.__init__(self,
               parent,
               agwStyle=SM.SM_DRAW_HAND|SM.SM_DRAW_SECTORS|SM.SM_DRAW_MIDDLE_TEXT|SM.SM_DRAW_SECONDARY_TICKS,
               size=(500,500),
               pos=(10, 30))
      
       self.SetAngleRange(-pi/6, 7*pi/6)
       self.SetMiddleText("Km/h")

       # Intervals
       intervals = range(0, 201, 10)
       self.SetIntervals(intervals)
       ticks = [str(i) for i in intervals]
       self.SetTicks(ticks)

       # Colors
       self.SetTicksColour(wx.WHITE)
       self.SetSpeedBackground(wx.BLACK)
       interval_colours = [wx.BLACK]*(len(intervals)-1)
       self.SetIntervalColours(interval_colours)
       self.SetHandColour(wx.Colour(255,50,0))
       self.SetMiddleTextColour(wx.WHITE)

       # Divide in 5 pieces
       self.SetNumberOfSecondaryTicks(4)

       # Fonts
       self.SetTicksFont(
               wx.Font(15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
       self.SetMiddleTextFont(
               wx.Font(20, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

       # Remove arc (visible on non-black bg)
       self.DrawExternalArc(False)

   def Set(self, value):
       self.SetSpeedValue(int(value))
       self.Refresh()
