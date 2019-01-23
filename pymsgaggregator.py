import wx


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title)
        self.init_user_interface()

    def init_user_interface(self):
        menu_bar = wx.MenuBar()

        file_menu = wx.Menu()
        exit_item = wx.MenuItem(file_menu, wx.ID_EXIT, '&Exit\tCtrl+Q')
        file_menu.Append(exit_item)
        menu_bar.Append(file_menu, '&File')

        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.menu_handler)
        self.SetSize((800, 600))
        self.Centre()
        self.Show(True)

    def menu_handler(self, event):
        id = event.GetId()
        if id == wx.ID_EXIT:
            self.Close()


app = wx.App()
MainWindow(None, 'PyMsgAggregator')
app.MainLoop()
