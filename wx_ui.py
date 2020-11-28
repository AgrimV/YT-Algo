import wx
import wx.adv


class Frame(wx.Frame):

    """Frame for the UI"""

    def __init__(self):
        """Initialize the frame """
        wx.Frame.__init__(self, None, pos=wx.DefaultPosition,
                          size=wx.Size(475, 100), style=wx.MINIMIZE_BOX |
                          wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX |
                          wx.CLIP_CHILDREN, title='AceTube')


if __name__ == '__main__':
    app = wx.App(True)
    frame = Frame()
    app.MainLoop()
