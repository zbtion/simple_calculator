# it's main body of the calculator
# it's implemented using wxPython

import wx
from Button import Button
from Screen import Screen
from Controller import Controller

class Calculator(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300, 400))
        
        base_panel = wx.Panel(self)
        base_sizer = wx.BoxSizer(wx.VERTICAL)
        base_panel.SetSizer(base_sizer)

        screen = Screen(base_panel, -1, "", pos=(0, 0), size=(280, 50))
        base_sizer.Add(screen, 0, wx.EXPAND)
        controller = Controller(screen)
        self.set_buttons(base_panel, controller)

    def set_buttons(self, base_panel, controller):
        button_panel = wx.Panel(base_panel)
        sizer = wx.GridSizer(4, 4, 5, 5)
        sizer.AddMany([ (Button(button_panel, 1, '1', controller), 0, wx.EXPAND),
                               (Button(button_panel, 2, '2', controller), 0, wx.EXPAND),
                               (Button(button_panel, 3, '3', controller), 0, wx.EXPAND),
                               (Button(button_panel, -1, '+', controller), 0, wx.EXPAND),
                               (Button(button_panel, 4, '4', controller), 0, wx.EXPAND),
                               (Button(button_panel, 5, '5', controller), 0, wx.EXPAND),
                               (Button(button_panel, 6, '6', controller), 0, wx.EXPAND),
                               (Button(button_panel, -1, '-', controller), 0, wx.EXPAND),
                               (Button(button_panel, 7, '7', controller), 0, wx.EXPAND),
                               (Button(button_panel, 8, '8', controller), 0, wx.EXPAND),
                               (Button(button_panel, 9, '9', controller), 0, wx.EXPAND),
                               (Button(button_panel, -1, '*', controller), 0, wx.EXPAND),
                               (Button(button_panel, -1, 'C', controller), 0, wx.EXPAND),
                               (Button(button_panel, 0, '0', controller), 0, wx.EXPAND),
                               (Button(button_panel, -1, '=', controller), 0, wx.EXPAND),
                               (Button(button_panel, -1, '/', controller), 0, wx.EXPAND)
                               ])
        button_panel.SetSizer(sizer)
        base_panel.GetSizer().Add(button_panel, 0, wx.EXPAND)
        
    
