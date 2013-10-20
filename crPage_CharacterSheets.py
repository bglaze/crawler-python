#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  A Notebook-Page module for Crawler I
#  by Brock Glaze
#
#  crPage_CharacterSheets.py


import crawler
import crPanel_CharacterSheets
import wx
import wx.lib.scrolledpanel as scrolled


#-----------------------------------------------------------------------
#------ Advanture Calculator Page --------------------------------------
#-----------------------------------------------------------------------


class characterSheetsPage(scrolled.ScrolledPanel):
    def __init__(self, parent, frame, txt_affect, *args, **kwargs):
        scrolled.ScrolledPanel.__init__(self, parent, *args, **kwargs)

        self.frame = frame

        # Main Multi-line TextCtrl
        self.txt_affect = txt_affect

        panel_cs = (
        crPanel_CharacterSheets.characterSheetsPanel(self, self.txt_affect)
        )

        # Top Horizontal Sizer 1
        h_sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        h_sizer1.Add(panel_cs, 1, wx.EXPAND)


        # Main Sizer
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(h_sizer1, 1, wx.EXPAND)

        self.SetSizer(main_sizer)
        self.SetAutoLayout(True)
        self.SetupScrolling()


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
