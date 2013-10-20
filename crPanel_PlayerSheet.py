#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  A Player Character Sheet wx.Panel for Crawler I
#  by Brock Glaze
#
#  crPanel_PlayerSheet.py


import crawler
import sys
import wx


class plrPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.frame = parent.frame


#------ Character Name Label -------------------------------------------


        lbl_char_name = wx.StaticText(self, label="Character Name")
        lbl_char_name.SetFont(self.MyFontB1(15))

        szr_char_name = wx.BoxSizer(wx.HORIZONTAL)
        szr_char_name.Add(lbl_char_name, flag=wx.LEFT, border=10)


#------- Collapsable Pane Objects --------------------------------------


        self.cp_attributes = wx.CollapsiblePane(self,
                  label="Character Attributes",
                  style=wx.CP_DEFAULT_STYLE|wx.CP_NO_TLW_RESIZE
                  )
        self.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED,
                  self.OnPaneChanged, self.cp_attributes
                  )
        self.MakeAttributePane(self.cp_attributes.GetPane())


#------ Main Sizer -----------------------------------------------------

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(szr_char_name, flag=wx.TOP, border=5)
        main_sizer.Add(self.cp_attributes, 0,
                   flag=wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND,
                   border=10
                   )

        self.SetSizer(main_sizer)


#-----------------------------------------------------------------------
#------ Collapsable Panes ----------------------------------------------
#-----------------------------------------------------------------------


    def OnPaneChanged(self, evt=None):
        self.Layout()


    def MakeAttributePane(self, pane):

        # Player Name
        txt_player_name = wx.TextCtrl(pane)
        lbl_player_name = wx.StaticText(pane, label="Player Name")
        lbl_player_name.SetFont(self.MyFontB1(8))
        #--- Sizer ---
        szr_player_name_v = wx.BoxSizer(wx.VERTICAL)
        szr_player_name_v.Add(txt_player_name, 0, flag=wx.RIGHT|wx.EXPAND, border=5)
        szr_player_name_v.Add(lbl_player_name, flag=wx.LEFT|wx.TOP, border=2)


        # Row One Sizer
        szr_row_one_h = wx.BoxSizer(wx.HORIZONTAL)
        szr_row_one_h.Add(szr_player_name_v, 1, flag=wx.EXPAND)


        # Main Pane Sizer
        szr_pane = wx.BoxSizer(wx.VERTICAL)
        szr_pane.Add(szr_row_one_h, 1, flag=wx.ALL|wx.EXPAND, border=5)

        pane.SetSizer(szr_pane)


    def AddClassRow(self, ulc):
        # Create Row
        row = ulc.GetItemCount()

        index = ulc.InsertStringItem(sys.maxint, "", 0)

        pan_level = SpinLevelPanel(ulc, size=(56, 21))
        item = ulc.GetItem(row, 0)
        item.SetWindow(pan_level)
        ulc.SetItem(item)

        pan_class = ComboClassPanel(ulc, size=(123, 21))
        item = ulc.GetItem(row, 1)
        item.SetWindow(pan_class)
        ulc.SetItem(item)


#-----------------------------------------------------------------------
#------ Font Methods ---------------------------------------------------
#-----------------------------------------------------------------------


    def MyFontN1(self, pointSize):
        return wx.Font(
               pointSize, wx.FONTFAMILY_DEFAULT,
               style=wx.NORMAL, weight=wx.NORMAL
               )

    def MyFontB1(self, pointSize):
        return wx.Font(
               pointSize, wx.FONTFAMILY_DEFAULT,
               style=wx.NORMAL, weight=wx.BOLD
               )

    def MyFixedFontN1(self, pointSize):
        return wx.Font(
               pointSize, wx.FONTFAMILY_MODERN,
               style=wx.NORMAL, weight=wx.NORMAL
               )

    def MyFixedFontB1(self, pointSize):
        return wx.Font(
               pointSize, wx.FONTFAMILY_MODERN,
               style=wx.NORMAL, weight=wx.BOLD
               )


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
