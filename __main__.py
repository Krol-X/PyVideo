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

        # <toolbar>
        self.toolbar = wx.ToolBar(self, -1, style=wx.TB_DEFAULT_STYLE | wx.TB_TEXT | wx.TB_HORZ_TEXT)
        self.SetToolBar(self.toolbar)
        self.toolbar.AddTool(wx.ID_OPEN, r"Открыть",
                             wx.Bitmap("icons\\open.png", wx.BITMAP_TYPE_ANY),
                             wx.Bitmap("icons\\open.disabled.png", wx.BITMAP_TYPE_ANY),
                             wx.ITEM_NORMAL, r"Открыть видео...", "")
        self.toolbar.AddTool(wx.ID_SAVEAS, r"Сохранить как",
                             wx.Bitmap("icons\\save.png", wx.BITMAP_TYPE_ANY),
                             wx.Bitmap("icons\\save.disabled.png", wx.BITMAP_TYPE_ANY),
                             wx.ITEM_NORMAL, r"Сохранить видео как...", "")
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
        # </toolbar>

        self.video_frame = wx.Panel(self, wx.ID_ANY)

        # <panel>
        self.panel = wx.Panel(self, wx.ID_ANY, style=wx.BORDER_STATIC)
        self.play_button = wx.BitmapButton(self.panel, wx.ID_ANY,
                                           wx.Bitmap("icons\\play.png", wx.BITMAP_TYPE_ANY))
        self.play_button.SetBitmapDisabled(wx.Bitmap("icons\\play.disabled.png", wx.BITMAP_TYPE_ANY))
        self.slider_1 = wx.Slider(self.panel, wx.ID_ANY, 0, 0, 10)
        # </panel>

        self.__set_properties()
        self.__do_layout()

        # Set events
        self.Bind(wx.EVT_TOOL, onToolbarClick, id=wx.ID_ANY)

    def __set_properties(self):
        self.SetTitle(r"PyVideo")
        self.toolbar.EnableTool(wx.ID_SAVEAS, False)
        self.toolbar.EnableTool(wx.ID_UNDO, False)
        self.toolbar.EnableTool(wx.ID_REDO, False)
        self.toolbar.EnableTool(wx.ID_ADD, False)
        self.toolbar.Realize()
        self.play_button.SetSize(self.play_button.GetBestSize())
        self.panel.SetMinSize((24, 24))

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL), 0, 0, 0)
        sizer_1.Add(self.video_frame, 1, wx.EXPAND, 0)
        sizer_2.Add(self.play_button, 0, 0, 0)
        sizer_2.Add(self.slider_1, 1, wx.EXPAND, 0)
        self.panel.SetSizer(sizer_2)
        sizer_1.Add(self.panel, 0, wx.EXPAND | wx.FIXED_MINSIZE, 0)
        self.SetSizer(sizer_1)
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
