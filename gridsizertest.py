# put two different size panels into a wxBoxSizer
import wx
class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(250, 70))
        panel = wx.Panel(self, -1)
        panel1 = wx.Panel(panel, -1, size=(50, 30))
        panel1.SetBackgroundColour('blue')
        panel2 = wx.Panel(panel, -1, size=(200, 30))
        panel2.SetBackgroundColour('green')
        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(panel1, 1)
        box.Add(panel2, 1)
        panel.SetSizer(box)
        self.Centre()
class MyApp(wx.App):
     def OnInit(self):
         frame = MyFrame(None, -1, 'wxBoxSizer.py')
         frame.Show(True)
         return True
app = MyApp(0)
app.MainLoop()