import wx
from frame_main import MainFrame


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
