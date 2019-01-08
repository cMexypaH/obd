#!/usr/bin/env python

from math import pi, ceil

import wx
from wx.lib.agw.speedmeter import\
    SpeedMeter,\
    SM_DRAW_HAND,\
    SM_DRAW_MIDDLE_TEXT,\
    SM_DRAW_PARTIAL_SECTORS,\
    SM_DRAW_SECONDARY_TICKS 

class Meter(SpeedMeter):
    def __init__(self, parent, low=0, high=100, step=10, ticks=None):
        SpeedMeter.__init__(self, parent,\
                agwStyle=SM_DRAW_HAND|\
                SM_DRAW_MIDDLE_TEXT|\
                SM_DRAW_SECONDARY_TICKS|\
                SM_DRAW_PARTIAL_SECTORS)

        # Defaults
        self.SetAngleRange(-pi/6, 7*pi/6)
        self.SetMiddleText("MiddleText")

        # Intervals
        intervals = range(low, high+1, step)
        self.SetIntervals(intervals)

        # Fallback to numbers if ticks is None
        if ticks is None:
            ticks = [str(i) for i in intervals]

        self.SetTicks(ticks)

        # Default colors
        self.SetTicksColour(wx.WHITE)
        self.SetSpeedBackground(wx.BLACK)

        self.SetIntervalColours([wx.BLACK] * (len(intervals)-1))
        self.SetHandColour(wx.Colour(255,50,0))
        self.SetMiddleTextColour(wx.WHITE)

        # Divide in 5 pieces
        self.SetNumberOfSecondaryTicks(4)
 
        # Fonts
        self.font_ticks = wx.Font(15,
            wx.FONTFAMILY_SWISS,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL)
        self.SetTicksFont(self.font_ticks)
        self.font_mid_text = wx.Font(20,
            wx.FONTFAMILY_SWISS,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_BOLD)
        self.SetMiddleTextFont(self.font_mid_text)

        # Remove arc (visible on non-black bg)
        self.DrawExternalArc(False)
 
        # Set start value
        self.SetSpeedValue(0)

    # Set warning zone
    def SetZone(self, start, end, colour):
        colours = self.GetIntervalColours()
        for index, value in enumerate( self.GetIntervals() ):
            if value >= start and value < end:
                colours[index] = colour
        self.SetIntervalColours(colours)

    # This is meant to be overriden
    def Set(self, value):
        self.SetSpeedValue(int(value))

