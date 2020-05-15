import wx

class Effects(wx.Dialog):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION
        wx.Dialog.__init__(self, *args, **kwds)
        self.list_box_1 = wx.ListBox(self, wx.ID_ANY, choices=[r"Blur", r"GaussianBlur", r"medianBlur", r"bilateralFilter"])
        self.spin_1 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_2 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_3 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.button_ok = wx.Button(self, wx.ID_ANY, r"Применить")
        self.button_back = wx.Button(self, wx.ID_ANY, r"Назад")

        self.__set_properties()
        self.__do_layout()


    def __set_properties(self):
        self.SetTitle(r"Добавить эффект")
        self.list_box_1.SetSelection(0)

    def __do_layout(self):
        sizer_0 = wx.BoxSizer(wx.VERTICAL)
        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(self.list_box_1, 1, 0, 0)
        sizer_0.Add(sizer_1, 0, wx.EXPAND, 0)
        label_1 = wx.StaticText(self, wx.ID_ANY, r"Параметр 1")
        label_1.SetMinSize((80, 16))
        sizer_2.Add(label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.spin_1, 0, 0, 0)
        sizer_0.Add(sizer_2, 0, wx.EXPAND, 0)
        label_2 = wx.StaticText(self, wx.ID_ANY, r"Параметр 2")
        label_2.SetMinSize((80, 16))
        sizer_3.Add(label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.spin_2, 0, 0, 0)
        sizer_0.Add(sizer_3, 0, wx.EXPAND, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, r"Параметр 3")
        label_3.SetMinSize((80, 16))
        sizer_4.Add(label_3, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(self.spin_3, 0, 0, 0)
        sizer_0.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_5.Add(self.button_ok, 1, 0, 0)
        sizer_5.Add(self.button_back, 1, 0, 0)
        sizer_0.Add(sizer_5, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_0)
        sizer_0.Fit(self)
        self.Layout()

