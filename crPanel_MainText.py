#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Text Panel module for Crawler I
#  by Brock Glaze
#
#  crTextPanel.py


import crawler
import wx


textPanel_height = 145


#-----------------------------------------------------------------------
#------ Custom TextCtrls -----------------------------------------------
#-----------------------------------------------------------------------


class MainText(wx.TextCtrl):
    def __init__(self, parent, *args, **kwargs):
        wx.TextCtrl.__init__(self, parent, wx.ID_ANY,
        style=wx.SIMPLE_BORDER
        |wx.TE_READONLY
        |wx.TE_DONTWRAP
        |wx.TE_MULTILINE,
        *args, **kwargs)

        self.max_lines = 1500

        self.Bind(wx.EVT_CONTEXT_MENU, self.OnContextMenu)
        self.ID_CLEAR = wx.NewId()
        self.Bind(wx.EVT_MENU, self.ClearText, id=self.ID_CLEAR)


    def ClearText(self, event=None):
        if self.GetValue():
            self.Clear()


    # When called, will remove top lines
    # until num_lines_allowed is reached
    def DeleteLines(self, event=None):
        while self.GetNumberOfLines() > self.max_lines:
            self.Remove(0, self.GetLineLength(0)+1)


    # Appends Text to TextCtrl, calls DeleteLines,
    # and sets Insertion Point to the beginning of the bottom line
    def DoAppendText(self, text, event=None):

        # Only handle one line at a time if the TextCtrl is full
        if self.GetNumberOfLines() >= self.max_lines:

            lines = text.splitlines(True)

            freeze = False
            if len(lines) <= 2:
                # Single lines need frozen to reduce flickers.
                freeze = True

            if freeze: self.Freeze()

            # Process one line at a time,
            # even if text is a multi-line string
            for line in lines:
                self.AppendText(line)
                self.DeleteLines()

            if freeze: self.Thaw()

        else:
            self.AppendText(text)
            self.DeleteLines()

        self.SetInsertionPointEnd()
        self.SetInsertionPoint(self.XYToPosition(0, -1))


    # Popup Menu
    def OnContextMenu(self, event):
        menu = wx.Menu()
        menu.Append(self.ID_CLEAR, "Clear All")
        self.PopupMenu(menu)
        menu.Destroy()


class InputText(wx.TextCtrl):
    def __init__(self, parent, txt_affect, *args, **kwargs):
        wx.TextCtrl.__init__(self, parent, wx.ID_ANY,
        style=wx.SIMPLE_BORDER
        |wx.TE_PROCESS_ENTER,
        *args, **kwargs)

        # Main Multi-line TextCtrl
        self.txt_affect = txt_affect

        self.Bind(wx.EVT_CHAR, self.OnChar)


    def OnChar(self, event):
        if event.GetKeyCode() == wx.WXK_RETURN:

            new_line = "\n"
            if self.txt_affect.GetValue() == "":
                new_line = ""

            text = "%s%s" % (new_line, self.GetValue())
            self.txt_affect.DoAppendText(text)
            self.Clear()

        event.Skip()


#-----------------------------------------------------------------------
#------ Text Panel -----------------------------------------------------
#-----------------------------------------------------------------------


class textPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent,
        size=(-1, textPanel_height), *args, **kwargs)

        # parent = Main Frame
        self.parent = parent


        # Main Multi-Line TextCtrl
        fg_color_txt_main = (0, 120, 0)
        self.txt_main = MainText(self)
        self.txt_main.SetForegroundColour(fg_color_txt_main)
        self.txt_main.SetFont(self.MyFixedFontB1(10))


        # Input TextCtrl
        #~ self.txt_input = InputText(self, self.txt_main)


        # Main Sizer for textPanel
        szr_text = wx.BoxSizer(wx.VERTICAL)
        szr_text.Add(self.txt_main, 1, flag=wx.EXPAND)
        self.SetSizer(szr_text)


    def MyFixedFontB1(self, pointSize):
        return wx.Font(
               pointSize, wx.FONTFAMILY_MODERN,
               style=wx.NORMAL, weight=wx.BOLD
               )


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
