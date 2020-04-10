import wx


#####################################################################
# onToolbarClick
#####################################################################
def onToolbarClick(self, event):
    id = event.getId()
    pass


#####################################################################
# wx.Frame MainFrame
#####################################################################
class MainFrame(wx.Frame):
    file_filters = "AVI (*.avi)|*.avi|All files (*.*)|*.*"

    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((576, 432))

        # <ToolBar>
        self.toolbar = wx.ToolBar(self, -1, style=wx.TB_DEFAULT_STYLE | wx.TB_TEXT)
        self.SetToolBar(self.toolbar)
        self.toolbar.AddTool(wx.ID_OPEN, r"Открыть видео",
                             wx.Bitmap("icons\\open.png", wx.BITMAP_TYPE_ANY),
                             wx.Bitmap("icons\\open.disabled.png", wx.BITMAP_TYPE_ANY),
                             wx.ITEM_NORMAL, r"Открыть видео", "")
        self.toolbar.AddTool(wx.ID_SAVE, r"Сохранить видео",
                             wx.Bitmap("icons\\save.png", wx.BITMAP_TYPE_ANY),
                             wx.Bitmap("icons\\save.disabled.png", wx.BITMAP_TYPE_ANY),
                             wx.ITEM_NORMAL, r"Сохранить видео", "")
        self.toolbar.AddSeparator()
        self.toolbar.AddTool(wx.ID_UNDO, r"Отменить",
                             wx.Bitmap("icons\\undo.png", wx.BITMAP_TYPE_ANY),
                             wx.Bitmap("icons\\undo.disabled.png", wx.BITMAP_TYPE_ANY),
                             wx.ITEM_NORMAL, r"Отменить", "")
        self.toolbar.AddTool(wx.ID_REDO, r"Повторить",
                             wx.Bitmap("icons\\repeat.png", wx.BITMAP_TYPE_ANY),
                             wx.Bitmap("icons\\repeat.disabled.png", wx.BITMAP_TYPE_ANY),
                             wx.ITEM_NORMAL, r"Повторить", "")
        self.toolbar.AddSeparator()
        self.toolbar.AddTool(wx.ID_ADD, r"Новый эффект",
                             wx.Bitmap("icons\\effect.png", wx.BITMAP_TYPE_ANY),
                             wx.Bitmap("icons\\effect.disabled.png", wx.BITMAP_TYPE_ANY),
                             wx.ITEM_NORMAL, r"Новый эффект", "")
        self.toolbar.EnableTool(wx.ID_SAVE, False)
        self.toolbar.EnableTool(wx.ID_UNDO, False)
        self.toolbar.EnableTool(wx.ID_REDO, False)
        self.toolbar.EnableTool(wx.ID_ADD, False)
        # </ToolBar>

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TOOL, self.click_open, id=wx.ID_OPEN)
        self.Bind(wx.EVT_TOOL, self.click_save, id=wx.ID_SAVE)
        self.Bind(wx.EVT_TOOL, self.click_undo, id=wx.ID_UNDO)
        self.Bind(wx.EVT_TOOL, self.click_redo, id=wx.ID_REDO)
        self.Bind(wx.EVT_TOOL, self.click_addeffect, id=wx.ID_ADD)

    def __set_properties(self):
        self.SetTitle(r"PyVideo")
        self.toolbar.Realize()

    def __do_layout(self):
        self.Layout()

    def click_open(self, event):
        dialog = wx.FileDialog(self, message="Select video file...", defaultDir="",
                               wildcard=self.file_filters, style=wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            pass # self.load_file(dialog.GetPath())

    def click_save(self, event):
        dialog = wx.FileDialog(self, message="Save as...", defaultDir="",
                               wildcard=self.file_filters, style=wx.FD_SAVE)
        if dialog.ShowModal() == wx.ID_OK:
            pass

    def click_undo(self, event):
        print("Event handler 'click_undo' not implemented!")
        event.Skip()

    def click_redo(self, event):
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
