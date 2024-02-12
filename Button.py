import wx

class Button(wx.Button):
    def __init__(self, parent, id, label, controller):
        wx.Button.__init__(self, parent, id, label, size=(100, 100))
        self.controller = controller
        self.Bind(wx.EVT_BUTTON, self.OnClick)

    def OnClick(self, event):
        self.controller.recv_message(self.GetLabel())
        pass
