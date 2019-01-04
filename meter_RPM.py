#!/usr/bin/env python

from math import pi, ceil

import wx
import wx.lib.agw.speedmeter as SM

class SpeedMeter(SM.SpeedMeter):

   def __init__(self, parent):
       SM.SpeedMeter.__init__(self,
               parent,
               agwStyle=SM.SM_DRAW_HAND|SM.SM_DRAW_MIDDLE_TEXT|SM.SM_DRAW_SECONDARY_TICKS|SM.SM_DRAW_PARTIAL_SECTORS,
               size=(500,500),
               pos=(10, 30))
      
       self.SetAngleRange(-pi/6, 7*pi/6)
       self.SetMiddleText("RPM")

       # Intervals
       intervals = range(0, 6001, 500)
       self.SetIntervals(intervals)
       ticks = [str(i) for i in intervals]
       self.SetTicks(ticks)

       # Colors
       self.SetTicksColour(wx.WHITE)
       self.SetSpeedBackground(wx.BLACK)
       
       # Setting 20% at end to be red coloured
       length_colours = len(intervals)-1
       red_colours = ceil(length_colours*20/100)
       black_colours = length_colours-red_colours
       red_colours_list = [wx.RED]*(red_colours)
       interval_colours = [wx.BLACK]*(black_colours)
       interval_colours.extend(red_colours_list)
       
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
       
       # Set start value
       self.SetSpeedValue(int(0))

   def Set(self, value):
       self.SetSpeedValue(int(value))
       self.Refresh()
