#!/usr/bin/env python

from time import sleep
from threading import Thread
from math import ceil
import wx
import obd

import meter_Speed
import meter_RPM
import meter_Fuel
import meter_Temp


#DisplaySize = wx.GetDisplaySize()


''' Commented for testing'''
# Init
obd_connection = obd.Async("\.\COM4")
# Callback is called when data is received
obd_connection.watch(obd.commands.RPM)
obd_connection.watch(obd.commands.SPEED)
obd_connection.watch(obd.commands.GET_DTC)
obd_connection.watch(obd.commands.DISTANCE_W_MIL)
obd_connection.watch(obd.commands.COOLANT_TEMP)

#obd_connection.watch(obd.commands[1][166])
''''''
class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=wx.GetDisplaySize())
        MainPanel = wx.Panel(self, size=self.GetSize())
        MainPanel.SetBackgroundColour(wx.Colour(0,0,255))
        
        panel_KPH = wx.Panel(self, size=(500,500), pos=(0,0))
        panel_RPM = wx.Panel(self, size=(500,500), pos=(500,0))
        panel_Fuel = wx.Panel(self, size=(250,250), pos=(1000,0))
        panel_Temp = wx.Panel(self, size=(250,250), pos=(1000,250))

        #bind on esc key
        self.Bind(wx.EVT_CHAR_HOOK, self.onKey)
        
        # Eyes burning <remove later>
        panel_KPH.SetBackgroundColour(wx.Colour(255,33,33))
        panel_RPM.SetBackgroundColour(wx.Colour(33,255,33))


        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(panel_KPH,0)
        box.Add(panel_RPM,1)
        MainPanel.SetSizer(box)
        #GridSizer
        #gs = wx.GridSizer(2,1,5,5)
        #gs.Add(self.speedmeter = speedmeter.SpeedMeter(panel))
        #gs.Add(self.speedmeter1 = speedmeter.SpeedMeter(panel1))
        
        '''
        # Start
        self.btn_start_stop = wx.Button(MainPanel, label="Start")
        self.btn_start_stop.Bind(wx.EVT_BUTTON, self.OnStartStop)
        '''
        
        # Add speedmeter
        self.Speed = meter_Speed.SpeedMeter(panel_KPH,panel_KPH.GetSize())
        self.RPM = meter_RPM.SpeedMeter(panel_RPM,panel_RPM.GetSize())
        self.Fuel = meter_Fuel.SpeedMeter(panel_Fuel,panel_Fuel.GetSize())
        self.Temp = meter_Temp.SpeedMeter(panel_Temp,panel_Temp.GetSize())
		
        self.ShowFullScreen(True)

    # Start_Stop button
    def OnStartStop(self, event):
        obd_connection.start()
        print("Started")
        
    def onKey(self, event):
        """
        Check for ESC key press and exit is ESC is pressed
        """
        key_code = event.GetKeyCode()
        if key_code == wx.WXK_ESCAPE:
            self.Close(True)
        else:
            event.Skip()

    # Called on GUI exit (X btn)
    def OnExit(self, event):
        self.Close(True)

# DEBUG
def test():
    kph = 0
    rpm = 0
    temp = 0
    
    
    while True:
        frame.Speed.Set(kph)
        frame.RPM.Set(rpm)
        frame.Temp.Set(temp)
        
        
        
        sleep(0.2)
        '''  Commented for testing'''
        obd_connection.stop()
        value_RPM = obd_connection.query(obd.commands.RPM)
        value_KPH = obd_connection.query(obd.commands.SPEED)
        value_TEMP = obd_connection.query(obd.commands.COOLANT_TEMP)
        value_FUEL = obd_connection.query(obd.commands.DISTANCE_W_MIL)
        #supp = obd_connection.query(obd.commands[1][166])
        rpm = value_RPM  #ne sa testvani
        kph = value_KPH    #ne sa testvani
        print("value temp: "+str(value_TEMP))
        print("value fuel: "+str(value_FUEL))
       # print("value RPM: "+str(value_RPM.magnitude))
        print("rpm: "+str(rpm))
        #print(supp)
        ''''''
        # Testvano i raboti
        kph_str=str(value_KPH)
        if kph_str=="None":
            kph_str="0"
        kph=int(kph_str.split()[0])
        rpm_str=str(value_RPM)
        if rpm_str=="None":
            rpm_str="0"
        rpm=ceil(float(rpm_str.split()[0]))
        temp_str=str(value_TEMP)
        if temp_str=="None":
            temp_str="0"
        temp=int(temp_str.split()[0])
        print(temp)
        
        '''  Commented for testing'''
        print(obd_connection.query(obd.commands.GET_DTC))
        print(obd.commands.has_pid(1, 166))
        

        for i in range(0,95):
            print("PID " + str(i) + " --- " + str(obd_connection.query(obd.commands[1][i])))
        
        
        obd_connection.start()
        ''''''

# Entry point
if __name__ == "__main__":
    app = wx.App(False)
    frame = MainWindow(None, "Main Window")
    frame.Show()
    
    # DEBUG
    Thread(target=test).start()
    

    # Blocking
    app.MainLoop()


