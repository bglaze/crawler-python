#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Adventure Ideas Panel/ListCtrl module for Crawler I
#  by Brock Glaze
#
#  crAdventureIdeasPanel.py


import crawler
import random
import string
import wx
import wx.grid


def GetAdventureList():
    file_name = "adventure_ideas.txt"
    adv_list = []

    f = open(file_name, "r")
    for line in f.readlines():
        adv_list.append(line.strip())
    f.close()

    return adv_list


class adventureIdeasGrid(wx.grid.Grid):
    def __init__(self, parent, txt_affect, *args, **kwargs):
        wx.grid.Grid.__init__(self, parent, size=(510, 178),
        style=wx.SIMPLE_BORDER,
        *args, **kwargs)

        self.frame = parent.frame

        # Main Multi-line TextCtrl
        self.txt_affect = txt_affect

        # List of Ideas from File
        self.lst_ideas = GetAdventureList()

        # Current Random Seed
        self.c_seed = 0

        # Main Grid
        self.DisableDragGridSize()
        self.SetRowLabelSize(0)
        self.SetColLabelSize(0)
        self.CreateGrid(len(self.lst_ideas), 1)
        self.EnableEditing(False)
        self.EnableGridLines(False)
        self.SetCellHighlightColour((0, 120, 0))
        self.SetCellHighlightPenWidth(1)

        # Populate Grid
        for idx in xrange(len(self.lst_ideas)):
            self.SetCellValue(idx, 0, self.lst_ideas[idx])

        self.AutoSizeColumns(True)

        # Event Bindings
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.OnDoubleClick)
        
        # Disable Drag-Selecting
        wx.EVT_MOTION(self.GetGridWindow(), self.OnMouseMotion)

    def OnMouseMotion(self, event):
        if event.Dragging():
            pass
        else:
            event.Skip()

    def OnDoubleClick(self, event):
        # Write double-clicked item to the Main TextCtrl
        row = event.GetRow()
        col = event.GetCol()

        if self.frame.menu_options.IsChecked(self.frame.ID_CLEAR_TEXT):
            self.txt_affect.Clear()

        new_line = "\n"
        if self.txt_affect.GetValue() == "":
            new_line = ""
        text = "%sAdventure Idea: %s" % (new_line, self.GetCellValue(row, col))

        self.txt_affect.DoAppendText(text)

    def RandomIdea(self, event=None):
        # Set old cell back to white
        self.SetCellBackgroundColour(self.c_seed, 0, (255, 255, 255))
        self.SetCellTextColour(self.c_seed, 0, (0, 0, 0))
        self.Refresh()

        # Set focus and background on new random cell
        seed = random.randint(0, len(self.lst_ideas)-1)
        self.c_seed = seed
        self.SetCellBackgroundColour(self.c_seed, 0, (0, 120, 0))
        self.SetCellTextColour(self.c_seed, 0, (255, 255, 0))
        self.MakeCellVisible(seed, 0)

        if self.frame.menu_options.IsChecked(self.frame.ID_CLEAR_TEXT):
            self.txt_affect.Clear()

        new_line = "\n"
        if self.txt_affect.GetValue() == "":
            new_line = ""
        text = "%sAdventure Idea: %s" % (new_line, self.GetCellValue(seed, 0))

        self.txt_affect.DoAppendText(text)


#-----------------------------------------------------------------------
#------ Adventure Ideas Panel ------------------------------------------
#-----------------------------------------------------------------------


class adventureIdeasPanel(wx.Panel):
    def __init__(self, parent, txt_affect, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)

        self.frame = parent.frame

        # Main Multi-line TextCtrl
        self.txt_affect = txt_affect

        # Grid of Adventure Ideas
        self.grid_ideas = adventureIdeasGrid(self, self.txt_affect)

        # Random Idea Button
        btn_idea = wx.Button(self,
                   label="Get Random Idea", size=(-1, 21)
                   )

        self.Bind(wx.EVT_BUTTON, self.grid_ideas.RandomIdea, btn_idea)

        lbl_file = self.LblF(
        "list items stored in 'adventure_ideas.txt'", 8
        )

        h_sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        h_sizer1.Add(btn_idea)
        h_sizer1.Add(lbl_file, flag=wx.LEFT, border=57)


        # Static Box Sizer Adventure Ideas
        sb_main = wx.StaticBox(self)
        sb_main.SetFont(self.MyFontB1(8))
        sb_sizer = wx.StaticBoxSizer(sb_main, wx.VERTICAL)
        sb_sizer.Add(self.grid_ideas, flag=wx.ALL, border=5)
        sb_sizer.Add(h_sizer1, flag=wx.LEFT|wx.BOTTOM, border=5)


        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(sb_sizer, flag=wx.ALL, border=5)

        self.SetSizer(main_sizer)


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
