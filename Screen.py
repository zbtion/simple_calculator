# the screen would show the word and the word would align right
import wx

class Screen(wx.StaticText):
    def __init__(self, parent, id, label, pos, size):
        wx.StaticText.__init__(self, parent, id, label, pos, size, style=wx.ALIGN_RIGHT)
        self.label = label
        self.SetBackgroundColour("white")
        self.SetForegroundColour("black")


