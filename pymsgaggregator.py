import wx


class AdderTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        label = wx.StaticText(self, -1, "You didn't add any social network. Add it now?")
        add_button = wx.Button(self, -1, "Add")
        box_sizer = wx.BoxSizer(wx.VERTICAL)
        box_sizer.Add(label, 0, wx.ALL, 0)
        box_sizer.Add(add_button, 0, wx.ALL, 0)
        box_sizer.SetSizeHints(self)
        self.SetSizer(box_sizer)


class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        super(MainWindow, self).__init__(parent, title=title)
        self.init_user_interface()

    def init_user_interface(self):

        # Menu section
        menu_bar = wx.MenuBar()
        file_menu = wx.Menu()
        exit_item = wx.MenuItem(file_menu, wx.ID_EXIT, '&Exit\tCtrl+Q')
        file_menu.Append(exit_item)
        menu_bar.Append(file_menu, '&File')

        # Creating tab holder
        main_panel = wx.Panel(self)
        tab_holder = wx.Notebook(main_panel)

        adder_tab = AdderTab(tab_holder)

        tab_holder.AddPage(adder_tab, "Add SN")

        sizer = wx.BoxSizer()
        sizer.Add(tab_holder, 1, wx.EXPAND)
        main_panel.SetSizer(sizer)

        # Main window features
        self.SetMenuBar(menu_bar)
        self.Bind(wx.EVT_MENU, self.menu_handler)
        self.Centre()
        self.Show(True)

    def menu_handler(self, event):
        id = event.GetId()
        if id == wx.ID_EXIT:
            self.Close()


app = wx.App()
MainWindow(None, 'PyMsgAggregator')
app.MainLoop()
