#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Treasure Generators for Crawler I
#  by Brock Glaze
#
#  crCalc_Treasure.py


import crawler
import crDice
import crFormulas
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
import random
import string
import wx


#-----------------------------------------------------------------------
#------ Generate One Random Item ---------------------------------------
#-----------------------------------------------------------------------


def GetOneItem(m_type):

    mundane = False
    minor = False
    medium = False
    major = False

    if string.upper(m_type) == "MUNDANE": mundane = True
    elif string.upper(m_type) == "MINOR": minor = True
    elif string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True


    percentage_roll = crDice.RollPercentage()[1]

    if mundane:
        return mundane_lib.GetOneMundane()

    else:

        # Armor / Shields
        if (percentage_roll <= 4 and minor
        or percentage_roll <= 10 and medium
        or percentage_roll <= 10 and major):
            return armor_lib.GetOneMagicArmorShield(m_type)

        # Weapons
        elif (percentage_roll <= 9 and minor
        or percentage_roll <= 20 and medium
        or percentage_roll <= 20 and major):
            return weapon_lib.GetOneMagicWeapon(m_type)

        # Potions / Oils
        elif (percentage_roll <= 44 and minor
        or percentage_roll <= 30 and medium
        or percentage_roll <= 25 and major):
            return potion_lib.GetOnePotionOil(m_type)

        # Rings
        elif (percentage_roll <= 46 and minor
        or percentage_roll <= 40 and medium
        or percentage_roll <= 35 and major):
            return ring_lib.GetOneRing(m_type)

        # Rods
        elif (percentage_roll <= 50 and medium
        or percentage_roll <= 45 and major):
            return rod_lib.GetOneRod(m_type)

        # Scrolls
        elif (percentage_roll <= 81 and minor
        or percentage_roll <= 65 and medium
        or percentage_roll <= 55 and major):
            return scroll_lib.GetOneScroll(m_type)

        # Staffs
        elif (percentage_roll <= 68 and medium
        or percentage_roll <= 75 and major):
            return staff_lib.GetOneStaff(m_type)

        # Wands
        elif (percentage_roll <= 91 and minor
        or percentage_roll <= 83 and medium
        or percentage_roll <= 80 and major):
            return wand_lib.GetOneWand(m_type)

        # Wondrous
        elif (percentage_roll <= 100 and minor # 100
        or percentage_roll <= 100 and medium # 100
        or percentage_roll <= 100 and major): # 100
            return wondrous_lib.GetOneWondrous(m_type)


#-----------------------------------------------------------------------
#------ Calculate Gold Value -------------------------------------------
#-----------------------------------------------------------------------


lst_gold_values = [300, 600, 900, 1200, 1600, 2000, 2600, 3400,
                   4500, 5800, 7500, 9800, 13000, 17000, 22000,
                   28000, 36000, 47000, 61000, 80000, 87000, 96000,
                   106000, 116000, 128000, 141000, 155000, 170000,
                   187000, 206000, 227000, 249000, 274000, 302000,
                   332000, 365000, 401000, 442000, 486000, 534000]


def CalculateAvgTreasureValue(x):
    if (x > 40):
        x = 40 # Not perfect. But no idea what CRs above 40 should give.
    x2 = int(x)
    if (x < 1):
        # If level is a fraction, return that
        # fraction of the level 1 gold value
        i = x * lst_gold_values[0]

    # Formula currently not necessary
    #~ elif (x > x2):
        #~ i = lst_gold_values[x2-1] + (x-x2) * (
        #~ lst_gold_values[x2] - lst_gold_values[x2-1]
        #~ )

    else:
        i = lst_gold_values[x2-1]

    return i


# Calculate average treasure, convert and return readable string
def AvgTreasureValueTextulator(plrLst, monLst):
    cr = crFormulas.TotalLevel(monLst) # Original

    EL = int(crFormulas.FoeEffectiveLevel(monLst))

    if EL < 1:
        EL = "< 1"

    avg_treasure_value = int(
    crFormulas.RoundOnePlace(CalculateAvgTreasureValue(cr))
    )

    returnTxt = ("Average Treasure Value (EL %s): %sg" % (EL, avg_treasure_value))

    num_chars = crFormulas.CountChars(plrLst)
    if num_chars:
        # Append string with player specific info, if players exist
        avg_treasure_each = int(avg_treasure_value / num_chars)
        returnTxt += (
        "\nDivided by (%d players): %sg each" %
        (num_chars, avg_treasure_each)
        )

    return returnTxt


def GetAvgTreasureValue(monLst):
    cr = crFormulas.TotalLevel(monLst)

    avg_treasure_value = int(
    crFormulas.RoundOnePlace(CalculateAvgTreasureValue(cr))
    )

    return avg_treasure_value


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
