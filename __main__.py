import wx


#####################################################################
# wx.Frame MainFrame
#####################################################################
class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((492, 320))

        # <ToolBar>
        self.frame_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.frame_toolbar)
        self.frame_toolbar.AddTool(1000, r"Открыть видео",
                                    wx.Bitmap("icons\\open.png", wx.BITMAP_TYPE_ANY),
                                    wx.Bitmap("icons\\open.disabled.png", wx.BITMAP_TYPE_ANY),
                                    wx.ITEM_NORMAL, r"Открыть видео", "")
        self.frame_toolbar.AddTool(1001, r"Сохранить видео",
                                   wx.Bitmap("icons\\save.png", wx.BITMAP_TYPE_ANY),
                                   wx.Bitmap("icons\\save.disabled.png", wx.BITMAP_TYPE_ANY),
                                   wx.ITEM_NORMAL, r"Сохранить видео", "")
        self.frame_toolbar.AddSeparator()
        self.frame_toolbar.AddTool(1010, r"Отменить",
                                   wx.Bitmap("icons\\undo.png", wx.BITMAP_TYPE_ANY),
                                   wx.Bitmap("icons\\undo.disabled.png", wx.BITMAP_TYPE_ANY),
                                   wx.ITEM_NORMAL, r"Отменить", "")
        self.frame_toolbar.AddTool(1011, r"Повторить",
                                   wx.Bitmap("icons\\repeat.png", wx.BITMAP_TYPE_ANY),
                                   wx.Bitmap("icons\\repeat.disabled.png", wx.BITMAP_TYPE_ANY),
                                   wx.ITEM_NORMAL, r"Повторить", "")
        self.frame_toolbar.AddSeparator()
        self.frame_toolbar.AddTool(1020, r"Новый эффект",
                                   wx.Bitmap("icons\\effect.png", wx.BITMAP_TYPE_ANY),
                                   wx.Bitmap("icons\\effect.disabled.png", wx.BITMAP_TYPE_ANY),
                                   wx.ITEM_NORMAL, r"Новый эффект", "")
        # </ToolBar>

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TOOL, self.click_open, id=1000)
        self.Bind(wx.EVT_TOOL, self.click_save, id=1001)
        self.Bind(wx.EVT_TOOL, self.click_undo, id=1010)
        self.Bind(wx.EVT_TOOL, self.click_repeat, id=1011)
        self.Bind(wx.EVT_TOOL, self.click_addeffect, id=1020)

    def __set_properties(self):
        self.SetTitle(r"PyVideo")
        self.frame_toolbar.Realize()

    def __do_layout(self):
        self.Layout()

    def click_open(self, event):
        print("Event handler 'click_open' not implemented!")
        event.Skip()

    def click_save(self, event):
        print("Event handler 'click_save' not implemented!")
        event.Skip()

    def click_undo(self, event):
        print("Event handler 'click_undo' not implemented!")
        event.Skip()

    def click_repeat(self, event):
        print("Event handler 'click_repeat' not implemented!")
        event.Skip()

    def click_addeffect(self, event):
        print("Event handler 'click_addeffect' not implemented!")
        event.Skip()


#####################################################################
# wx.App MainApp
#####################################################################
class MainApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


#####################################################################
# main
#####################################################################
if __name__ == "__main__":
    app = MainApp(0)
    app.MainLoop()
