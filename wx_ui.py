import wx
import wx.adv
import ytapi


class Frame(wx.Frame):

    """Frame for the UI"""

    def __init__(self):
        """Initialize the frame """
        wx.Frame.__init__(self, None, pos=wx.DefaultPosition,
                          size=wx.Size(475, 100), style=wx.MINIMIZE_BOX |
                          wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX |
                          wx.CLIP_CHILDREN, title='AceTube')

        panel = wx.Panel(self)
        label = wx.StaticText(panel, label='\t\t\t\t\tAce YouTube Search')

        my_sizer = wx.BoxSizer(wx.VERTICAL)
        my_sizer.Add(label, 0, wx.ALL, 5)

        self.text = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,
                                size=(400, 30))
        self.text.SetFocus()
        self.text.Bind(wx.EVT_TEXT_ENTER, self.onButton)

        my_sizer.Add(self.text, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)

        # Icons not yet present
        search = wx.Bitmap("./icons/search.png", wx.BITMAP_TYPE_ANY)
        button = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=search,
                                 pos=(417, 28), size=(30, 30))
        button.Bind(wx.EVT_BUTTON, self.onButton)
        self.Show()

    def onButton(self, event):
        """
        Send the query to search
        """
        ytapi.redirect()  # Somewhere

    def onEnter(self, event):
        """
        Send the query to search
        """
        ytapi.redirect()  # Somewhere


class Results(wx.Frame):

    """Displaying the results"""

    def __init__(self, results):
        """Frame for results"""
        wx.Frame.__init__(self, None, pos=wx.DefaultPosition,
                          size=wx.Size(475, 100),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                          wx.CLOSE_BOX | wx.CLIP_CHILDREN, title='Results')


if __name__ == '__main__':
    app = wx.App(True)
    frame = Frame()
    app.MainLoop()
