#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Treasure Generators for Crawler I
#  by Brock Glaze
#
#  crCalc_Treasure_Rings.py


import crawler
import crDice
import string
import wx


#-----------------------------------------------------------------------
#------ Generate Rings (Table 7-18, Page 231) --------------------------
#-----------------------------------------------------------------------

def GetOneRing(m_type):

    dct_ring = {}

    minor = False
    medium = False
    major = False

    if string.upper(m_type) == "MINOR": minor = True
    elif string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True

    percentage_roll = crDice.RollPercentage()[1]

    if percentage_roll <= 18 and minor:
        name = "protection +1"
        value = 2000
    elif percentage_roll <= 28 and minor:
        name = "feather falling"
        value = 2200
    elif percentage_roll <= 36 and minor:
        name = "sustenance"
        value = 2500
    elif percentage_roll <= 44 and minor:
        name = "climbing"
        value = 2500
    elif percentage_roll <= 52 and minor:
        name = "jumping"
        value = 2500
    elif percentage_roll <= 60 and minor:
        name = "swimming"
        value = 2500
    elif (percentage_roll <= 70 and minor
    or percentage_roll <= 5 and medium):
        name = "counterspells"
        value = 4000
    elif (percentage_roll <= 75 and minor
    or percentage_roll <= 8 and medium):
        name = "mind shielding"
        value = 8000
    elif (percentage_roll <= 80 and minor
    or percentage_roll <= 18 and medium):
        name = "protection +2"
        value = 8000
    elif (percentage_roll <= 85 and minor
    or percentage_roll <= 23 and medium):
        name = "force shield"
        value = 8500
    elif (percentage_roll <= 90 and minor
    or percentage_roll <= 28 and medium):
        name = "ram"
        value = 8600
    elif percentage_roll <= 34 and medium:
        name = "climbing, improved"
        value = 10000
    elif percentage_roll <= 40 and medium:
        name = "jumping, improved"
        value = 10000
    elif percentage_roll <= 46 and medium:
        name = "swimming, improved"
        value = 10000
    elif (percentage_roll <= 93 and minor
    or percentage_roll <= 51 and medium):
        name = "animal friendship"
        value = 10800
    elif (percentage_roll <= 96 and minor
    or percentage_roll <= 56 and medium
    or percentage_roll <= 2 and major):

        percentage_roll_2 = crDice.RollPercentage()[1]

        if percentage_roll_2 <= 20:
            name = "energy resistance (acid), minor"
        elif percentage_roll_2 <= 40:
            name = "energy resistance (cold), minor"
        elif percentage_roll_2 <= 60:
            name = "energy resistance (electricity), minor"
        elif percentage_roll_2 <= 80:
            name = "energy resistance (fire), minor"
        elif percentage_roll_2 <= 100:
            name = "energy resistance (sonic), minor"

        value = 12000

    elif (percentage_roll <= 98 and minor
    or percentage_roll <= 61 and medium):
        name = "chameleon power"
        value = 12700
    elif (percentage_roll <= 100 and minor
    or percentage_roll <= 66 and medium):
        name = "water walking"
        value = 15000
    elif (percentage_roll <= 71 and medium
    or percentage_roll <= 7 and major):
        name = "protection +3"
        value = 18000
    elif (percentage_roll <= 76 and medium
    or percentage_roll <= 10 and major):
        name = "spell storing, minor"
        value = 18000
    elif (percentage_roll <= 81 and medium
    or percentage_roll <= 15 and major):
        name = "invisibility"
        value = 20000
    elif (percentage_roll <= 85 and medium
    or percentage_roll <= 19 and major):
        name = "wizardry (I)"
        value = 20000
    elif (percentage_roll <= 90 and medium
    or percentage_roll <= 25 and major):
        name = "evasion"
        value = 25000
    elif (percentage_roll <= 93 and medium
    or percentage_roll <= 28 and major):
        name = "x-ray vision"
        value = 25000
    elif (percentage_roll <= 97 and medium
    or percentage_roll <= 32 and major):
        name = "blinking"
        value = 27000
    elif (percentage_roll <= 100 and medium
    or percentage_roll <= 39 and major):

        percentage_roll_2 = crDice.RollPercentage()[1]

        if percentage_roll_2 <= 20:
            name = "energy resistance (acid), major"
        elif percentage_roll_2 <= 40:
            name = "energy resistance (cold), major"
        elif percentage_roll_2 <= 60:
            name = "energy resistance (electricity), major"
        elif percentage_roll_2 <= 80:
            name = "energy resistance (fire), major"
        elif percentage_roll_2 <= 100:
            name = "energy resistance (sonic), major"

        value = 28000

    elif percentage_roll <= 49 and major:
        name = "protection +4"
        value = 32000
    elif percentage_roll <= 55 and major:
        name = "wizardry (II)"
        value = 40000
    elif percentage_roll <= 60 and major:
        name = "freedom of movement"
        value = 40000
    elif percentage_roll <= 63 and major:

        percentage_roll_2 = crDice.RollPercentage()[1]

        if percentage_roll_2 <= 20:
            name = "energy resistance (acid), greater"
        elif percentage_roll_2 <= 40:
            name = "energy resistance (cold), greater"
        elif percentage_roll_2 <= 60:
            name = "energy resistance (electricity), greater"
        elif percentage_roll_2 <= 80:
            name = "energy resistance (fire), greater"
        elif percentage_roll_2 <= 100:
            name = "energy resistance (sonic), greater"

        value = 44000

    elif percentage_roll <= 65 and major:
        name = "friend shield (pair)"
        value = 50000
    elif percentage_roll <= 70 and major:
        name = "protection +5"
        value = 50000
    elif percentage_roll <= 74 and major:
        name = "shooting stars"
        value = 50000
    elif percentage_roll <= 79 and major:
        name = "spell storing"
        value = 50000
    elif percentage_roll <= 83 and major:
        name = "wizardry (III)"
        value = 70000
    elif percentage_roll <= 86 and major:
        name = "telekinesis"
        value = 75000
    elif percentage_roll <= 88 and major:
        name = "regeneration"
        value = 90000
    elif percentage_roll <= 89 and major:
        name = "three wishes"
        value = 97950
    elif percentage_roll <= 92 and major:
        name = "spell turning"
        value = 98280
    elif percentage_roll <= 94 and major:
        name = "wizardry (IV)"
        value = 100000
    elif percentage_roll <= 95 and major:
        name = "djinni calling"
        value = 125000
    elif percentage_roll <= 96 and major:
        name = "elemental command (air)"
        value = 200000
    elif percentage_roll <= 97 and major:
        name = "elemental command (earth)"
        value = 200000
    elif percentage_roll <= 98 and major:
        name = "elemental command (fire)"
        value = 200000
    elif percentage_roll <= 99 and major:
        name = "elemental command (water)"
        value = 200000
    elif percentage_roll <= 100 and major:
        name = "spell storing, major"
        value = 200000

    dct_ring["name"] = "ring of %s" % name
    dct_ring["value"] = value

    return dct_ring


#***********************************************************************


if __name__ == "__main__":
    #~ crawler.Main()
    for x in xrange(10000):
        item = GetOneRing("Major")
        print "%s - %s" % (item["name"], item["value"])
