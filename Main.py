from Calculator import Calculator
import wx

if __name__ == '__main__':
    app = wx.App()
    frame = Calculator(parent=None, id=-1, title="Calculator")
    frame.Show()
    app.MainLoop()