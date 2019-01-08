#!/usr/bin/env python

from math import pi, ceil

import wx
import wx.lib.agw.speedmeter as SM

class TempMeter(SM.SpeedMeter):
    def __init__(self, parent, size=(300,300), pos=(0,0)):
        SM.SpeedMeter.__init__(self,
                parent,
                agwStyle=SM.SM_DRAW_HAND|SM.SM_DRAW_MIDDLE_TEXT|SM.SM_DRAW_SECONDARY_TICKS|SM.SM_DRAW_PARTIAL_SECTORS,
                size=size,
                pos=pos)
        
        self.SetAngleRange(-pi/6, pi/6)
        self.SetMiddleText("C°")

        # Intervals
        intervals = range(0, 61, 15)
        self.SetIntervals(intervals)
        ticks = [str(i) for i in intervals]
        empty_ticks = [""]*(len(intervals)-2)
        ticks_ToShow = ["120"]
        ticks_ToShow.extend(empty_ticks)
        ticks_ToShow.extend(["60"])
        self.SetTicks(ticks_ToShow) #["F","","","","E"]

        # Colors
        self.SetTicksColour(wx.WHITE)
        self.SetSpeedBackground(wx.BLACK)

        # Setting 20% at end to be red coloured
        length_colours = len(intervals) - 1
        red_colours = length_colours - 3
        black_colours = length_colours - red_colours
        red_colours_list = [wx.RED] * (red_colours)
        black_colours_list = [wx.BLACK] * (black_colours)
        interval_colours = red_colours_list
        interval_colours.extend(black_colours_list)

        self.SetIntervalColours(interval_colours)
        self.SetHandColour(wx.Colour(255,50,0))
        self.SetMiddleTextColour(wx.WHITE)

        # Divide in 5 pieces
        self.SetNumberOfSecondaryTicks(2)

        # Fonts
        self.SetTicksFont(
               wx.Font(15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        self.SetMiddleTextFont(
               wx.Font(15, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        # Remove arc (visible on non-black bg)
        self.DrawExternalArc(False)

        # Set start value
        self.SetSpeedValue(int(60))

    def Set(self, value):
        if value >= 120:
           value1 = 120
        if value <= 60:
           value1 = 60
        else: 
           value1=value
        self.SetSpeedValue(120-int(value1))
        self.SetMiddleText(str(value)+"C°")
        self.Refresh()

