import wx


#####################################################################
# onToolbarClick
#####################################################################
def onToolbarClick(event):
    file_filters = "AVI (*.avi)|*.avi|All files (*.*)|*.*"

    if event.Id == wx.ID_OPEN:
        dialog = wx.FileDialog(None, message="Select video file...", defaultDir="",
                               wildcard=file_filters, style=wx.FD_OPEN)
        if dialog.ShowModal() == wx.ID_OK:
            pass  # self.load_file(dialog.GetPath())
    if event.Id == wx.ID_SAVEAS:
        dialog = wx.FileDialog(None, message="Save as...", defaultDir="",
                               wildcard=file_filters, style=wx.FD_SAVE)
        if dialog.ShowModal() == wx.ID_OK:
            pass
    if event.Id == wx.ID_UNDO:
        pass
    if event.Id == wx.ID_REDO:
        pass
    if event.Id == wx.ID_ADD:
        pass


#####################################################################
# wx.Frame MainFrame
#####################################################################
class MainFrame(wx.Frame):
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
        self.toolbar.AddTool(wx.ID_SAVEAS, r"Сохранить видео",
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
        self.toolbar.EnableTool(wx.ID_SAVEAS, False)
        self.toolbar.EnableTool(wx.ID_UNDO, False)
        self.toolbar.EnableTool(wx.ID_REDO, False)
        self.toolbar.EnableTool(wx.ID_ADD, False)
        # </ToolBar>

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_TOOL, onToolbarClick, id=wx.ID_ANY)

    def __set_properties(self):
        self.SetTitle(r"PyVideo")
        self.toolbar.Realize()

    def __do_layout(self):
        self.Layout()


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
