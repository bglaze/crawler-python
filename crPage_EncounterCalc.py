#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  A Notebook-Page module for Crawler I
#  by Brock Glaze
#
#  crPage_AdventureCalc.py


import crawler
import crPanel_EncounterCalc
import wx
import wx.lib.scrolledpanel as scrolled


#-----------------------------------------------------------------------
#------ Advanture Calculator Page --------------------------------------
#-----------------------------------------------------------------------


class encounterCalcPage(scrolled.ScrolledPanel):
    def __init__(self, parent, frame, txt_affect, *args, **kwargs):
        scrolled.ScrolledPanel.__init__(self, parent, *args, **kwargs)

        self.frame = frame

        # Main Multi-line TextCtrl
        self.txt_affect = txt_affect


        experience_calculator = (
        crPanel_EncounterCalc.encCalcPanel(self, self.frame, self.txt_affect)
        )

        # Top Horizontal Sizer 1
        h_sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        h_sizer1.Add(experience_calculator)


        # Main Sizer
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(h_sizer1)

        self.SetSizer(main_sizer)
        self.SetAutoLayout(True)
        self.SetupScrolling()


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
