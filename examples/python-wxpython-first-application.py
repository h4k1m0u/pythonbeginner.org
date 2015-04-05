#!/usr/bin/env python
import wx


# window frame class
class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)

        # add a button to the frame
        panel = wx.Panel(self)
        button = wx.Button(panel, label="Show the MessageBox")
        button.Bind(wx.EVT_BUTTON, self.OnClick)

        self.Show()

    def OnClick(self, event):
        # show a message box on button click
        wx.MessageBox("The button has been clicked", "Title")


# application main loop
app = wx.App()
MyFrame(None)
app.MainLoop()
