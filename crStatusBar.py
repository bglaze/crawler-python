#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  A Custom Statusbar for Crawler I
#  by Brock Glaze
#
#  crStatusBar.py

import time
import wx


class CustomStatusBar(wx.StatusBar):
    def __init__(self, parent):
        wx.StatusBar.__init__(self, parent, wx.ID_ANY)

        self.SetFieldsCount(3)
        self.SetStatusWidths([-2, 79, 79])

        # Set text for field 0
        self.SetStatusText("Ready", 0)

        self.timer = wx.PyTimer(self.Notify)
        self.timer.Start(1000)
        self.Notify()


    # Handles events from self.timer
    def Notify(self):
        t = time.localtime(time.time())
        cdate = time.strftime("%d %b %Y", t)
        ctime = time.strftime("%I:%M %p", t)
        self.SetStatusText(cdate, 1)
        self.SetStatusText(ctime, 2)


#***********************************************************************


if __name__ == '__main__':
    pass
