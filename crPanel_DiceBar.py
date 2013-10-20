#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Dice-Bar Panel module for Crawler I
#  by Brock Glaze
#
#  crPanel_DiceBar.py


import crawler
import crDice
import crValidator
import random
import string
import wx


#-----------------------------------------------------------------------
#------ Custom CheckBox ------------------------------------------------
#-----------------------------------------------------------------------


class DieCheck(wx.CheckBox):
    def __init__(self, parent, times_ctrl, die, *args, **kwargs):
        wx.CheckBox.__init__(self, parent, wx.ID_ANY, *args, **kwargs)

        self.times_ctrl = times_ctrl
        self.die = die


#-----------------------------------------------------------------------
#------ Custom TextCtrl ------------------------------------------------
#-----------------------------------------------------------------------


class DiceTimesText(wx.TextCtrl):
    def __init__(self, parent, *args, **kwargs):
        wx.TextCtrl.__init__(self, parent, wx.ID_ANY,
        style=wx.TE_CENTRE|wx.SIMPLE_BORDER,
        validator=crValidator.Validator(crValidator.DIGIT_ONLY),
        *args, **kwargs)

        self.SetMaxLength(3)
        self.Bind(wx.EVT_LEFT_DOWN, self.EvtLeftClick)

    # Highlights current text when clicked
    # to make it easier to change on the fly
    def EvtLeftClick(self, event):
        self.SetFocus()
        self.SetSelection(-1, -1)


#-----------------------------------------------------------------------
#------ Dice-Bar Panel -------------------------------------------------
#-----------------------------------------------------------------------


class diceBarPanel(wx.Panel):
    def __init__(self, parent, frame, txt_affect, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)


        # parent = Main Frame
        self.frame = frame


        # Main Multi-line TextCtrl
        self.txt_affect = txt_affect


        self.DieCheckBoxes = []


        # Attributes Die Button
        btn_attr_die = wx.Button(self, label="Attributes", size=(-1, 21))
        btn_attr_die.SetToolTip(wx.ToolTip("Roll 6 Character Attributes"))
        self.Bind(wx.EVT_BUTTON, lambda event:
            self.DieRoller(event, "attributes", None), btn_attr_die)

        # Percentage Die Button
        btn_perc_die = wx.Button(self, label="Percentage", size=(-1, 21))
        btn_perc_die.SetToolTip(wx.ToolTip("Roll Percentage Dice (2d10)"))
        self.Bind(wx.EVT_BUTTON, lambda event:
            self.DieRoller(event, "percentage", None), btn_perc_die)

        # d4 Sizer, TextCtrl and Button
        szr_d4 = wx.BoxSizer(wx.HORIZONTAL)
        self.txt_d4 = DiceTimesText(self, size=(29, 21))
        self.txt_d4.SetValue("1")
        btn_d4 = wx.Button(self, label=("d4"), size=(35, 21))
        self.Bind(wx.EVT_BUTTON, lambda event:
            self.DieRoller(event, 4, self.txt_d4), btn_d4)
        self.chk_d4 = DieCheck(self, self.txt_d4, 4)
        self.DieCheckBoxes.append(self.chk_d4)

        szr_d4.Add(self.chk_d4)
        szr_d4.Add(self.txt_d4, flag=wx.LEFT, border=2)
        szr_d4.Add(btn_d4, flag=wx.LEFT, border=1)

        # d6 Sizer, TextCtrl and Button
        szr_d6 = wx.BoxSizer(wx.HORIZONTAL)
        self.txt_d6 = DiceTimesText(self, size=(29, 21))
        self.txt_d6.SetValue("1")
        btn_d6 = wx.Button(self, label=("d6"), size=(35, 21))
        self.Bind(wx.EVT_BUTTON, lambda event:
            self.DieRoller(event, 6, self.txt_d6), btn_d6)
        self.chk_d6 = DieCheck(self, self.txt_d6, 6)
        self.DieCheckBoxes.append(self.chk_d6)

        szr_d6.Add(self.chk_d6)
        szr_d6.Add(self.txt_d6, flag=wx.LEFT, border=2)
        szr_d6.Add(btn_d6, flag=wx.LEFT, border=1)

        # d8 Sizer, TextCtrl and Button
        szr_d8 = wx.BoxSizer(wx.HORIZONTAL)
        self.txt_d8 = DiceTimesText(self, size=(29, 21))
        self.txt_d8.SetValue("1")
        btn_d8 = wx.Button(self, label=("d8"), size=(35, 21))
        self.Bind(wx.EVT_BUTTON, lambda event:
            self.DieRoller(event, 8, self.txt_d8), btn_d8)
        self.chk_d8 = DieCheck(self, self.txt_d8, 8)
        self.DieCheckBoxes.append(self.chk_d8)

        szr_d8.Add(self.chk_d8)
        szr_d8.Add(self.txt_d8, flag=wx.LEFT, border=2)
        szr_d8.Add(btn_d8, flag=wx.LEFT, border=1)

        # d10 Sizer, TextCtrl and Button
        szr_d10 = wx.BoxSizer(wx.HORIZONTAL)
        self.txt_d10 = DiceTimesText(self, size=(29, 21))
        self.txt_d10.SetValue("1")
        btn_d10 = wx.Button(self, label=("d10"), size=(35, 21))
        self.Bind(wx.EVT_BUTTON, lambda event:
            self.DieRoller(event, 10, self.txt_d10), btn_d10)
        self.chk_d10 = DieCheck(self, self.txt_d10, 10)
        self.DieCheckBoxes.append(self.chk_d10)

        szr_d10.Add(self.chk_d10)
        szr_d10.Add(self.txt_d10, flag=wx.LEFT, border=2)
        szr_d10.Add(btn_d10, flag=wx.LEFT, border=1)

        # d12 Sizer, TextCtrl and Button
        szr_d12 = wx.BoxSizer(wx.HORIZONTAL)
        self.txt_d12 = DiceTimesText(self, size=(29, 21))
        self.txt_d12.SetValue("1")
        btn_d12 = wx.Button(self, label=("d12"), size=(35, 21))
        self.Bind(wx.EVT_BUTTON, lambda event:
            self.DieRoller(event, 12, self.txt_d12), btn_d12)
        self.chk_d12 = DieCheck(self, self.txt_d12, 12)
        self.DieCheckBoxes.append(self.chk_d12)

        szr_d12.Add(self.chk_d12)
        szr_d12.Add(self.txt_d12, flag=wx.LEFT, border=2)
        szr_d12.Add(btn_d12, flag=wx.LEFT, border=1)

        # d20 Sizer, TextCtrl and Button
        szr_d20 = wx.BoxSizer(wx.HORIZONTAL)
        self.txt_d20 = DiceTimesText(self, size=(29, 21))
        self.txt_d20.SetValue("1")
        btn_d20 = wx.Button(self, label=("d20"), size=(35, 21))
        self.Bind(wx.EVT_BUTTON, lambda event:
            self.DieRoller(event, 20, self.txt_d20), btn_d20)
        self.chk_d20 = DieCheck(self, self.txt_d20, 20)
        self.DieCheckBoxes.append(self.chk_d20)

        szr_d20.Add(self.chk_d20)
        szr_d20.Add(self.txt_d20, flag=wx.LEFT, border=2)
        szr_d20.Add(btn_d20, flag=wx.LEFT, border=1)

        # d100 Sizer, TextCtrl and Button
        szr_d100 = wx.BoxSizer(wx.HORIZONTAL)
        self.txt_d100 = DiceTimesText(self, size=(29, 21))
        self.txt_d100.SetValue("1")
        btn_d100 = wx.Button(self, label=("d100"), size=(35, 21))
        self.Bind(wx.EVT_BUTTON, lambda event:
            self.DieRoller(event, 100, self.txt_d100), btn_d100)
        self.chk_d100 = DieCheck(self, self.txt_d100, 100)
        self.DieCheckBoxes.append(self.chk_d100)

        szr_d100.Add(self.chk_d100)
        szr_d100.Add(self.txt_d100, flag=wx.LEFT, border=2)
        szr_d100.Add(btn_d100, flag=wx.LEFT, border=1)

        # Show Rolls CheckBox
        self.chk_show_rolls = wx.CheckBox(self, label="Show Rolls")
        self.chk_show_rolls.SetToolTip(wx.ToolTip(
        "Show the individual die rolls as well as the sum total."
        ))

        # Roll Checked Dice
        btn_roll_checked = wx.Button(self, label=("Roll Checked"), size=(75, 21))
        btn_roll_checked.SetToolTip(wx.ToolTip(
        "Roll all dice that are checked, and display the sum total."
        ))
        self.Bind(wx.EVT_BUTTON, self.RollCheckedDice, btn_roll_checked)

        # Reset Dice Ctrls
        btn_db_reset = wx.Button(self, label=("Reset Dice"), size=(75, 21))
        self.Bind(wx.EVT_BUTTON, self.ResetDB, btn_db_reset)


        # Main Sizer Adds
        szr_dice = wx.BoxSizer(wx.HORIZONTAL)
        szr_dice.Add(btn_attr_die, flag=wx.RIGHT, border=5)
        szr_dice.Add(btn_perc_die, flag=wx.RIGHT, border=10)
        szr_dice.Add(szr_d4, flag=wx.RIGHT, border=5)
        szr_dice.Add(szr_d6, flag=wx.RIGHT, border=5)
        szr_dice.Add(szr_d8, flag=wx.RIGHT, border=5)
        szr_dice.Add(szr_d10, flag=wx.RIGHT, border=5)
        szr_dice.Add(szr_d12, flag=wx.RIGHT, border=5)
        szr_dice.Add(szr_d20, flag=wx.RIGHT, border=5)
        szr_dice.Add(szr_d100, flag=wx.RIGHT, border=10)
        szr_dice.Add(self.chk_show_rolls, flag=wx.RIGHT, border=5)
        szr_dice.Add(btn_roll_checked, flag=wx.RIGHT, border=5)
        szr_dice.Add(btn_db_reset)

        self.SetSizer(szr_dice)


    def ResetDB(self, event=None):

        # Reset All Editable Ctrls to their Defaults
        self.txt_d4.SetValue("1")
        self.chk_d4.SetValue(False)

        self.txt_d6.SetValue("1")
        self.chk_d6.SetValue(False)

        self.txt_d8.SetValue("1")
        self.chk_d8.SetValue(False)

        self.txt_d10.SetValue("1")
        self.chk_d10.SetValue(False)

        self.txt_d12.SetValue("1")
        self.chk_d12.SetValue(False)

        self.txt_d20.SetValue("1")
        self.chk_d20.SetValue(False)

        self.txt_d100.SetValue("1")
        self.chk_d100.SetValue(False)

        self.chk_show_rolls.SetValue(False)


    def DieRoller(self, event, die, times_ctrl):

        if times_ctrl:
            # If times text ctrl contains characters that are not
            # numbers, replace with 1
            if not times_ctrl.GetValue().isdigit():
                times_ctrl.SetValue("1")

            times = int(times_ctrl.GetValue())
        else:
            # If times text ctrl is empty, auto-fill with 1
            times = 1

        if self.frame.menu_options.IsChecked(self.frame.ID_CLEAR_TEXT):
            self.txt_affect.Clear()

        new_line = "\n"
        if self.txt_affect.GetValue() == "":
            new_line = ""


        # Roll Attribute Dice
        if string.lower(str(die)) == "attributes":
            attr_roll = crDice.RollAttributes()

            if self.chk_show_rolls.IsChecked():
                text = "%sAttributes:\n" % (new_line)

                for a in attr_roll:
                    text += ("{%d, %d, %d, %d} = %d" % (
                    a[1][0], a[1][1],
                    a[1][2], a[1][3],
                    a[0]
                    ))

                    if attr_roll.index(a) != len(attr_roll) - 1:
                        text += "\n"

            else:
                text = "%sAttributes: " % (new_line)

                for a in attr_roll:
                    text += "%d" % a[0]

                    if attr_roll.index(a) != len(attr_roll) - 1:
                        text += ", "

        # Roll Percentage Dice
        elif string.lower(str(die)) == "percentage":
            perc_roll = crDice.RollPercentage()

            if self.chk_show_rolls.IsChecked():
                text = (
                "%sPercentage: {%d, %d} = %d%%" % (
                new_line,
                perc_roll[0][0], perc_roll[0][1],
                perc_roll[1]
                ))
            else:
                text = (
                "%sPercentage: %d%%" % (new_line, perc_roll[1])
                )

        # Roll all other dice
        else:
            text = "%s%dd%d:" % (new_line, times, die)
            rolls = crDice.RollDice(times, die)

            if self.chk_show_rolls.IsChecked():
                text += " {"
                for die in rolls[0]:
                    text += "%d, " % die

                text = text[:-2]
                text += "} = %d" % rolls[1]

            else:
                text += " %d" % rolls[1]

        self.txt_affect.DoAppendText(text)

    # Allows users to check multiple dice, and roll them simultaneously.
    def RollCheckedDice(self, event=None):
        for chk in self.DieCheckBoxes:
            if chk.GetValue():
                if self.frame.menu_options.IsChecked(self.frame.ID_CLEAR_TEXT):
                    self.txt_affect.Clear()

        text = ""
        total_dice = []
        for chk in self.DieCheckBoxes:
            if chk.GetValue():

                if chk.times_ctrl.GetValue().isdigit():
                    times = int(chk.times_ctrl.GetValue())
                else:
                    times = 1

                die = chk.die
                
                text += "\n%dd%d:" % (times, die)
                rolls = crDice.RollDice(times, die)

                if self.chk_show_rolls.IsChecked():
                    text += " {"
                    for die in rolls[0]:
                        text += "%d, " % die

                    text = text[:-2]
                    text += "} = %d" % rolls[1]

                else:
                    text += " %d" % rolls[1]

                total_dice.append(rolls[1])

        if text:

            nl_idx = 0
            if self.txt_affect.GetValue() == "":
                nl_idx = 1

            text += "\n\nDice Total: %d\n" % (sum(total_dice))

            self.txt_affect.DoAppendText(text[nl_idx:])


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
