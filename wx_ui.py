import wx
import wx.adv

import yt_api


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

        search = wx.Bitmap("icons\search_reduced.bmp", wx.BITMAP_TYPE_ANY)
        button = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=search,
                                 pos=(417, 28), size=(30, 30))
        button.Bind(wx.EVT_BUTTON, self.onButton)
        self.Show()

    def onButton(self, event):
        """
        Send the query to search
        """
        sub_app = wx.App(True)
        Results(yt_api.search(self.text.GetValue()))
        sub_app.MainLoop()


class Results(wx.Frame):

    """Displaying the results"""

    def __init__(self, results):
        """Frame for results"""
        wx.Frame.__init__(self, None, pos=wx.DefaultPosition,
                          size=wx.Size(475, 100),
                          style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
                          wx.CLOSE_BOX | wx.CLIP_CHILDREN, title='Results')

        self.results = results
        for index, result in enumerate(results):
            print('\n' + str(index + 1) + '.  ' +
                  result['snippet']['title'] + '\n')

        panel = wx.Panel(self)
        label = wx.StaticText(panel,
                              label='Enter the number of video to play it')

        my_sizer = wx.BoxSizer(wx.VERTICAL)
        my_sizer.Add(label, 0, wx.ALL, 5)

        self.text = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,
                                size=(400, 30))
        self.text.SetFocus()
        self.text.Bind(wx.EVT_TEXT_ENTER, self.onButton)

        my_sizer.Add(self.text, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)

        search = wx.Bitmap("icons\play_reduced.bmp", wx.BITMAP_TYPE_ANY)
        button = wx.BitmapButton(panel, id=wx.ID_ANY, bitmap=search,
                                 pos=(417, 28), size=(30, 30))

        button.Bind(wx.EVT_BUTTON, self.onButton)
        self.Show()

    def onButton(self, event):
        serial = self.text.GetValue()
        for index, result in enumerate(self.results):
            if int(serial) == index + 1:
                yt_api.redirect(result['id']['videoId'])


if __name__ == '__main__':
    app = wx.App(True)
    frame = Frame()
    app.MainLoop()
