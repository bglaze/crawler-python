#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Treasure Generators for Crawler I
#  by Brock Glaze
#
#  crCalc_Treasure_Staffs.py


import crawler
import crDice
import string
import wx


#-----------------------------------------------------------------------
#------ Generate Staffs (Table 7-25, Page 243) --------------------------
#-----------------------------------------------------------------------


def GetOneStaff(m_type):

    dct_staff = {}

    medium = False
    major = False

    if string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True

    percentage_roll = crDice.RollPercentage()[1]

    if (percentage_roll <= 15 and medium
    or percentage_roll <= 3 and major):
        name = "charming"
        value = 16500
    elif (percentage_roll <= 30 and medium
    or percentage_roll <= 9 and major):
        name = "fire"
        value = 17750
    elif (percentage_roll <= 40 and medium
    or percentage_roll <= 11 and major):
        name = "swarming insects"
        value = 24750
    elif (percentage_roll <= 60 and medium
    or percentage_roll <= 17 and major):
        name = "healing"
        value = 27750
    elif (percentage_roll <= 75 and medium
    or percentage_roll <= 19 and major):
        name = "size alteration"
        value = 29000
    elif (percentage_roll <= 90 and medium
    or percentage_roll <= 24 and major):
        name = "illumination"
        value = 48250
    elif (percentage_roll <= 95 and medium
    or percentage_roll <= 31 and major):
        name = "frost"
        value = 56250
    elif (percentage_roll <= 100 and medium
    or percentage_roll <= 38 and major):
        name = "defense"
        value = 58250
    elif percentage_roll <= 43 and major:
        name = "abjuration"
        value = 65000
    elif percentage_roll <= 48 and major:
        name = "conjuration"
        value = 65000
    elif percentage_roll <= 53 and major:
        name = "enchantment"
        value = 65000
    elif percentage_roll <= 58 and major:
        name = "evocation"
        value = 65000
    elif percentage_roll <= 63 and major:
        name = "illusion"
        value = 65000
    elif percentage_roll <= 68 and major:
        name = "necromancy"
        value = 65000
    elif percentage_roll <= 73 and major:
        name = "transmutation"
        value = 65000
    elif percentage_roll <= 77 and major:
        name = "divination"
        value = 73500
    elif percentage_roll <= 82 and major:
        name = "earth and stone"
        value = 80500
    elif percentage_roll <= 87 and major:
        name = "woodlands"
        value = 101250
    elif percentage_roll <= 92 and major:
        name = "life"
        value = 155750
    elif percentage_roll <= 97 and major:
        name = "passage"
        value = 170500
    elif percentage_roll <= 100 and major:
        name = "power"
        value = 211000

    dct_staff["name"] = "staff of %s" % name
    dct_staff["value"] = value

    return dct_staff


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
