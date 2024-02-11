import wx

class Button(wx.Button):
    def __init__(self, parent, id, label, pos, size):
        wx.Button.__init__(self, parent, id, label, pos, size)
        self.label = label
        self.Bind(wx.EVT_BUTTON, self.OnClick)

    def OnClick(self, event):
        # self.parent.sent_message(self.label)
        pass
