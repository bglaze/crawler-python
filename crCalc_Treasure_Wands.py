#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Treasure Generators for Crawler I
#  by Brock Glaze
#
#  crCalc_Treasure_Wands.py


import crawler
import crDice
import string
import wx


#-----------------------------------------------------------------------
#------ Generate Wands (Table 7-26, Page 246) --------------------------
#-----------------------------------------------------------------------


def GetOneWand(m_type, fully_charged=False):

    dct_wand = {}

    minor = False
    medium = False
    major = False

    if string.upper(m_type) == "MINOR": minor = True
    elif string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True

    percentage_roll = crDice.RollPercentage()[1]

    if percentage_roll <= 2 and minor:
        name = "detect magic"
        value = 375
    elif percentage_roll <= 4 and minor:
        name = "light"
        value = 375
    elif percentage_roll <= 7 and minor:
        name = "burning hands"
        value = 750
    elif percentage_roll <= 10 and minor:
        name = "charm animal"
        value = 750
    elif percentage_roll <= 13 and minor:
        name = "charm person"
        value = 750
    elif percentage_roll <= 16 and minor:
        name = "color spray"
        value = 750
    elif percentage_roll <= 19 and minor:
        name = "cure light wounds"
        value = 750
    elif percentage_roll <= 22 and minor:
        name = "detect secret doors"
        value = 750
    elif percentage_roll <= 25 and minor:
        name = "enlarge person"
        value = 750
    elif percentage_roll <= 28 and minor:
        name = "magic missile (1st)"
        value = 750
    elif percentage_roll <= 31 and minor:
        name = "shocking grasp"
        value = 750
    elif percentage_roll <= 34 and minor:
        name = "summon monster I"
        value = 750
    elif percentage_roll <= 36 and minor:
        name = "magic missile (3rd)"
        value = 2250
    elif (percentage_roll <= 37 and minor
    or percentage_roll <= 3 and medium):
        name = "magic missile (5th)"
        value = 3750
    elif (percentage_roll <= 40 and minor
    or percentage_roll <= 7 and medium):
        name = "bear's endurance"
        value = 4500
    elif (percentage_roll <= 43 and minor
    or percentage_roll <= 11 and medium):
        name = "bull's strength"
        value = 4500
    elif (percentage_roll <= 46 and minor
    or percentage_roll <= 15 and medium):
        name = "cat's grace"
        value = 4500
    elif (percentage_roll <= 49 and minor
    or percentage_roll <= 20 and medium):
        name = "cure moderate wounds"
        value = 4500
    elif (percentage_roll <= 51 and minor
    or percentage_roll <= 22 and medium):
        name = "darkness"
        value = 4500
    elif (percentage_roll <= 54 and minor
    or percentage_roll <= 24 and medium):
        name = "daylight"
        value = 4500
    elif (percentage_roll <= 57 and minor
    or percentage_roll <= 27 and medium):
        name = "delay poison"
        value = 4500
    elif (percentage_roll <= 60 and minor
    or percentage_roll <= 31 and medium):
        name = "eagle's splendor"
        value = 4500
    elif (percentage_roll <= 63 and minor
    or percentage_roll <= 33 and medium):
        name = "false life"
        value = 4500
    elif (percentage_roll <= 66 and minor
    or percentage_roll <= 37 and medium):
        name = "fox's cunning"
        value = 4500
    elif (percentage_roll <= 68 and minor
    or percentage_roll <= 38 and medium):
        name = "ghoul touch"
        value = 4500
    elif (percentage_roll <= 71 and minor
    or percentage_roll <= 39 and medium):
        name = "hold person"
        value = 4500
    elif (percentage_roll <= 74 and minor
    or percentage_roll <= 42 and medium):
        name = "invisibility"
        value = 4500
    elif (percentage_roll <= 77 and minor
    or percentage_roll <= 44 and medium):
        name = "knock"
        value = 4500
    elif (percentage_roll <= 80 and minor
    or percentage_roll <= 45 and medium):
        name = "levitate"
        value = 4500
    elif (percentage_roll <= 83 and minor
    or percentage_roll <= 47 and medium):
        name = "melf's acid arrow"
        value = 4500
    elif (percentage_roll <= 86 and minor
    or percentage_roll <= 49 and medium):
        name = "mirror image"
        value = 4500
    elif (percentage_roll <= 89 and minor
    or percentage_roll <= 53 and medium):
        name = "owl's wisdom"
        value = 4500
    elif (percentage_roll <= 91 and minor
    or percentage_roll <= 54 and medium):
        name = "shatter"
        value = 4500
    elif (percentage_roll <= 94 and minor
    or percentage_roll <= 56 and medium):
        name = "silence"
        value = 4500
    elif (percentage_roll <= 97 and minor
    or percentage_roll <= 57 and medium):
        name = "summon monster II"
        value = 4500
    elif (percentage_roll <= 100 and minor
    or percentage_roll <= 59 and medium):
        name = "web"
        value = 4500
    elif (percentage_roll <= 62 and medium
    or percentage_roll <= 2 and major):
        name = "magic missile (7th)"
        value = 5250
    elif (percentage_roll <= 64 and medium
    or percentage_roll <= 5 and major):
        name = "magic missile (9th)"
        value = 6750
    elif (percentage_roll <= 67 and medium
    or percentage_roll <= 7 and major):
        name = "call lightning (5th)"
        value = 11250
    elif (percentage_roll <= 68 and medium
    or percentage_roll <= 8 and major):
        name = "charm person, heightened (3rd-level spell)"
        value = 11250
    elif (percentage_roll <= 70 and medium
    or percentage_roll <= 10 and major):
        name = "contagion"
        value = 11250
    elif (percentage_roll <= 74 and medium
    or percentage_roll <= 13 and major):
        name = "cure serious wounds"
        value = 11250
    elif (percentage_roll <= 77 and medium
    or percentage_roll <= 15 and major):
        name = "dispel magic"
        value = 11250
    elif (percentage_roll <= 81 and medium
    or percentage_roll <= 17 and major):
        name = "fireball (5th)"
        value = 11250
    elif (percentage_roll <= 83 and medium
    or percentage_roll <= 19 and major):
        name = "keen edge"
        value = 11250
    elif (percentage_roll <= 87 and medium
    or percentage_roll <= 21 and major):
        name = "lightning bolt (5th)"
        value = 11250
    elif (percentage_roll <= 89 and medium
    or percentage_roll <= 23 and major):
        name = "major image"
        value = 11250
    elif (percentage_roll <= 91 and medium
    or percentage_roll <= 25 and major):
        name = "slow"
        value = 11250
    elif (percentage_roll <= 94 and medium
    or percentage_roll <= 27 and major):
        name = "suggestion"
        value = 11250
    elif (percentage_roll <= 97 and medium
    or percentage_roll <= 29 and major):
        name = "summon monster III"
        value = 11250
    elif (percentage_roll <= 98 and medium
    or percentage_roll <= 31 and major):
        name = "fireball (6th)"
        value = 13500
    elif (percentage_roll <= 99 and medium
    or percentage_roll <= 33 and major):
        name = "lightning bolt (6th)"
        value = 13500
    elif (percentage_roll <= 100 and medium
    or percentage_roll <= 35 and major):
        name = "searing light (6th)"
        value = 13500
    elif percentage_roll <= 37 and major:
        name = "call lightning (8th)"
        value = 18000
    elif percentage_roll <= 39 and major:
        name = "fireball (8th)"
        value = 18000
    elif percentage_roll <= 41 and major:
        name = "lightning bolt (8th)"
        value = 18000
    elif percentage_roll <= 45 and major:
        name = "charm monster"
        value = 21000
    elif percentage_roll <= 50 and major:
        name = "cure critical wounds"
        value = 21000
    elif percentage_roll <= 52 and major:
        name = "dimensional anchor"
        value = 21000
    elif percentage_roll <= 55 and major:
        name = "fear"
        value = 21000
    elif percentage_roll <= 59 and major:
        name = "greater invisibility"
        value = 21000
    elif percentage_roll <= 60 and major:
        name = "hold person, heightened (4th level)"
        value = 21000
    elif percentage_roll <= 65 and major:
        name = "ice storm"
        value = 21000
    elif percentage_roll <= 68 and major:
        name = "inflict critical wounds"
        value = 21000
    elif percentage_roll <= 72 and major:
        name = "neutralize poison"
        value = 21000
    elif percentage_roll <= 74 and major:
        name = "poison"
        value = 21000
    elif percentage_roll <= 77 and major:
        name = "polymorph"
        value = 21000
    elif percentage_roll <= 78 and major:
        name = "ray of enfeeblement, heightened (4th level)"
        value = 21000
    elif percentage_roll <= 79 and major:
        name = "suggestion, heightened (4th level)"
        value = 21000
    elif percentage_roll <= 82 and major:
        name = "summon monster IV"
        value = 21000
    elif percentage_roll <= 86 and major:
        name = "wall of fire"
        value = 21000
    elif percentage_roll <= 90 and major:
        name = "wall of ice"
        value = 21000
    elif percentage_roll <= 91 and major:
        name = "dispel magic (10th)"
        value = 22500
    elif percentage_roll <= 92 and major:
        name = "fireball (10th)"
        value = 22500
    elif percentage_roll <= 93 and major:
        name = "lightning bolt (10th)"
        value = 22500
    elif percentage_roll <= 94 and major:
        name = "chaos hammer (8th)"
        value = 24000
    elif percentage_roll <= 95 and major:
        name = "holy smite (8th)"
        value = 24000
    elif percentage_roll <= 96 and major:
        name = "order's wrath (8th)"
        value = 24000
    elif percentage_roll <= 97 and major:
        name = "unholy blight (8th)"
        value = 24000
    elif percentage_roll <= 99 and major:
        name = "restoration"
        value = 26000
    elif percentage_roll <= 100 and major:
        name = "stoneskin"
        value = 33500

    if not fully_charged:
        percentage_roll_2 = crDice.RollPercentage()[1]

        if percentage_roll_2 <= 25:
            max_charges = 12
        elif percentage_roll_2 <= 50:
            max_charges = 25
        elif percentage_roll_2 <= 75:
            max_charges = 37
        elif percentage_roll_2 <= 100:
            max_charges = 50

        charges = crDice.RollDice(1, max_charges)[1]

    else:
        charges = 50

    name += " (%d charge" % charges
    if charges > 1:
        name += "s)"
    else:
        name += ")"

    value = (value / 50) * charges

    dct_wand["name"] = "wand of %s" % name
    dct_wand["value"] = value
    dct_wand["charges"] = charges

    return dct_wand


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
    #~ lst_perc = []
    #~ times = 1000
#~ 
    #~ for x in xrange(times):
        #~ count = 0
        #~ for x in xrange(100):
            #~ item = GetOneWand("Minor")
            #~ if item["charges"] >= 2:
                #~ count += 1
        #~ lst_perc.append(count)
#~ 
    #~ total = float(sum(lst_perc))
    #~ avg = total / times
    #~ print avg
