import wx


class AdderTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        label = wx.StaticText(self, -1, "You didn't add any social network. Add it now?")
        add_button = wx.Button(self, -1, "Add")
        content_sizer = wx.BoxSizer(wx.VERTICAL)
        content_sizer.AddStretchSpacer()
        # 20 and 10 is border with
        content_sizer.Add(label, 0, wx.ALIGN_CENTER | wx.BOTTOM | wx.LEFT | wx.RIGHT, 20)
        content_sizer.Add(add_button, 0, wx.ALIGN_CENTER | wx.BOTTOM, 10)
        content_sizer.AddStretchSpacer()
        # 0 is add_button index in next method, because it added to sizer first
        content_sizer.SetItemMinSize(0, add_button.GetDefaultSize())
        # auto resize to elements
        content_sizer.SetSizeHints(self)
        self.SetSizer(content_sizer)


class SocialNetworkTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)