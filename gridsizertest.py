import wx 
import datetime

dtime = datetime.datetime.now()
timenow = str(dtime.day)+"/"+str(dtime.month)+"/"+str(dtime.year)+"  "+str(dtime.hour)+":"+str(dtime.minute)
 
class Example(wx.Frame): 
   
   def __init__(self, parent, title): 
      super(Example, self).__init__(parent, title = title, size = (200,300)) 
             
      self.InitUI() 
      self.Centre() 
      self.Show()
		
   def InitUI(self): 
      p = wx.Panel(self) 
      vbox = wx.BoxSizer(wx.VERTICAL) 
      l1 = wx.StaticText(p,label = timenow ,style = wx.ALIGN_RIGHT ) 
      vbox.Add(l1,0,wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,0) 
      p2 = wx.Panel(self)
      hbox = wx.BoxSizer(wx.HORIZONTAL) 
      l2 = wx.StaticText(p,label = "Label2", style = wx.ALIGN_CENTRE) 
		
      hbox.Add(p2,0,wx.EXPAND) 
      b3 = wx.Button(p,label = "Btn3") 
      hbox.AddStretchSpacer(1) 
      hbox.Add(b3,0,wx.ALIGN_LEFT,20) 
      vbox.Add(hbox,1,wx.ALL|wx.EXPAND) 
      p.SetSizer(vbox) 
          
app = wx.App() 
Example(None, title = 'BoxSizer demo') 
app.MainLoop()