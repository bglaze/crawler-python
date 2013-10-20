#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Character Sheets Panel module for Crawler I
#  by Brock Glaze
#
#  crPanel_CharacterSheets.py


import crawler
import crPanel_PlayerSheet
import crPanel_MonsterSheet
import string
import wx


#-----------------------------------------------------------------------
#------ CheckListBoxes -------------------------------------------------
#-----------------------------------------------------------------------


class plrCheckListBox(wx.CheckListBox):
    def __init__(self, parent, pan_sheet):
        self.pan_sheet = pan_sheet
        self.choices = sorted(self.pan_sheet.dct_plr.keys())
        wx.CheckListBox.__init__(self, parent, wx.ID_ANY,
                                 choices=self.choices)
        if self.GetItems():
            self.SetSelection(0)

        self.Bind(wx.EVT_LISTBOX, self.EvtListBox)


    def EvtListBox(self, event):
        if (self.GetStringSelection() == event.GetString()):
            if not self.pan_sheet.plr_panel.IsShown():
                #~ self.pan_sheet.Freeze()
                self.pan_sheet.mon_panel.Hide()
                self.pan_sheet.plr_panel.Show()
                #~ self.pan_sheet.Thaw()
                self.pan_sheet.Layout()

            self.pan_sheet.clb_mon.DeselectAll()


class monCheckListBox(wx.CheckListBox):
    def __init__(self, parent, pan_sheet):
        self.pan_sheet = pan_sheet
        self.choices = sorted(self.pan_sheet.dct_mon.keys())
        wx.CheckListBox.__init__(self, parent, wx.ID_ANY,
                                 choices=self.choices)

        self.Bind(wx.EVT_LISTBOX, self.EvtListBox)


    def EvtListBox(self, event):
        if self.GetStringSelection() == event.GetString():
            if not self.pan_sheet.mon_panel.IsShown():
                #~ self.pan_sheet.Freeze()
                self.pan_sheet.plr_panel.Hide()
                self.pan_sheet.mon_panel.Show()
                #~ self.pan_sheet.Thaw()
                self.pan_sheet.Layout()

            self.pan_sheet.clb_plr.DeselectAll()


#-----------------------------------------------------------------------
#------ Character Sheets Panel ------------------------------------------
#-----------------------------------------------------------------------


class characterSheetsPanel(wx.Panel):
    def __init__(self, parent, txt_affect, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)

        self.frame = parent.frame

        # Main Multi-line TextCtrl
        self.txt_affect = txt_affect

        self.dct_plr = {}
        self.dct_mon = {}

        for x in xrange(4):
            plr_count = x+1
            self.dct_plr["Temp Player %d" % plr_count] = {}


#-----------------------------------------------------------------------
#------ CheckListBox Panel (Left) --------------------------------------
#-----------------------------------------------------------------------


        # CheckListBox Panel
        self.clb_panel = wx.Panel(self)

        # Main CheckListBoxes (Left)
        self.clb_plr = plrCheckListBox(self.clb_panel, self)

        for m in ["Rat", "Bear", "Kobold", "Zombie"]:
            self.dct_mon[m] = {}
        self.clb_mon = monCheckListBox(self.clb_panel, self)

        # Player Add/Delete Row
        plr_btn_row = self.PlrRow()
        mon_btn_row = self.MonRow()

        # Main Sizer for Player/Monster Panel (Left)
        szr_clb_v = wx.BoxSizer(wx.VERTICAL)
        szr_clb_v.Add(plr_btn_row, 0, flag=wx.TOP, border=2)
        szr_clb_v.Add(self.clb_plr, 1, flag=wx.ALL|wx.EXPAND, border=2)
        szr_clb_v.Add(mon_btn_row, 0)
        szr_clb_v.Add(self.clb_mon, 1, flag=wx.ALL|wx.EXPAND, border=2)
        self.clb_panel.SetSizer(szr_clb_v)


#-----------------------------------------------------------------------
#------ Player/Monster Panels (Right) ----------------------------------
#-----------------------------------------------------------------------


        # Main Player Character Sheet Panel (Right)
        self.plr_panel = crPanel_PlayerSheet.plrPanel(self)
        self.mon_panel = crPanel_MonsterSheet.monPanel(self)
        self.mon_panel.Hide()

        if not self.clb_plr.GetItems():
            self.plr_panel.Hide()
            if self.clb_mon.GetItems():
                self.mon_panel.Show()
                self.clb_mon.SetSelection(0)


#-----------------------------------------------------------------------
#------ Main Sizers for Frame ------------------------------------------
#-----------------------------------------------------------------------


        # Main Horizontal Sizer
        # (CheckListBox Panel and Character Sheet Panel)
        self.szr_main_h = wx.BoxSizer(wx.HORIZONTAL)
        self.szr_main_h.Add(self.clb_panel, 0, wx.EXPAND)
        self.szr_main_h.Add(self.plr_panel, 1, wx.EXPAND)
        self.szr_main_h.Add(self.mon_panel, 1, wx.EXPAND)

        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(self.szr_main_h, 1, wx.EXPAND)

        self.SetSizer(main_sizer)


#-----------------------------------------------------------------------
#------ Sizer Creation Methods -----------------------------------------
#-----------------------------------------------------------------------

    def PlrRow(self):

        # Players Label, Add/Delete Buttons, and Sizer
        lbl1 = wx.StaticText(
               self.clb_panel, label="Players:", size=(80, -1)
               )
        lbl1.SetFont(self.MyFontB1(10))
        #-----
        btn_add = wx.Button(self.clb_panel, label="Add", size=(35, 19))
        btn_add.SetFont(self.MyFontN1(7))
        self.Bind(wx.EVT_BUTTON, self.TestButton, btn_add)
        #-----
        btn_del = wx.Button(self.clb_panel, label="Del", size=(35, 19))
        btn_del.SetFont(self.MyFontN1(7))
        #-----
        row_sizer = wx.BoxSizer(wx.HORIZONTAL)
        row_sizer.Add(lbl1, flag=wx.LEFT, border=4)
        row_sizer.Add(btn_add)
        row_sizer.Add(btn_del, flag=wx.LEFT|wx.RIGHT, border=3)

        return row_sizer

    def TestButton(self, event):
        pass


    def MonRow(self):

        # Monsters Label, Add/Delete Buttons, and Sizer
        lbl1 = wx.StaticText(
               self.clb_panel, label="Monsters:", size=(80, -1)
               )
        lbl1.SetFont(self.MyFontB1(10))
        #-----
        btn_add = wx.Button(self.clb_panel, label="Add", size=(35, 19))
        btn_add.SetFont(self.MyFontN1(7))
        #-----
        btn_del = wx.Button(self.clb_panel, label="Del", size=(35, 19))
        btn_del.SetFont(self.MyFontN1(7))
        #-----
        row_sizer = wx.BoxSizer(wx.HORIZONTAL)
        row_sizer.Add(lbl1, flag=wx.LEFT, border=4)
        row_sizer.Add(btn_add)
        row_sizer.Add(btn_del, flag=wx.LEFT|wx.RIGHT, border=3)

        return row_sizer


#-----------------------------------------------------------------------
#------ Label Methods --------------------------------------------------
#-----------------------------------------------------------------------


    def Lbl(self, lbl_text, font_size, weight="NORMAL", parent=None):
        if not parent:
            parent = self

        lbl = wx.StaticText(parent, label=lbl_text)

        if string.upper(weight) == "BOLD":
            lbl.SetFont(self.MyFontB1(font_size))
        elif string.upper(weight) == "NORMAL":
            lbl.SetFont(self.MyFontN1(font_size))
        else:
            lbl.SetFont(self.MyFontN1(font_size))

        return lbl


    def LblF(self, lbl_text, font_size, weight="NORMAL", parent=None):
        if not parent:
            parent = self

        lbl = wx.StaticText(parent, label=lbl_text)

        if string.upper(weight) == "BOLD":
            lbl.SetFont(self.MyFixedFontB1(font_size))
        elif string.upper(weight) == "NORMAL":
            lbl.SetFont(self.MyFixedFontN1(font_size))
        else:
            lbl.SetFont(self.MyFixedFontN1(font_size))

        return lbl


    def LblC(self, lbl_text, font_size, weight="NORMAL", parent=None):
        if not parent:
            parent = self

        lbl = wx.StaticText(parent,
                            label=lbl_text,
                            style=wx.ALIGN_CENTER
                            )

        if string.upper(weight) == "BOLD":
            lbl.SetFont(self.MyFontB1(font_size))
        elif string.upper(weight) == "NORMAL":
            lbl.SetFont(self.MyFontN1(font_size))
        else:
            lbl.SetFont(self.MyFontN1(font_size))

        return lbl


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
