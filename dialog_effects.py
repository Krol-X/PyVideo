import wx

ID_OK = 20000
ID_BACK = 20001


#####################################################################
# wx.Dialog Effects
#####################################################################
class Effects(wx.Dialog):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION
        wx.Dialog.__init__(self, *args, **kwds)
        self.list_box_1 = wx.ListBox(self, wx.ID_ANY, choices=[r"--", r"Blur", r"GaussianBlur", r"medianBlur", r"bilateralFilter"])
        self.spin_1 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_2 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.spin_3 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=100)
        self.button_ok = wx.Button(self, ID_OK, r"Применить")
        self.button_back = wx.Button(self, ID_BACK, r"Назад")

        self.__set_properties()
        self.__do_layout()
        self.__update_ui()

        self.Bind(wx.EVT_LISTBOX, self.onListbox, id=wx.ID_ANY)
        self.Bind(wx.EVT_BUTTON, self.onButton, id=wx.ID_ANY)

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
        self.label_1 = wx.StaticText(self, wx.ID_ANY, r"Параметр 1")
        self.label_1.SetMinSize((80, 16))
        sizer_2.Add(self.label_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.spin_1, 0, 0, 0)
        sizer_0.Add(sizer_2, 0, wx.EXPAND, 0)
        self.label_2 = wx.StaticText(self, wx.ID_ANY, r"Параметр 2")
        self.label_2.SetMinSize((80, 16))
        sizer_3.Add(self.label_2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_3.Add(self.spin_2, 0, 0, 0)
        sizer_0.Add(sizer_3, 0, wx.EXPAND, 0)
        self.label_3 = wx.StaticText(self, wx.ID_ANY, r"Параметр 3")
        self.label_3.SetMinSize((80, 16))
        sizer_4.Add(self.label_3, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_4.Add(self.spin_3, 0, 0, 0)
        sizer_0.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_5.Add(self.button_ok, 1, 0, 0)
        sizer_5.Add(self.button_back, 1, 0, 0)
        sizer_0.Add(sizer_5, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_0)
        sizer_0.Fit(self)
        self.Layout()


    def __update_ui(self):
        sel = self.list_box_1.GetSelection()
        par1 = par2 = par3 = ""
        par1_en, par2_en, par3_en = False, False, False
        if sel == 1:
            par1, par2 = "Ширина ядра", "Высота ядра"
            par1_en, par2_en = True, True
        elif sel == 2:
            par1, par2 = "Ширина ядра", "Высота ядра"
            par1_en, par2_en, par3_en = True, True
        elif sel == 3:
            par1 = "Параметр"
            par1_en = True
        elif sel == 4:
            par1, par2, par3 = "Параметр1", "Параметр2", "Параметр3"
            par1_en, par2_en, par3_en = True, True, True
        self.label_1.SetLabel(par1)
        self.label_2.SetLabel(par2)
        self.label_3.SetLabel(par3)
        self.spin_1.Enable(par1_en)
        self.spin_2.Enable(par2_en)
        self.spin_3.Enable(par3_en)


    def onListbox(self, event):
        self.__update_ui()
        event.Skip()

    def onButton(self, event):
        if event.Id == ID_BACK or event.Id == ID_OK:
            self.Result = event.Id == ID_OK
            self.Close()
        event.Skip()
