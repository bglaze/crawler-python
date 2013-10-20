#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Treasure Generators for Crawler I
#  by Brock Glaze
#
#  crCalc_Treasure_Wondrous.py


import crawler
import crDice
import string
import wx


#-----------------------------------------------------------------------
#------ Generate Minor Wondrous Item (Table 7-27, Page 247) ------------
#-----------------------------------------------------------------------


def GetOneMinorWondrous():
    dct_item = {}

    percentage_roll = crDice.RollPercentage()[1]

    item_tuple = (
    ("Quaal's feather token, anchor", 50),
    ("universal solvent", 50),
    ("elixir of love", 150),
    ("unguent of timelessness", 150),
    ("Quaal's feather token, fan", 200),
    ("dust of tracelessness", 250),
    ("elixir of hiding", 250),
    ("elixir of sneaking", 250),
    ("elixir of swimming", 250),
    ("elixir of vision", 250),
    ("silversheen", 250),
    ("Quaal's feather token, bird", 300),
    ("Quaal's feather token, tree", 400),
    ("Quaal's feather token, swan boat", 450),
    ("elixir of truth", 500),
    ("Quaal's feather token, whip", 500),
    ("dust of dryness", 850),
    ("bag of tricks, gray", 900),
    ("hand of the mage", 900),
    ("bracers of armor +1", 1000),
    ("cloak of resistance +1", 1000),
    ("pearl of power, 1st-level spell", 1000),
    ("phylactery of faithfulness", 1000),
    ("salve of slipperiness", 1000),
    ("elixir of fire breath", 1100),
    ("pipes of the sewers", 1150),
    ("dust of illusion", 1200),
    ("goggles of minute seeing", 1250),
    ("brooch of shielding", 1500),
    ("necklace of fireballs type I", 1650),
    ("dust of appearance", 1800),
    ("hat of disguise", 1800),
    ("pipes of sounding", 1800),
    ("quiver of Ehlonna", 1800),
    ("amulet of natural armor +1", 2000),
    ("Heward's handy haversack", 2000),
    ("horn of fog", 2000),
    ("elemental gem", 2250),
    ("robe of bones", 2400),
    ("sovereign glue", 2400),
    ("bag of holding type I", 2500),
    ("boots of elvenkind", 2500),
    ("boots of the winterlands", 2500),
    ("candle of truth", 2500),
    ("cloak of elvenkind", 2500),
    ("eyes of the eagle", 2500),
    ("scarab, golembane", 2500),
    ("necklace of fireballs type II", 2700),
    ("stone of alarm", 2700),
    ("bag of tricks, rust", 3000),
    ("bead of force", 3000),
    ("chime of opening", 3000),
    ("horseshoes of speed", 3000),
    ("rope of climbing", 3000),
    ("dust of disappearance", 3500),
    ("lens of detection", 3500),
    ("vestment, druid's", 3750),
    ("figurine of wondrous power, silver raven", 3800),
    ("amulet of health +2", 4000),
    ("bracers of armor +2", 4000),
    ("cloak of charisma +2", 4000),
    ("cloak of resistance +2", 4000),
    ("gauntlets of ogre power", 4000),
    ("gloves of arrow snaring", 4000),
    ("gloves of dexterity +2", 4000),
    ("headband of intellect +2", 4000),
    ("ioun stone, clear spindle", 4000),
    ("Keoghtom's ointment", 4000),
    ("Nolzur's marvelous pigments", 4000),
    ("pearl of power, 2nd-level spell", 4000),
    ("periapt of wisdom +2", 4000),
    ("stone salve", 4000),
    ("necklace of fireballs type III", 4350),
    ("circlet of persuasion", 4500),
    ("slippers of spider climbing", 4800),
    ("incense of meditation", 4900),
    ("bag of holding type II", 5000),
    ("bracers of archery, lesser", 5000),
    ("ioun stone, dusty rose prism", 5000),
    ("helm of comprehend languages and read magic", 5200),
    ("vest of escape", 5200),
    ("eversmoking bottle", 5400),
    ("Murlynd's spoon", 5400),
    ("necklace of fireballs type IV", 5400),
    ("boots of striding and springing", 5500),
    ("wind fan", 5500),
    ("amulet of mighty fists +1", 6000),
    ("horseshoes of a zephyr", 6000),
    ("pipes of haunting", 6000),
    ("necklace of fireballs type V", 6150),
    ("gloves of swimming and climbing", 6250),
    ("bag of tricks, tan", 6300),
    ("circlet of blasting, minor", 6480),
    ("horn of goodness/evil", 6500),
    ("robe of useful items", 7000),
    ("boat, folding", 7200),
    ("cloak of the manta ray", 7200),
    ("bottle of air", 7250),
    ("bag of holding type III", 7400),
    ("periapt of health", 7400)
    )

    item_index = (percentage_roll-1)

    name = item_tuple[item_index][0]
    base_value = item_tuple[item_index][1]

    dct_item["name"] = name
    dct_item["value"] = base_value

    return dct_item


#-----------------------------------------------------------------------
#------ Generate Medium Wondrous Item (Table 7-28, Page 249) -----------
#-----------------------------------------------------------------------


def GetOneMediumWondrous():
    dct_item = {}

    percentage_roll = crDice.RollPercentage()[1]

    item_tuple = (
    ("boots of levitation", 7500),
    ("harp of charming", 7500),
    ("amulet of natural armor +2", 8000),
    ("golem manual, flesh", 8000),
    ("hand of glory", 8000),
    ("ioun stone, deep red sphere", 8000),
    ("ioun stone, incandescent blue sphere", 8000),
    ("ioun stone, pale blue rhomboid", 8000),
    ("ioun stone, pink and green sphere", 8000),
    ("ioun stone, pink rhomboid", 8000),
    ("ioun stone, scarlet and blue sphere", 8000),
    ("deck of illusions", 8100),
    ("necklace of fireballs type VI", 8100),
    ("candle of invocation", 8400),
    ("bracers of armor +3", 9000),
    ("cloak of resistance +3", 9000),
    ("decanter of endless water", 9000),
    ("necklace of adaptation", 9000),
    ("pearl of power, 3rd-level spell", 9000),
    ("talisman of the sphere", 9000),
    ("figurine of wondrous power, serpentine owl", 9100),
    ("necklace of fireballs type VII", 9150),
    ("strand of prayer beads, lesser", 9600),
    ("bag of holding type IV", 10000),
    ("figurine of wondrous power, bronze griffon", 10000),
    ("figurine of wondrous power, ebony fly", 10000),
    ("glove of storing", 10000),
    ("ioun stone, dark blue rhomboid", 10000),
    ("stone horse, courser", 10000),
    ("cape of the mountebank", 10080),
    ("phylactery of undead turning", 11000),
    ("gauntlet of rust", 11500),
    ("boots of speed", 12000),
    ("goggles of night", 12000),
    ("golem manual, clay", 12000),
    ("medallion of thoughts", 12000),
    ("pipes of pain", 12000),
    ("Boccob's blessed book", 12500),
    ("belt, monk's", 13000),
    ("gem of brightness", 13000),
    ("lyre of building", 13000),
    ("cloak of arachnida", 14000),
    ("stone horse, destrier", 14800),
    ("belt of dwarvenkind", 14900),
    ("periapt of wound closure", 15000),
    ("horn of the tritons", 15100),
    ("pearl of the sirines", 15300),
    ("figurine of wondrous power, onyx dog", 15500),
    ("amulet of health +4", 16000),
    ("belt of giant strength +4", 16000),
    ("boots, winged", 16000),
    ("bracers of armor +4", 16000),
    ("cloak of charisma +4", 16000),
    ("cloak of resistance +4", 16000),
    ("gloves of dexterity +4", 16000),
    ("headband of intellect +4", 16000),
    ("pearl of power, 4th-level spell", 16000),
    ("periapt of wisdom +4", 16000),
    ("scabbard of keen edges", 16000),
    ("figurine of wondrous power, golden lions", 16500),
    ("chime of interruption", 16800),
    ("broom of flying", 17000),
    ("figurine of wondrous power, marble elephant", 17000),
    ("amulet of natural armor +3", 18000),
    ("ioun stone, iridescent spindle", 18000),
    ("bracelet of friends", 19000),
    ("carpet of flying, 5 ft. by 5 ft.", 20000),
    ("horn of blasting", 20000),
    ("ioun stone, pale lavender ellipsoid", 20000),
    ("ioun stone, pearly white spindle", 20000),
    ("portable hole", 20000),
    ("stone of good luck (luckstone)", 20000),
    ("figurine of wondrous power, ivory goats", 21000),
    ("rope of entanglement", 21000),
    ("golem manual, stone", 22000),
    ("mask of the skull", 22000),
    ("mattock of the titans", 23348),
    ("circlet of blasting, major", 23760),
    ("amulet of mighty fists +2", 24000),
    ("cloak of displacement, minor", 24000),
    ("helm of underwater action", 24000),
    ("bracers of archery, greater", 25000),
    ("bracers of armor +5", 25000),
    ("cloak of resistance +5", 25000),
    ("eyes of doom", 25000),
    ("pearl of power, 5th-level spell", 25000),
    ("maul of the titans", 25305),
    ("strand of prayer beads", 25800),
    ("cloak of the bat", 26000),
    ("iron bands of Bilarro", 26000),
    ("cube of frost resistance", 27000),
    ("helm of telepathy", 27000),
    ("periapt of proof against poison", 27000),
    ("robe of scintillating colors", 27000),
    ("manual of bodily health +1", 27500),
    ("manual of gainful exercise +1", 27500),
    ("manual of quickness in action +1", 27500),
    ("tome of clear thought +1", 27500),
    ("tome of leadership and influence +1", 27500),
    ("tome of understanding +1", 27500)
    )

    item_index = (percentage_roll-1)

    name = item_tuple[item_index][0]
    base_value = item_tuple[item_index][1]

    dct_item["name"] = name
    dct_item["value"] = base_value

    return dct_item


#-----------------------------------------------------------------------
#------ Generate Major Wondrous Item (Table 7-29, Page 251) ------------
#-----------------------------------------------------------------------


def GetOneMajorWondrous():
    dct_item = {}

    percentage_roll = crDice.RollPercentage()[1]

    item_tuple = (
    ("dimensional shackles", 28000),
    ("figurine of wondrous power, obsidian steed", 28500),
    ("drums of panic", 30000),
    ("ioun stone, orange", 30000),
    ("ioun stone, pale green prism", 30000),
    ("lantern of revealing", 30000),
    ("robe of blending", 30000),
    ("amulet of natural armor +4", 32000),
    ("amulet of proof against detection and location", 35000),
    ("carpet of flying, 5 ft. by 10 ft.", 35000),
    ("golem manual, iron", 35000),
    ("amulet of health +6", 36000),
    ("belt of giant strength +6", 36000),
    ("bracers of armor +6", 36000),
    ("cloak of charisma +6", 36000),
    ("gloves of dexterity +6", 36000),
    ("headband of intellect +6", 36000),
    ("ioun stone, vibrant purple prism", 36000),
    ("pearl of power, 6th-level spell", 36000),
    ("periapt of wisdom +6", 36000),
    ("scarab of protection", 38000),
    ("ioun stone, lavender and green ellipsoid", 40000),
    ("ring gates", 40000),
    ("crystal ball", 42000),
    ("golem manual, greater stone", 44000),
    ("orb of storms", 48000),
    ("boots of teleportation", 49000),
    ("bracers of armor +7", 49000),
    ("pearl of power, 7th-level spell", 49000),
    ("amulet of natural armor +5", 50000),
    ("cloak of displacement, major", 50000),
    ("crystal ball with see invisibility", 50000),
    ("horn of Valhalla", 50000),
    ("crystal ball with detect thoughts", 51000),
    ("carpet of flying, 6 ft. by 9 ft.", 53000),
    ("amulet of mighty fists +3", 54000),
    ("wings of flying", 54000),
    ("cloak of etherealness", 55000),
    ("Daern's instant fortress", 55000),
    ("manual of bodily health +2", 55000),
    ("manual of gainful exercise +2", 55000),
    ("manual of quickness in action +2", 55000),
    ("tome of clear thought +2", 55000),
    ("tome of leadership and influence +2", 55000),
    ("tome of understanding +2", 55000),
    ("eyes of charming", 56000),
    ("robe of stars", 58000),
    ("carpet of flying, 10 ft. by 10 ft.", 60000),
    ("darkskull", 60000),
    ("cube of force", 62000),
    ("bracers of armor +8", 64000),
    ("pearl of power, 8th-level spell", 64000),
    ("crystal ball with telepathy", 70000),
    ("horn of blasting, greater", 70000),
    ("pearl of power, two spells", 70000),
    ("helm of teleportation", 73500),
    ("gem of seeing", 75000),
    ("robe of the archmagi", 75000),
    ("mantle of faith", 76000),
    ("crystal ball with true seeing", 80000),
    ("pearl of power, 9th-level spell", 81000),
    ("well of many worlds", 82000),
    ("manual of bodily health +3", 82500),
    ("manual of gainful exercise +3", 82500),
    ("manual of quickness in action +3", 82500),
    ("tome of clear thought +3", 82500),
    ("tome of leadership and influence +3", 82500),
    ("tome of understanding +3", 82500),
    ("apparatus of Kwalish", 90000),
    ("mantle of spell resistance", 90000),
    ("mirror of opposition", 92000),
    ("strand of prayer beads, greater", 95800),
    ("amulet of mighty fists +4", 96000),
    ("eyes of petrification", 98000),
    ("bowl of commanding water elementals", 100000),
    ("brazier of commanding fire elementals", 100000),
    ("censer of controlling air elementals", 100000),
    ("stone of controlling earth elementals", 100000),
    ("manual of bodily health +4", 110000),
    ("manual of gainful exercise +4", 110000),
    ("manual of quickness in action +4", 110000),
    ("tome of clear thought +4", 110000),
    ("tome of leadership and influence +4", 110000),
    ("tome of understanding +4", 110000),
    ("amulet of the planes", 120000),
    ("robe of eyes", 120000),
    ("helm of brilliance", 125000),
    ("manual of bodily health +5", 137500),
    ("manual of gainful exercise +5", 137500),
    ("manual of quickness in action +5", 137500),
    ("tome of clear thought +5", 137500),
    ("tome of leadership and influence +5", 137500),
    ("tome of understanding +5", 137500),
    ("efreeti bottle", 145000),
    ("amulet of mighty fists +5", 150000),
    ("chaos diamond", 160000),
    ("cubic gate", 164000),
    ("iron flask", 170000),
    ("mirror of mental prowess", 175000),
    ("mirror of life trapping", 200000)
    )

    item_index = (percentage_roll-1)

    name = item_tuple[item_index][0]
    base_value = item_tuple[item_index][1]

    dct_item["name"] = name
    dct_item["value"] = base_value

    return dct_item


#-----------------------------------------------------------------------
#------ Generate One Random Wondrous Item ------------------------------
#-----------------------------------------------------------------------


def GetOneWondrous(m_type):
    minor = False
    medium = False
    major = False

    if string.upper(m_type) == "MINOR": minor = True
    elif string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True

    if minor:
        return GetOneMinorWondrous()
    elif medium:
        return GetOneMediumWondrous()
    elif major:
        return GetOneMajorWondrous()


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
