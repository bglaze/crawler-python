#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  A Monster Character Sheet wx.Panel for Crawler I
#  by Brock Glaze
#
#  crPanel_MonsterSheet.py


import crawler
import wx


class monPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.frame = parent.frame


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
