#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Treasure Generators for Crawler I
#  by Brock Glaze
#
#  crCalc_Treasure_Rods.py


import crawler
import crDice
import string
import wx


#-----------------------------------------------------------------------
#------ Generate Rings (Table 7-18, Page 231) --------------------------
#-----------------------------------------------------------------------

def GetOneRod(m_type):

    dct_rod = {}

    medium = False
    major = False

    if string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True

    percentage_roll = crDice.RollPercentage()[1]

    if percentage_roll <= 7 and medium:
        name = "metamagic, enlarge, lesser"
        value = 3000
    elif percentage_roll <= 14 and medium:
        name = "metamagic, extend, lesser"
        value = 3000
    elif percentage_roll <= 21 and medium:
        name = "metamagic, silent, lesser"
        value = 3000
    elif percentage_roll <= 28 and medium:
        name = "immovable"
        value = 5000
    elif percentage_roll <= 35 and medium:
        name = "metamagic, empower, lesser"
        value = 9000
    elif percentage_roll <= 42 and medium:
        name = "metal and mineral detection"
        value = 10500
    elif (percentage_roll <= 53 and medium
    or percentage_roll <= 4 and major):
        name = "cancellation"
        value = 11000
    elif (percentage_roll <= 57 and medium
    or percentage_roll <= 6 and major):
        name = "metamagic, enlarge"
        value = 11000
    elif (percentage_roll <= 61 and medium
    or percentage_roll <= 8 and major):
        name = "metamagic, extend"
        value = 11000
    elif (percentage_roll <= 65 and medium
    or percentage_roll <= 10 and major):
        name = "metamagic, silent"
        value = 11000
    elif (percentage_roll <= 71 and medium
    or percentage_roll <= 14 and major):
        name = "wonder"
        value = 12000
    elif (percentage_roll <= 79 and medium
    or percentage_roll <= 18 and major):
        name = "the python"
        value = 13000
    elif percentage_roll <= 83 and medium:
        name = "metamagic, maximize, lesser"
        value = 14000
    elif (percentage_roll <= 89 and medium
    or percentage_roll <= 21 and major):
        name = "flame extinguishing"
        value = 15000
    elif (percentage_roll <= 97 and medium
    or percentage_roll <= 25 and major):
        name = "the viper"
        value = 19000
    elif percentage_roll <= 30 and major:
        name = "enemy detection"
        value = 23500
    elif percentage_roll <= 36 and major:
        name = "metamagic, enlarge, greater"
        value = 24500
    elif percentage_roll <= 42 and major:
        name = "metamagic, extend, greater"
        value = 24500
    elif percentage_roll <= 48 and major:
        name = "metamagic, silent, greater"
        value = 24500
    elif percentage_roll <= 53 and major:
        name = "splendor"
        value = 25000
    elif percentage_roll <= 58 and major:
        name = "withering"
        value = 25000
    elif (percentage_roll <= 99 and medium
    or percentage_roll <= 64 and major):
        name = "metamagic, empower"
        value = 32500
    elif percentage_roll <= 69 and major:
        name = "thunder and lightning"
        value = 33000
    elif (percentage_roll <= 100 and medium
    or percentage_roll <= 73 and major):
        name = "metamagic, quicken, lesser"
        value = 35000
    elif percentage_roll <= 77 and major:
        name = "negation"
        value = 37000
    elif percentage_roll <= 80 and major:
        name = "absorption"
        value = 50000
    elif percentage_roll <= 84 and major:
        name = "flailing"
        value = 50000
    elif percentage_roll <= 86 and major:
        name = "metamagic, maximize"
        value = 54000
    elif percentage_roll <= 88 and major:
        name = "rulership"
        value = 60000
    elif percentage_roll <= 90 and major:
        name = "security"
        value = 61000
    elif percentage_roll <= 92 and major:
        name = "lordly might"
        value = 70000
    elif percentage_roll <= 94 and major:
        name = "metamagic, empower, greater"
        value = 73000
    elif percentage_roll <= 96 and major:
        name = "metamagic, quicken"
        value = 75500
    elif percentage_roll <= 98 and major:
        name = "alertness"
        value = 85000
    elif percentage_roll <= 99 and major:
        name = "metamagic, maximize, greater"
        value = 121500
    elif percentage_roll <= 100 and major:
        name = "metamagic, quicken, greater"
        value = 170000

    dct_rod["name"] = "rod of %s" % name
    dct_rod["value"] = value

    return dct_rod


#***********************************************************************


if __name__ == "__main__":
    #~ crawler.Main()
    for x in xrange(10000):
        item = GetOneRod("Medium")
        print "%s - %s" % (item["name"], item["value"])
