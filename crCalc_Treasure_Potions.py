#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Treasure Generators for Crawler I
#  by Brock Glaze
#
#  crCalc_Treasure_Potions.py


import crawler
import crDice
import string
import wx


#-----------------------------------------------------------------------
#------ Generate Potions / Oils (Table 7-17, Page 230) -----------------
#-----------------------------------------------------------------------

def GetOnePotionOil(m_type):

    dct_potion = {}

    minor = False
    medium = False
    major = False

    if string.upper(m_type) == "MINOR": minor = True
    elif string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True

    percentage_roll = crDice.RollPercentage()[1]

    if percentage_roll <= 10 and minor:
        name = "cure light wounds (potion)"
        value = 50
    elif percentage_roll <= 13 and minor:
        name = "endure elements (potion)"
        value = 50
    elif percentage_roll <= 15 and minor:
        name = "hide from animals (potion)"
        value = 50
    elif percentage_roll <= 17 and minor:
        name = "hide from undead (potion)"
        value = 50
    elif percentage_roll <= 19 and minor:
        name = "jump (potion)"
        value = 50
    elif percentage_roll <= 22 and minor:
        name = "mage armor (potion)"
        value = 50
    elif percentage_roll <= 25 and minor:
        name = "magic fang (potion)"
        value = 50
    elif percentage_roll <= 26 and minor:
        name = "magic stone (oil)"
        value = 50
    elif percentage_roll <= 29 and minor:
        name = "magic weapon (oil)"
        value = 50
    elif percentage_roll <= 30 and minor:
        name = "pass without trace (potion)"
        value = 50
    elif percentage_roll <= 32 and minor:

        percentage_roll_2 = crDice.RollPercentage()[1]

        if percentage_roll_2 <= 25:
            name = "protection from (chaos) (potion)"
        elif percentage_roll_2 <= 50:
            name = "protection from (evil) (potion)"
        elif percentage_roll_2 <= 75:
            name = "protection from (good) (potion)"
        elif percentage_roll_2 <= 100:
            name = "protection from (law) (potion)"

        value = 50

    elif percentage_roll <= 34 and minor:
        name = "remove fear (potion)"
        value = 50
    elif percentage_roll <= 35 and minor:
        name = "sanctuary (potion)"
        value = 50
    elif percentage_roll <= 38 and minor:
        name = "shield of faith +2 (potion)"
        value = 50
    elif percentage_roll <= 39 and minor:
        name = "shillelagh (oil)"
        value = 50
    elif (percentage_roll <= 41 and minor
    or percentage_roll <= 2 and medium):
        name = "bless weapon (oil)"
        value = 100
    elif (percentage_roll <= 44 and minor
    or percentage_roll <= 4 and medium):
        name = "enlarge person (potion)"
        value = 250
    elif (percentage_roll <= 45 and minor
    or percentage_roll <= 5 and medium):
        name = "reduce person (potion)"
        value = 250
    elif (percentage_roll <= 47 and minor
    or percentage_roll <= 6 and medium):
        name = "aid (potion)"
        value = 300
    elif (percentage_roll <= 50 and minor
    or percentage_roll <= 7 and medium):
        name = "barkskin +2 (potion)"
        value = 300
    elif (percentage_roll <= 53 and minor
    or percentage_roll <= 10 and medium):
        name = "bear's endurance (potion)"
        value = 300
    elif (percentage_roll <= 56 and minor
    or percentage_roll <= 13 and medium
    or percentage_roll <= 2 and major):
        name = "blur (potion)"
        value = 300
    elif (percentage_roll <= 59 and minor
    or percentage_roll <= 16 and medium):
        name = "bull's strength (potion)"
        value = 300
    elif (percentage_roll <= 62 and minor
    or percentage_roll <= 19 and medium):
        name = "cat's grace (potion)"
        value = 300
    elif (percentage_roll <= 67 and minor
    or percentage_roll <= 27 and medium
    or percentage_roll <= 7 and major):
        name = "cure moderate wounds (potion)"
        value = 300
    elif (percentage_roll <= 68 and minor
    or percentage_roll <= 28 and medium):
        name = "darkness (oil)"
        value = 300
    elif (percentage_roll <= 71 and minor
    or percentage_roll <= 30 and medium
    or percentage_roll <= 9 and major):
        name = "darkvision (potion)"
        value = 300
    elif (percentage_roll <= 74 and minor
    or percentage_roll <= 31 and medium):
        name = "delay poison (potion)"
        value = 300
    elif (percentage_roll <= 76 and minor
    or percentage_roll <= 33 and medium):
        name = "eagle's splendor (potion)"
        value = 300
    elif (percentage_roll <= 78 and minor
    or percentage_roll <= 35 and medium):
        name = "fox's cunning (potion)"
        value = 300
    elif (percentage_roll <= 81 and minor
    or percentage_roll <= 37 and medium
    or percentage_roll <= 11 and major):
        name = "invisibility (potion or oil)"
        value = 300
    elif (percentage_roll <= 84 and minor
    or percentage_roll <= 38 and medium
    or percentage_roll <= 12 and major):
        name = "lesser restoration (potion)"
        value = 300
    elif (percentage_roll <= 86 and minor
    or percentage_roll <= 39 and medium):
        name = "levitate (potion or oil)"
        value = 300
    elif (percentage_roll <= 87 and minor
    or percentage_roll <= 40 and medium):
        name = "misdirection (potion)"
        value = 300
    elif (percentage_roll <= 89 and minor
    or percentage_roll <= 42 and medium):
        name = "owl's wisdom (potion)"
        value = 300
    elif (percentage_roll <= 91 and minor
    or percentage_roll <= 43 and medium):
        name = "protection from arrows 10/magic (potion)"
        value = 300
    elif (percentage_roll <= 93 and minor
    or percentage_roll <= 44 and medium
    or percentage_roll <= 13 and major):
        name = "remove paralysis (potion)"
        value = 300
    elif (percentage_roll <= 96 and minor
    or percentage_roll <= 46 and medium):

        percentage_roll_2 = crDice.RollPercentage()[1]

        if percentage_roll_2 <= 20:
            name = "resist energy (acid) 10 (potion)"
        elif percentage_roll_2 <= 40:
            name = "resist energy (cold) 10 (potion)"
        elif percentage_roll_2 <= 60:
            name = "resist energy (electricity) 10 (potion)"
        elif percentage_roll_2 <= 80:
            name = "resist energy (fire) 10 (potion)"
        elif percentage_roll_2 <= 100:
            name = "resist energy (sonic) 10 (potion)"

        value = 300

    elif (percentage_roll <= 97 and minor
    or percentage_roll <= 48 and medium
    or percentage_roll <= 14 and major):
        name = "shield of faith +3 (potion)"
        value = 300
    elif (percentage_roll <= 99 and minor
    or percentage_roll <= 49 and medium):
        name = "spider climb (potion)"
        value = 300
    elif (percentage_roll <= 100 and minor
    or percentage_roll <= 50 and medium
    or percentage_roll <= 15 and major):
        name = "undetectable alignment (potion)"
        value = 300
    elif (percentage_roll <= 51 and medium
    or percentage_roll <= 16 and major):
        name = "barkskin +3 (potion)"
        value = 600
    elif (percentage_roll <= 52 and medium
    or percentage_roll <= 18 and major):
        name = "shield of faith +4 (potion)"
        value = 600
    elif (percentage_roll <= 55 and medium
    or percentage_roll <= 20 and major):

        percentage_roll_2 = crDice.RollPercentage()[1]

        if percentage_roll_2 <= 20:
            name = "resist energy (acid) 20 (potion)"
        elif percentage_roll_2 <= 40:
            name = "resist energy (cold) 20 (potion)"
        elif percentage_roll_2 <= 60:
            name = "resist energy (electricity) 20 (potion)"
        elif percentage_roll_2 <= 80:
            name = "resist energy (fire) 20 (potion)"
        elif percentage_roll_2 <= 100:
            name = "resist energy (sonic) 20 (potion)"

        value = 700

    elif (percentage_roll <= 60 and medium
    or percentage_roll <= 28 and major):
        name = "cure serious wounds (potion)"
        value = 750
    elif (percentage_roll <= 61 and medium
    or percentage_roll <= 29 and major):
        name = "daylight (oil)"
        value = 750
    elif (percentage_roll <= 64 and medium
    or percentage_roll <= 32 and major):
        name = "displacement (potion)"
        value = 750
    elif (percentage_roll <= 65 and medium
    or percentage_roll <= 33 and major):
        name = "flame arrow (oil)"
        value = 750
    elif (percentage_roll <= 68 and medium
    or percentage_roll <= 38 and major):
        name = "fly (potion)"
        value = 750
    elif (percentage_roll <= 69 and medium
    or percentage_roll <= 39 and major):
        name = "gaseous form (potion)"
        value = 750
    elif percentage_roll <= 71 and medium:
        name = "greater magic fang +1 (potion)"
        value = 750
    elif percentage_roll <= 73 and medium:
        name = "greater magic weapon +1 (oil)"
        value = 750
    elif (percentage_roll <= 75 and medium
    or percentage_roll <= 41 and major):
        name = "haste (potion)"
        value = 750
    elif (percentage_roll <= 78 and medium
    or percentage_roll <= 44 and major):
        name = "heroism (potion)"
        value = 750
    elif (percentage_roll <= 80 and medium
    or percentage_roll <= 46 and major):
        name = "keen edge (oil)"
        value = 750
    elif (percentage_roll <= 81 and medium
    or percentage_roll <= 47 and major):

        percentage_roll_2 = crDice.RollPercentage()[1]

        if percentage_roll_2 <= 25:
            name = "magic circle against (chaos) (potion)"
        elif percentage_roll_2 <= 50:
            name = "magic circle against (evil) (potion)"
        elif percentage_roll_2 <= 75:
            name = "magic circle against (good) (potion)"
        elif percentage_roll_2 <= 100:
            name = "magic circle against (law) (potion)"

        value = 750

    elif percentage_roll <= 83 and medium:
        name = "magic vestment +1 (oil)"
        value = 750
    elif (percentage_roll <= 86 and medium
    or percentage_roll <= 50 and major):
        name = "neutralize poison (potion)"
        value = 750
    elif (percentage_roll <= 88 and medium
    or percentage_roll <= 52 and major):
        name = "nondetection (potion)"
        value = 750
    elif (percentage_roll <= 91 and medium
    or percentage_roll <= 54 and major):

        percentage_roll_2 = crDice.RollPercentage()[1]

        if percentage_roll_2 <= 20:
            name = "protection from energy (acid) (potion)"
        elif percentage_roll_2 <= 40:
            name = "protection from energy (cold) (potion)"
        elif percentage_roll_2 <= 60:
            name = "protection from energy (electricity) (potion)"
        elif percentage_roll_2 <= 80:
            name = "protection from energy (fire) (potion)"
        elif percentage_roll_2 <= 100:
            name = "protection from energy (sonic) (potion)"

        value = 750

    elif (percentage_roll <= 93 and medium
    or percentage_roll <= 55 and major):
        name = "rage (potion)"
        value = 750
    elif (percentage_roll <= 94 and medium
    or percentage_roll <= 56 and major):
        name = "remove blindness/deafness (potion)"
        value = 750
    elif (percentage_roll <= 95 and medium
    or percentage_roll <= 57 and major):
        name = "remove curse (potion)"
        value = 750
    elif (percentage_roll <= 96 and medium
    or percentage_roll <= 58 and major):
        name = "remove disease (potion)"
        value = 750
    elif (percentage_roll <= 97 and medium
    or percentage_roll <= 59 and major):
        name = "tongues (potion)"
        value = 750
    elif (percentage_roll <= 99 and medium
    or percentage_roll <= 60 and major):
        name = "water breathing (potion)"
        value = 750
    elif (percentage_roll <= 100 and medium
    or percentage_roll <= 61 and major):
        name = "water walk (potion)"
        value = 750
    elif percentage_roll <= 63 and major:
        name = "barkskin +4 (potion)"
        value = 900
    elif percentage_roll <= 64 and major:
        name = "shield of faith +5 (potion)"
        value = 900
    elif percentage_roll <= 65 and major:
        name = "good hope (potion)"
        value = 1050
    elif percentage_roll <= 68 and major:

        percentage_roll_2 = crDice.RollPercentage()[1]

        if percentage_roll_2 <= 20:
            name = "resist energy (acid) 30 (potion)"
        elif percentage_roll_2 <= 40:
            name = "resist energy (cold) 30 (potion)"
        elif percentage_roll_2 <= 60:
            name = "resist energy (electricity) 30 (potion)"
        elif percentage_roll_2 <= 80:
            name = "resist energy (fire) 30 (potion)"
        elif percentage_roll_2 <= 100:
            name = "resist energy (sonic) 30 (potion)"

        value = 1100

    elif percentage_roll <= 69 and major:
        name = "barkskin +5 (potion)"
        value = 1200
    elif percentage_roll <= 73 and major:
        name = "greater magic fang +2 (potion)"
        value = 1200
    elif percentage_roll <= 77 and major:
        name = "greater magic weapon +2 (oil)"
        value = 1200
    elif percentage_roll <= 81 and major:
        name = "magic vestment +2 (oil)"
        value = 1200
    elif percentage_roll <= 82 and major:
        name = "protection from arrows 15/magic (potion)"
        value = 1500
    elif percentage_roll <= 85 and major:
        name = "greater magic fang +3 (potion)"
        value = 1800
    elif percentage_roll <= 88 and major:
        name = "greater magic weapon +3 (oil)"
        value = 1800
    elif percentage_roll <= 91 and major:
        name = "magic vestment +3 (oil)"
        value = 1800
    elif percentage_roll <= 93 and major:
        name = "greater magic fang +4 (potion)"
        value = 2400
    elif percentage_roll <= 95 and major:
        name = "greater magic weapon +4 (oil)"
        value = 2400
    elif percentage_roll <= 97 and major:
        name = "magic vestment +4 (oil)"
        value = 2400
    elif percentage_roll <= 98 and major:
        name = "greater magic fang +5 (potion)"
        value = 3000
    elif percentage_roll <= 99 and major:
        name = "greater magic weapon +5 (oil)"
        value = 3000
    elif percentage_roll <= 100 and major:
        name = "magic vestment +5 (oil)"
        value = 3000

    dct_potion["name"] = name
    dct_potion["value"] = value

    return dct_potion


#***********************************************************************


if __name__ == "__main__":
    #~ crawler.Main()
    for x in xrange(100000):
        item = GetOnePotionOil("Major")
        print "%s - %s" % (item["name"], item["value"])
