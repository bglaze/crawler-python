#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  An Encounter Calculator Panel module for Crawler I
#  by Brock Glaze
#
#  crPanel_EncounterCalc.py


import crawler
import crDice
import crCalc_Difficulty as difficulty_lib
import crCalc_Experience as experience_lib
import crCalc_Treasure_Goods as goods_lib
import crCalc_Treasure_Mundane as mundane_lib
import crCalc_Treasure_Armor as armor_lib
import crCalc_Treasure_Weapons as weapon_lib
import crCalc_Treasure_Potions as potion_lib
import crCalc_Treasure_Rings as ring_lib
import crCalc_Treasure_Rods as rod_lib
import crCalc_Treasure_Scrolls as scroll_lib
import crCalc_Treasure_Staffs as staff_lib
import crCalc_Treasure_Wands as wand_lib
import crCalc_Treasure_Wondrous as wondrous_lib
import crCalc_Treasure_TextGen as gen_treasure_lib
import crCalc_Treasure as treasure_lib
import crValidator
import random
import string
import wx

default_tr_rating = 10

choices_si = {
"Gem": ["None"],
"Art": ["None"],
"Mundane Item": ["None"],
"Common Melee": ["Any", "Standard", "Masterwork"],
"Common Ranged": ["Any", "Standard", "Masterwork"],
"Uncommon Weapon": ["Any", "Standard", "Masterwork"],
"Common Armor": ["Any", "Standard", "Masterwork"],
"Common Shield": ["Any", "Standard", "Masterwork"],
"Magic Armor/Shield": ["Any", "Minor", "Medium", "Major"],
"Magic Weapon": ["Any", "Minor", "Medium", "Major"],
"Potion/Oil": ["Any", "Minor", "Medium", "Major"],
"Ring": ["Any", "Minor", "Medium", "Major"],
"Rod": ["Any", "Medium", "Major"],
"Arcane Scroll": ["Any", "Minor", "Medium", "Major"],
"Divine Scroll": ["Any", "Minor", "Medium", "Major"],
"Staff": ["Any", "Medium", "Major"],
"Wand": ["Any", "Minor", "Medium", "Major"],
"Wondrous Item": ["Any", "Minor", "Medium", "Major"]
}

# Need to use a list instead of choices_si.keys()
# Because the specific order of items needs to be preserved.
lst_choices = [
"Gem",
"Art",
"Mundane Item",
"Common Melee",
"Common Ranged",
"Uncommon Weapon",
"Common Armor",
"Common Shield",
"Magic Armor/Shield",
"Magic Weapon",
"Potion/Oil",
"Ring",
"Rod",
"Arcane Scroll",
"Divine Scroll",
"Staff",
"Wand",
"Wondrous Item",
]


#-----------------------------------------------------------------------
#------ Get Control Values Function ------------------------------------
#-----------------------------------------------------------------------


def GetCtrlValues(aCtrlLst):
    aDct = {}
    aLst = []

    for t in aCtrlLst:
        if t[0].GetValue() and t[1].GetValue():
            number = float(t[0].GetValue())
            level = float(t[1].GetValue())
            if not aDct.has_key(level):
                aDct[level] = number
            else:
                aDct[level] += number

    for level in aDct.keys():
            aLst.append(
            (aDct[level], level)
            )

    return aLst


#-----------------------------------------------------------------------
#------ Custom TextCtrl ------------------------------------------------
#-----------------------------------------------------------------------


class CalcText(wx.TextCtrl):
    def __init__(self, parent, max_length=3, *args, **kwargs):
        wx.TextCtrl.__init__(self, parent, wx.ID_ANY,
        style=wx.TE_CENTRE|wx.SIMPLE_BORDER,
        validator=crValidator.Validator(crValidator.DIGIT_ONLY),
        *args, **kwargs)

        self.SetMaxLength(max_length)
        self.Bind(wx.EVT_LEFT_DOWN, self.EvtLeftClick)

    # Highlights current text when clicked
    # to make it easier to change on the fly
    def EvtLeftClick(self, event):
        self.SetFocus()
        self.SetSelection(-1, -1)


class CalcTextDecimal(wx.TextCtrl):
    def __init__(self, parent, *args, **kwargs):
        wx.TextCtrl.__init__(self, parent, wx.ID_ANY,
        style=wx.TE_CENTRE|wx.SIMPLE_BORDER,
        validator=crValidator.Validator(crValidator.DIGIT_DECIMAL_ONLY),
        *args, **kwargs)

        self.Bind(wx.EVT_LEFT_DOWN, self.EvtLeftClick)
        self.Bind(wx.EVT_TEXT, self.EvtText)

    # Highlights current text when clicked
    # to make it easier to change on the fly
    def EvtLeftClick(self, event):
        self.SetFocus()
        self.SetSelection(-1, -1)

    def EvtText(self, event):
        if self.GetValue() and self.GetValue()[0] == ".":
            self.SetMaxLength(4)
        else:
            self.SetMaxLength(3)


#-----------------------------------------------------------------------
#------ Random Specific Item Choice --------------------------------------
#-----------------------------------------------------------------------


class SpecificItemChoice(wx.Choice):
    def __init__(self, parent, choice_affect, *args, **kwargs):
        wx.Choice.__init__(self, parent, wx.ID_ANY,
        size=(130, 21), choices=lst_choices,
        *args, **kwargs)

        self.choice_affect = choice_affect

        self.Bind(wx.EVT_CHOICE, self.SetItemQuality)

        self.SetSelection(2)
        self.SetItemQuality()


    def SetItemQuality(self, event=None):
        if (
        self.choice_affect.GetItems() !=
        choices_si[self.GetStringSelection()]
        ):
            self.choice_affect.Clear()
            for quality in choices_si[self.GetStringSelection()]:
                self.choice_affect.Append(quality)
            self.choice_affect.SetSelection(0)


#-----------------------------------------------------------------------
#------ Treasure Radio Button ------------------------------------------
#-----------------------------------------------------------------------


class TreasureRadio(wx.RadioButton):
    def __init__(self, parent, *args, **kwargs):
        wx.RadioButton.__init__(self, parent, wx.ID_ANY,
        *args, **kwargs)

        self.parent = parent

        self.Bind(wx.EVT_RADIOBUTTON, self.SetTreasureChoices)


    def SetTreasureChoices(self, event=None):
        for t in self.parent.monCtrlLst:
            if t[2].GetValue():
                lst_choices = t[3]
                self.parent.choice_coins.SetSelection(lst_choices[0])
                self.parent.choice_goods.SetSelection(lst_choices[1])
                self.parent.choice_items.SetSelection(lst_choices[2])


#-----------------------------------------------------------------------
#------ Treasure Choice ------------------------------------------------
#-----------------------------------------------------------------------

class TreasureRatingChoice(wx.Choice):
    def __init__(self, parent, lst_index, *args, **kwargs):
        wx.Choice.__init__(self, parent, wx.ID_ANY,
        size=(75, 21),
        *args, **kwargs)

        self.parent = parent
        self.lst_index = lst_index

        self.Bind(wx.EVT_CHOICE, self.SetRating)

    def SetRating(self, event=None):
        for t in self.parent.monCtrlLst:
            if t[2].GetValue():
                lst_choices = t[3]
                lst_choices[self.lst_index] = self.GetCurrentSelection()
        


#-----------------------------------------------------------------------
#------ Encounter Calculator Panel -------------------------------------
#-----------------------------------------------------------------------

class encCalcPanel(wx.Panel):
    def __init__(self, parent, frame, txt_affect, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)

        self.avg_list = []

        self.frame = frame

        # Main Multi-line TextCtrl
        self.txt_affect = txt_affect


        # Lists to store TextCtrls for Calculations
        self.plrCtrlLst = []
        self.monCtrlLst = []


        # Top Labels
        lbl_num_pcs = self.LblC("# PCs", 7, "Bold")
        lbl_pc_level = self.LblC("Level", 7, "Bold")
        lbl_num_foes = self.LblC("# Foes", 7, "Bold")
        lbl_cr = self.LblC("CR", 7, "Bold")
        lbl_cr.SetToolTip(wx.ToolTip(
        "Combat Rating"
        ))

        lbl_tr = self.LblC("Set TR*", 7, "Bold")
        lbl_tr.SetForegroundColour((200, 150, 0))
        lbl_tr.SetToolTip(wx.ToolTip(
        "Set the Treasure Rating (below) for the selected row of foes."
        ))

        # Top Label Sizer
        szr_top_labels_h = wx.BoxSizer(wx.HORIZONTAL)
        szr_top_labels_h.Add(lbl_num_pcs, flag=wx.LEFT, border=5)
        szr_top_labels_h.Add(lbl_pc_level, flag=wx.LEFT, border=31)
        szr_top_labels_h.Add(lbl_num_foes, flag=wx.LEFT, border=25)
        szr_top_labels_h.Add(lbl_cr, flag=wx.LEFT, border=34)
        szr_top_labels_h.Add(lbl_tr, flag=wx.LEFT, border=18)


        # TextCtrl, Label, and SpinButton Rows
        self.szr_exp_calc_rows = wx.BoxSizer(wx.VERTICAL)
        self.szr_exp_calc_rows.Add(szr_top_labels_h)
        first_row = True
        for row in xrange(6):
            self.szr_exp_calc_rows.Add(self.OneRow(first_row),
                                   flag=wx.TOP|wx.BOTTOM, border=3
                                   )
            if first_row:
                first_row = False


        # Buttons and Button Sizer
        btn_exp_calc = wx.Button(self,
                       label="Experience", size=(67, 21)
                       )
        btn_difficulty = wx.Button(self,
                         label="Difficulty", size=(67, 21)
                         )
        btn_gold_value = wx.Button(self,
                       label="Avg. Treasure Value", size=(115, 21)
                       )
        self.Bind(wx.EVT_BUTTON, self.CalcExp, btn_exp_calc)
        self.Bind(wx.EVT_BUTTON, self.CalcDifficulty, btn_difficulty)
        self.Bind(wx.EVT_BUTTON, self.CalcAvgTreasureValue, btn_gold_value)


        szr_h_btns = wx.BoxSizer(wx.HORIZONTAL)
        szr_h_btns.Add(btn_exp_calc)
        szr_h_btns.Add(btn_difficulty,
                       flag=wx.LEFT, border=5
                       )
        szr_h_btns.Add(btn_gold_value,
                       flag=wx.LEFT, border=5
                       )

        szr_enc_calc_v1 = wx.BoxSizer(wx.VERTICAL)
        szr_enc_calc_v1.Add(self.szr_exp_calc_rows, flag=wx.ALL, border=5)
        szr_enc_calc_v1.Add(szr_h_btns, flag=wx.ALL, border=5)


#------ Treasure Box ---------------------------------------------------


        # Treasure Calculator Labels
        lbl_coins = self.LblC("Coins*", 7, "Bold")
        lbl_coins.SetForegroundColour((200, 150, 0))
        lbl_goods = self.LblC("Goods*", 7, "Bold")
        lbl_goods.SetForegroundColour((200, 150, 0))
        lbl_items = self.LblC("Items*", 7, "Bold")
        lbl_items.SetForegroundColour((200, 150, 0))        

        szr_tr_labels_h = wx.BoxSizer(wx.HORIZONTAL)
        szr_tr_labels_h.Add(lbl_coins, flag=wx.LEFT, border=7)
        szr_tr_labels_h.Add(lbl_goods, flag=wx.LEFT, border=47)
        szr_tr_labels_h.Add(lbl_items, flag=wx.LEFT, border=44)

        # Treasure ChoiceBoxes
        choices_tr = ["None", "10%", "20%", "30%", "40%",
                      "50%", "60%", "70%", "80%", "90%",
                      "Standard", "Double", "Triple", "Quadruple"]
        self.choice_coins = TreasureRatingChoice(self, 0,
                            choices=choices_tr
                            )
        self.choice_coins.SetSelection(default_tr_rating)
        self.choice_goods = TreasureRatingChoice(self, 1,
                            choices=choices_tr
                            )
        self.choice_goods.SetSelection(default_tr_rating)
        self.choice_items = TreasureRatingChoice(self, 2,
                            choices=choices_tr
                            )
        self.choice_items.SetSelection(default_tr_rating)

        szr_tr_choice = wx.BoxSizer(wx.HORIZONTAL)
        szr_tr_choice.Add(self.choice_coins, flag=wx.LEFT, border=5)
        szr_tr_choice.Add(self.choice_goods, flag=wx.LEFT, border=5)
        szr_tr_choice.Add(self.choice_items, flag=wx.LEFT|wx.RIGHT, border=5)


        # Treasure Buttons
        btn_tr_calc = wx.Button(self,
                      label="Generate Treasure", size=(110, 21)
                      )
        self.Bind(wx.EVT_BUTTON, self.CalcTreasure, btn_tr_calc)

        szr_tr_calc_h = wx.BoxSizer(wx.HORIZONTAL)
        szr_tr_calc_h.Add(btn_tr_calc, flag=wx.RIGHT, border=5)

        # Full Treasure Box Sizer
        sb_treasure = wx.StaticBox(self, label="Full Treasure")
        sb_treasure.SetFont(self.MyFontB1(7))
        sb_treasure_sizer = wx.StaticBoxSizer(sb_treasure, wx.VERTICAL)
        sb_treasure_sizer.Add(szr_tr_labels_h, flag=wx.TOP|wx.BOTTOM, border=6)
        sb_treasure_sizer.Add(szr_tr_choice, flag=wx.BOTTOM, border=8)
        sb_treasure_sizer.Add(szr_tr_calc_h, flag=wx.ALL, border=5)


        # Single Item Label, ChoiceBox, and Button
        lbl_si = self.LblC("Item Type", 7)
        lbl_si_quality = self.LblC("Quality", 7)
        szr_lbl_si_h = wx.BoxSizer(wx.HORIZONTAL)
        szr_lbl_si_h.Add(lbl_si, flag=wx.LEFT, border=7)
        szr_lbl_si_h.Add(lbl_si_quality, flag=wx.LEFT, border=90)
        szr_lbl_si_h2 = wx.BoxSizer(wx.HORIZONTAL)
        szr_lbl_si_h2.Add(szr_lbl_si_h, flag=wx.BOTTOM, border=1)

        self.choice_si_quality = wx.Choice(self, size=(100, 21))
        self.choice_specific_item = SpecificItemChoice(self,
                                    self.choice_si_quality)

        szr_si_h = wx.BoxSizer(wx.HORIZONTAL)
        szr_si_h.Add(self.choice_specific_item, flag=wx.ALL, border=5)
        szr_si_h.Add(self.choice_si_quality, flag=wx.RIGHT|wx.TOP|wx.BOTTOM, border=5)



        # Choose how many Specific items by number or gold value
        lbl_si_count = self.LblC("Count", 7)
        lbl_si_gold_worth = self.LblC("Worth (GP)", 7)
        szr_lbl_si_h3 = wx.BoxSizer(wx.HORIZONTAL)
        szr_lbl_si_h3.Add(lbl_si_count, flag=wx.LEFT, border=7)
        szr_lbl_si_h3.Add(lbl_si_gold_worth, flag=wx.LEFT, border=53)
        self.txt_spec_item_count = CalcText(self, 2, size=(50, 21))
        self.txt_spec_item_count.SetValue("1")
        self.txt_spec_item_count.SetToolTip(wx.ToolTip(
        "Generate this exact number of items."
        ))
        self.rdo_spec_item_count = wx.RadioButton(self, style=wx.RB_GROUP)
        szr_si_h2 = wx.BoxSizer(wx.HORIZONTAL)
        szr_si_h2.Add(self.txt_spec_item_count, flag=wx.RIGHT, border=5)
        szr_si_h2.Add(self.rdo_spec_item_count, flag=wx.TOP, border=3)

        self.txt_spec_item_worth = CalcText(self, 6, size=(50, 21))
        self.txt_spec_item_worth.SetValue("10000")
        self.txt_spec_item_worth.SetToolTip(wx.ToolTip(
        "Warning: This is an approximate limiter.\n"
        "Items will be generated until the sum of their values meets or exceeds this set value.\n"
        "If an item's intrinsic value is very high, the total value will often exceed this set value."
        ))
        self.rdo_spec_item_worth = wx.RadioButton(self)
        szr_si_h3 = wx.BoxSizer(wx.HORIZONTAL)
        szr_si_h3.Add(self.txt_spec_item_worth, flag=wx.RIGHT, border=5)
        szr_si_h3.Add(self.rdo_spec_item_worth, flag=wx.TOP, border=3)

        szr_si_amount_h = wx.BoxSizer(wx.HORIZONTAL)
        szr_si_amount_h.Add(szr_si_h2, flag=wx.LEFT, border=5)
        szr_si_amount_h.Add(szr_si_h3, flag=wx.LEFT, border=10)



        btn_si = wx.Button(self,
                 label="Generate Items", size=(110, 21)
                 )
        self.Bind(wx.EVT_BUTTON, self.GetSingleItem, btn_si)

        # Single Item Box Sizer
        sb_treasure_si = wx.StaticBox(self, label="Get Items of Specific Type")
        sb_treasure_si.SetFont(self.MyFontB1(7))
        sb_treasure_si_sizer = wx.StaticBoxSizer(sb_treasure_si, wx.VERTICAL)
        sb_treasure_si_sizer.Add(szr_lbl_si_h2, flag=wx.TOP, border=3)
        sb_treasure_si_sizer.Add(szr_si_h)
        sb_treasure_si_sizer.Add(szr_lbl_si_h3, flag=wx.BOTTOM, border=3)
        sb_treasure_si_sizer.Add(szr_si_amount_h, flag=wx.BOTTOM, border=8)
        sb_treasure_si_sizer.Add(btn_si, flag=wx.ALL, border=5)


        btn_reset = wx.Button(self,
                    label="Reset Calculator", size=(-1, 21)
                    )
        self.Bind(wx.EVT_BUTTON, self.ResetCalc, btn_reset)


#-----------------------------------------------------------------------


        # Static Box Sizer Experience Calculator
        sb_main = wx.StaticBox(self)
        sb_main.SetFont(self.MyFontB1(8))
        sb_main_sizer = wx.StaticBoxSizer(sb_main, wx.VERTICAL)
        sb_main_sizer.Add(szr_enc_calc_v1)
        sb_main_sizer.Add(sb_treasure_sizer,
                          flag=wx.ALL|wx.ALIGN_CENTER,
                          border=5)
        sb_main_sizer.Add(sb_treasure_si_sizer,
                          flag=wx.ALL|wx.ALIGN_CENTER,
                          border=5)
        sb_main_sizer.Add(btn_reset, flag=wx.ALL|wx.ALIGN_RIGHT, border=7)

        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(sb_main_sizer, flag=wx.ALL, border=5)

        self.SetSizer(main_sizer)


    def ResetCalc(self, event=None):

        # Reset Player Ctrls
        for t in self.plrCtrlLst:
            t[0].Clear()
            t[1].Clear()

        # Reset Monster Ctrls
        top_row = True
        for t in self.monCtrlLst:
            t[0].Clear()
            t[1].Clear()

            if top_row:
                t[2].SetValue(True)
                top_row = False

            for x in xrange(len(t[3])):
                t[3][x] = default_tr_rating

        # Reset Treasure Rating Choices
        self.choice_coins.SetSelection(default_tr_rating)
        self.choice_goods.SetSelection(default_tr_rating)
        self.choice_items.SetSelection(default_tr_rating)

        # Reset Specific Item Type Choice
        self.choice_specific_item.SetSelection(2)
        self.choice_specific_item.SetItemQuality()

        # Reset Count and Worth Ctrls
        self.txt_spec_item_count.SetValue("1")
        self.rdo_spec_item_count.SetValue(True)
        self.txt_spec_item_worth.SetValue("10000")


    def OneRow(self, first_row):
        txt_width = 40

        # PC Controls
        txt_pc_times = CalcText(self, size=(txt_width, 21))
        txt_pc_lvl = CalcText(self, size=(txt_width, 21))
        self.plrCtrlLst.append((txt_pc_times, txt_pc_lvl))

        # Monster Controls
        txt_cr_times = CalcText(self, size=(txt_width, 21))
        txt_cr_lvl = CalcTextDecimal(self, size=(txt_width, 21))

        # Set First-Row RadioButton to Primary
        if first_row:
            rdo_treasure = TreasureRadio(self, style=wx.RB_GROUP)
        else:
            rdo_treasure = TreasureRadio(self)

        self.monCtrlLst.append(
        (txt_cr_times, txt_cr_lvl, rdo_treasure,
        [default_tr_rating, default_tr_rating, default_tr_rating])
        )


        # Main Sizer for Row
        row_sizer = wx.BoxSizer(wx.HORIZONTAL)
        row_sizer.Add(txt_pc_times)
        row_sizer.Add(self.LblF("x", 10, "Bold"),
                      flag=wx.LEFT|wx.RIGHT, border=5
                      )
        row_sizer.Add(txt_pc_lvl)

        row_sizer.Add(txt_cr_times, flag=wx.LEFT, border=15)
        row_sizer.Add(self.LblF("x", 10, "Bold"),
                      flag=wx.LEFT|wx.RIGHT, border=5
                      )
        row_sizer.Add(txt_cr_lvl, flag=wx.RIGHT, border=16)
        row_sizer.Add(rdo_treasure, flag=wx.TOP, border=3)

        return row_sizer


    def CalcExp(self, event=None):
        calc = experience_lib.ExperienceTextulator
        plrLst = GetCtrlValues(self.plrCtrlLst)
        monLst = GetCtrlValues(self.monCtrlLst)

        if plrLst and monLst:

            if self.frame.menu_options.IsChecked(self.frame.ID_CLEAR_TEXT):
                self.txt_affect.Clear()

            for line in calc(plrLst, monLst):
                new_line = "\n"
                if self.txt_affect.GetValue() == "":
                    new_line = ""

                self.txt_affect.DoAppendText("%s%s" % (new_line, line))


    def CalcDifficulty(self, event=None):
        calc = difficulty_lib.DifficultyTextulator
        plrLst = GetCtrlValues(self.plrCtrlLst)
        monLst = GetCtrlValues(self.monCtrlLst)

        if plrLst and monLst:

            if self.frame.menu_options.IsChecked(self.frame.ID_CLEAR_TEXT):
                self.txt_affect.Clear()

            new_line = "\n"
            if self.txt_affect.GetValue() == "":
                new_line = ""

            self.txt_affect.DoAppendText(
                            "%s%s" % (new_line, calc(plrLst, monLst))
                            )


    def CalcAvgTreasureValue(self, event=None):
        calc = treasure_lib.AvgTreasureValueTextulator
        plrLst = GetCtrlValues(self.plrCtrlLst)
        monLst = GetCtrlValues(self.monCtrlLst)

        if monLst:

            if self.frame.menu_options.IsChecked(self.frame.ID_CLEAR_TEXT):
                self.txt_affect.Clear()

            new_line = "\n"
            if self.txt_affect.GetValue() == "":
                new_line = ""

            self.txt_affect.DoAppendText(
                            "%s%s" % (new_line, calc(plrLst, monLst))
                            )


    def CalcTreasure(self, event=None):
        calc = gen_treasure_lib.FullTreasureTextulator
        monLst = GetCtrlValues(self.monCtrlLst)

        if monLst:
            c = calc(self.txt_affect, self.frame, self.monCtrlLst)

            # Print Average Treasure Value
            #~ self.avg_list.append(c)
            #~ print sum(self.avg_list) / len(self.avg_list)


    # Get Single Item
    def GetSingleItem(self, event=None):


        current_item = self.choice_specific_item.GetStringSelection()
        current_quality = self.choice_si_quality.GetStringSelection()

        Any_Quality = False
        if string.upper(current_quality) == "ANY":
            Any_Quality = True

        if self.frame.menu_options.IsChecked(self.frame.ID_CLEAR_TEXT):
            self.txt_affect.Clear()

        if (not self.txt_spec_item_count.GetValue()
        or self.txt_spec_item_count.GetValue() == "0"):
            self.txt_spec_item_count.SetValue("1")

        if (not self.txt_spec_item_worth.GetValue()
        or self.txt_spec_item_worth.GetValue() == "0"):
            self.txt_spec_item_worth.SetValue("1")

        lst_text = []
        number = 0
        worth = 0
        while True:

            if Any_Quality:
                lst_qualities = self.choice_si_quality.GetItems()[1:]
                random.shuffle(lst_qualities)
                current_quality = lst_qualities[0]

            if string.upper(current_item) == "GEM":
                item = goods_lib.GetOneGem()
                type_str = "gem"
            elif string.upper(current_item) == "ART":
                item = goods_lib.GetOneArt()
                type_str = "art"
            elif string.upper(current_item) == "MUNDANE ITEM":
                item = mundane_lib.GetOneMundane()
                type_str = "mundane"
            elif string.upper(current_item) == "COMMON MELEE":
                item = weapon_lib.GetOneCommonMeleeWep(masterwork=False)
                if string.upper(current_quality) == "MASTERWORK":
                    item = weapon_lib.GetOneCommonMeleeWep(masterwork=True)
                type_str = "weapon"
            elif string.upper(current_item) == "COMMON RANGED":
                item = weapon_lib.GetOneCommonRangedWep(masterwork=False)
                if string.upper(current_quality) == "MASTERWORK":
                    item = weapon_lib.GetOneCommonRangedWep(masterwork=True)
                type_str = "weapon"
            elif string.upper(current_item) == "UNCOMMON WEAPON":
                item = weapon_lib.GetOneUncommonWep(masterwork=False)
                if string.upper(current_quality) == "MASTERWORK":
                    item = weapon_lib.GetOneUncommonWep(masterwork=True)
                type_str = "weapon"
            elif string.upper(current_item) == "COMMON ARMOR":
                item = armor_lib.GetArmorType(masterwork=False)
                if string.upper(current_quality) == "MASTERWORK":
                    item = armor_lib.GetArmorType(masterwork=True)
                type_str = "armor"
            elif string.upper(current_item) == "COMMON SHIELD":
                item = armor_lib.GetShieldType(masterwork=False)
                if string.upper(current_quality) == "MASTERWORK":
                    item = armor_lib.GetShieldType(masterwork=True)
                type_str = "shield"
            elif string.upper(current_item) == "MAGIC ARMOR/SHIELD":
                item = armor_lib.GetOneMagicArmorShield(current_quality)
                type_str = string.lower(current_quality)
            elif string.upper(current_item) == "MAGIC WEAPON":
                item = weapon_lib.GetOneMagicWeapon(current_quality)
                type_str = string.lower(current_quality)
            elif string.upper(current_item) == "POTION/OIL":
                item = potion_lib.GetOnePotionOil(current_quality)
                type_str = string.lower(current_quality)
            elif string.upper(current_item) == "RING":
                item = ring_lib.GetOneRing(current_quality)
                type_str = string.lower(current_quality)
            elif string.upper(current_item) == "ROD":
                item = rod_lib.GetOneRod(current_quality)
                type_str = string.lower(current_quality)
            elif string.upper(current_item) == "ARCANE SCROLL":
                item = scroll_lib.GetOneScroll(current_quality, "arcane")
                type_str = string.lower(current_quality)
            elif string.upper(current_item) == "DIVINE SCROLL":
                item = scroll_lib.GetOneScroll(current_quality, "divine")
                type_str = string.lower(current_quality)
            elif string.upper(current_item) == "STAFF":
                item = staff_lib.GetOneStaff(current_quality)
                type_str = string.lower(current_quality)
            elif string.upper(current_item) == "WAND":
                item = wand_lib.GetOneWand(current_quality)
                type_str = string.lower(current_quality)
            elif string.upper(current_item) == "WONDROUS ITEM":
                item = wondrous_lib.GetOneWondrous(current_quality)
                type_str = string.lower(current_quality)

            lst_text.append("\n%s (%sg)" %
            (item["name"], item["value"]))

            number += 1
            worth += item["value"]
            if (self.rdo_spec_item_count.GetValue()
            and number >= int(self.txt_spec_item_count.GetValue())):
                break

            elif (self.rdo_spec_item_worth.GetValue()
            and worth >= int(self.txt_spec_item_worth.GetValue())):
                break

        nl_idx = 0
        if self.txt_affect.GetValue() == "":
            nl_idx = 1

        text = "".join(sorted(lst_text))

        self.txt_affect.DoAppendText(
        "%s\n\nItem Count: %d"
        "\nTotal Worth: %dgp\n" %
        (text[nl_idx:], number, worth)
        )

        


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
