#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Crawler I
#  by Brock Glaze
#  brockgl.crawler@gmail.com
#
#  crawler.pyw


import crAbout
import crPanel_DiceBar
import crPage_CharacterSheets
import crPage_EncounterCalc
import crPage_AdventureIdeas
import crStatusBar
import crPanel_MainText
import os
import wx


# Toggle to show/hide dice bar on startup
DICE_BAR_ON = True

# Wildcard text for File > Save dialog
wildcard = "Text Documents (*.txt)|*.txt|"     \
           "All Files (*.*)|*.*"


# Launch App
def Main():
    app = wx.App(False)

    frame = crawlerFrame(
    parent=None, id=wx.ID_ANY, title="Crawler I", size=(1024, 768)
    )

    frame.Show()
    app.MainLoop()


class crawlerFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        # Frame Bindings
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        # Frame Attributes
        self.SetSizeHints(minW=550, minH=450)
        self.Centre()

        # Main Panel
        self.panel = wx.Panel(self)

        # Splitter Window (Splits Notebook and Text panel)
        self.splitter = wx.SplitterWindow(self.panel,
                        style=wx.SP_LIVE_UPDATE
                        )


#-----------------------------------------------------------------------
#------- Text Panel ----------------------------------------------------
#-----------------------------------------------------------------------


        # Must be created first, so other objects can access it
        self.text_panel = crPanel_MainText.textPanel(self.splitter)


#-----------------------------------------------------------------------
#------- Dice Panel ----------------------------------------------------
#-----------------------------------------------------------------------


        self.dice_bar_panel = crPanel_DiceBar.diceBarPanel(self.panel,
                              self, self.text_panel.txt_main
                              )


#-----------------------------------------------------------------------
#------- Notebook ------------------------------------------------------
#-----------------------------------------------------------------------


        self.notebook = wx.Notebook(self.splitter)

        self.notebook.AddPage(crPage_EncounterCalc.encounterCalcPage(
                      self.notebook, self, 
                      self.text_panel.txt_main
                      ),
                      text="Encounter Calculator"
                      )

#-----------------------------------------------------------------------
#------- Notebook Pages Under Development ------------------------------
#-----------------------------------------------------------------------


        #~ self.notebook.AddPage(crPage_AdventureIdeas.adventureIdeasPage(
                      #~ self.notebook, self,
                      #~ self.text_panel.txt_main
                      #~ ),
                      #~ text="Adventure Ideas"
                      #~ )
        #~ self.notebook.AddPage(crPage_CharacterSheets.characterSheetsPage(
                      #~ self.notebook, self,
                      #~ self.text_panel.txt_main
                      #~ ),
                      #~ text="Character Sheets"
                      #~ )

#-----------------------------------------------------------------------
#------- Main Sizer ----------------------------------------------------
#-----------------------------------------------------------------------


        szr_main = wx.BoxSizer(wx.VERTICAL)
        szr_main.Add(self.dice_bar_panel, 0,
                     flag=wx.LEFT|wx.RIGHT|wx.TOP|wx.EXPAND,
                     border=5
                     )
        szr_main.Add(self.splitter, 1, flag=wx.ALL|wx.EXPAND, border=5)

        self.panel.SetSizer(szr_main)


#-----------------------------------------------------------------------
#------- Menu ----------------------------------------------------------
#-----------------------------------------------------------------------


        # Primary MenuBar
        menu_bar = wx.MenuBar()


        # File Menu
        menu_file = wx.Menu()
        menu_bar.Append(menu_file, "&File")
        menu_file.Append(wx.ID_SAVE, "&Save Text")
        #~ menu_file.Append(wx.ID_PRINT, "&Print Text")
        menu_file.AppendSeparator()
        menu_file.Append(wx.ID_EXIT, "E&xit")
        #-----
        self.Bind(wx.EVT_MENU, self.SaveText, id=wx.ID_SAVE)
        #~ self.Bind(wx.EVT_MENU, self.PrintText, id=wx.ID_PRINT)
        self.Bind(wx.EVT_MENU, self.CloseWindow, id=wx.ID_EXIT)

        # Options Menu
        self.menu_options = wx.Menu()
        menu_bar.Append(self.menu_options, "&Options")
        self.ID_CLEAR_TEXT=wx.NewId() # Create New ID
        self.menu_options.Append(self.ID_CLEAR_TEXT, "Clear Text on Run",
                  "Clear Main Textbox Before Displaying New Entries",
                  kind=wx.ITEM_CHECK
                  )
        self.menu_options.Check(self.ID_CLEAR_TEXT, True)


        # View Menu
        self.menu_view = wx.Menu()
        menu_bar.Append(self.menu_view, "&View")
        #----- DiceBar SubMenu -----
        self.ID_DICE_BAR=wx.NewId() # Create New ID
        self.menu_view.Append(self.ID_DICE_BAR, "Dice Bar",
                  "Toggle Dice Bar",
                  kind=wx.ITEM_CHECK
                  )
        self.menu_view.Check(self.ID_DICE_BAR, DICE_BAR_ON)
        self.Bind(wx.EVT_MENU, self.ToggleDiceBar, id=self.ID_DICE_BAR)
        self.ToggleDiceBar()
        #----- Layout SubMenu -----
        #~ ID_LAYOUT = wx.NewId()
        #~ self.ID_SPLIT_H = wx.NewId()
        #~ self.ID_SPLIT_V = wx.NewId()
        #~ layout_submenu = wx.Menu()
        #~ layout_submenu.Append(self.ID_SPLIT_H,
                       #~ "Split Horizontally",
                       #~ "Split Window Horizontally",
                       #~ kind=wx.ITEM_CHECK
                       #~ )
        #~ layout_submenu.Append(self.ID_SPLIT_V,
                              #~ "Split Vertically",
                              #~ "Split Window Vertically",
                              #~ kind=wx.ITEM_CHECK
                              #~ )
        #~ self.menu_view.AppendMenu(ID_LAYOUT, "Layout", layout_submenu)
        #~ self.menu_view.Check(self.ID_SPLIT_V, True)
        #~ self.Bind(wx.EVT_MENU, self.SplitWindowHorizontally, id=self.ID_SPLIT_H)
        #~ self.Bind(wx.EVT_MENU, self.SplitWindowVertically, id=self.ID_SPLIT_V)


        # Help Menu
        menu_help = wx.Menu()
        menu_bar.Append(menu_help, "&Help")
        #-----
        menu_help.Append(wx.ID_ABOUT, "&About")
        #-----
        self.Bind(wx.EVT_MENU, self.ShowAbout, id=wx.ID_ABOUT)


        self.SetMenuBar(menu_bar)


#-----------------------------------------------------------------------
#------- Status Bar ----------------------------------------------------
#-----------------------------------------------------------------------


        self.status_bar = crStatusBar.CustomStatusBar(self)
        self.SetStatusBar(self.status_bar)


#-----------------------------------------------------------------------
#------- Config Splitter Window ----------------------------------------
#-----------------------------------------------------------------------


        # Config Splitter
        self.splitter.SplitVertically(
                      self.notebook,
                      self.text_panel,
                      325
                      )
        self.splitter.SetMinimumPaneSize(100)
        self.splitter.SetSashGravity(0.0)
        self.splitter.SendSizeEvent()


#-----------------------------------------------------------------------
#------ Dialogs --------------------------------------------------------
#-----------------------------------------------------------------------


    def PrintText(self, event=None):
        pass


    def SaveText(self, event=None):

        dlg_save_text = wx.FileDialog(self,
            message="Save text as ...", defaultDir=os.getcwd(),
            defaultFile="", wildcard=wildcard, style=wx.SAVE
            )

        write_file = True
        if dlg_save_text.ShowModal() == wx.ID_OK:
            path = dlg_save_text.GetPath()
            file_name = os.path.basename(path)

            if os.path.exists(path):
                dlg_file_exists = wx.MessageDialog(self,
                "%s already exists.\nDo you want to replace it?" % file_name,
                "Confirm Save Text",
                style=(wx.YES_NO | wx.ICON_EXCLAMATION)
                )
                if dlg_file_exists.ShowModal() == wx.ID_NO:
                    write_file = False
                dlg_file_exists.Destroy()

            if write_file:
                text = ""
                text += "%s, %s\n\n" % (self.status_bar.GetStatusText(1),
                                        self.status_bar.GetStatusText(2))
                text += self.text_panel.txt_main.GetValue()

                f = open(path, "w")
                f.write(text)
                f.close()

        dlg_save_text.Destroy()


    def ShowAbout(self, event=None):
        '''Display the About dialog'''

        crAbout.ShowAboutDialog(self)


#-----------------------------------------------------------------------
#------ Frame Methods --------------------------------------------------
#-----------------------------------------------------------------------


    def SplitWindowHorizontally(self, event=None):
        self.menu_view.Check(self.ID_SPLIT_H, True)
        self.menu_view.Check(self.ID_SPLIT_V, False)
        self.splitter.SetSplitMode(wx.SPLIT_HORIZONTAL)
        self.splitter.SetSashGravity(1.0)
        self.splitter.SendSizeEvent()
        self.panel.Layout()


    def SplitWindowVertically(self, event=None):
        self.menu_view.Check(self.ID_SPLIT_V, True)
        self.menu_view.Check(self.ID_SPLIT_H, False)
        self.splitter.SetSplitMode(wx.SPLIT_VERTICAL)
        self.splitter.SetSashGravity(0.0)
        self.splitter.SendSizeEvent()
        self.panel.Layout()


    # Handle toggling the dice bar (View > Dice Bar)
    def ToggleDiceBar(self, event=None):
        if self.menu_view.IsChecked(self.ID_DICE_BAR):
            self.dice_bar_panel.Show()
            self.panel.Layout()
            self.Refresh()

        else:
            self.dice_bar_panel.Hide()
            self.panel.Layout()
            self.Refresh()


    def CloseWindow(self, event):
        self.Close()


    def OnCloseWindow(self, event):
        self.status_bar.timer.Stop()
        del self.status_bar.timer
        self.Destroy()


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
    Main()
