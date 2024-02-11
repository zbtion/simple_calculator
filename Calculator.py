# it's main body of the calculator
# it's implemented using wxPython

import wx
from Button import Button
from Screen import Screen

class Calculator(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300, 400))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        screen_panel = wx.Panel(panel)
        button_panel = wx.Panel(panel)
        sizer.Add(screen_panel, 0, wx.EXPAND)
        sizer.Add(button_panel, 1, wx.EXPAND)

        self.text = Screen(screen_panel, -1, "", pos=(0, 0), size=(280, 50))
        self.Add_button(button_panel)
        
        panel.SetSizer(sizer)
    
    def Add_button(self, button_panel):
        button_sizer = wx.GridSizer(4, 3, 5, 5)
        button_sizer.AddMany([ (Button(button_panel, 1, '1', pos=(0, 0), size=(50, 50)), 0, wx.EXPAND),
                                 (Button(button_panel, 2, '2', pos=(0, 0), size=(50, 50)), 0, wx.EXPAND),
                                 (Button(button_panel, 3, '3', pos=(0, 0), size=(50, 50)), 0, wx.EXPAND),
                                 (Button(button_panel, 4, '4', pos=(0, 0), size=(50, 50)), 0, wx.EXPAND),
                                 (Button(button_panel, 5, '5', pos=(0, 0), size=(50, 50)), 0, wx.EXPAND),
                                 (Button(button_panel, 6, '6', pos=(0, 0), size=(50, 50)), 0, wx.EXPAND),
                                 (Button(button_panel, 7, '7', pos=(0, 0), size=(50, 50)), 0, wx.EXPAND),
                                 (Button(button_panel, 8, '8', pos=(0, 0), size=(50, 50)), 0, wx.EXPAND),
                                 (Button(button_panel, 9, '9', pos=(0, 0), size=(50, 50)), 0, wx.EXPAND),
                                 (Button(button_panel, 0, '0', pos=(0, 0), size=(50, 50)), 0, wx.EXPAND),
                                 (Button(button_panel, -1, 'C', pos=(0, 0), size=(50, 50)), 0, wx.EXPAND),
                                 (Button(button_panel, -1, '=', pos=(0, 0), size=(50, 50)), 0, wx.EXPAND)])
        button_panel.SetSizer(button_sizer)
