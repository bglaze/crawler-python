#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Treasure Generators for Crawler I
#  by Brock Glaze
#
#  crCalc_Treasure_Armor.py


import crawler
import crDice
import crCalc_Treasure_Scrolls as scroll_lib
import string
import wx


#-----------------------------------------------------------------------
#------ Generate Armor Type (Table 7-3, Page 216) ----------------------
#-----------------------------------------------------------------------


def GetArmorType(masterwork=False, magic=False):
    dct_item = {}

    percentage_roll = crDice.RollPercentage()[1]

    if percentage_roll <= 1:
        base_value = 5
        name = "padded"
    elif percentage_roll <= 2:
        base_value = 10
        name = "leather"
    elif percentage_roll <= 17:
        base_value = 25
        name = "studded leather"
    elif percentage_roll <= 32:
        base_value = 100
        name = "chain shirt"
    elif percentage_roll <= 42:
        base_value = 15
        name = "hide"
    elif percentage_roll <= 43:
        base_value = 50
        name = "scale mail"
    elif percentage_roll <= 44:
        base_value = 150
        name = "chainmail"
    elif percentage_roll <= 57:
        base_value = 200
        name = "breastplate"
    elif percentage_roll <= 58:
        base_value = 200
        name = "splint mail"
    elif percentage_roll <= 59:
        base_value = 250
        name = "banded mail"
    elif percentage_roll <= 60:
        base_value = 600
        name = "half-plate"
    elif percentage_roll <= 100:
        base_value = 1500
        name = "full plate"

    if magic:
        masterwork = True

    if masterwork:
        base_value += 150
        if not magic:
            name = "%s, masterwork" % name

    dct_item["name"] = name
    dct_item["value"] = base_value
    dct_item["mod"] = 0

    return dct_item


def GetShieldType(masterwork=False, magic=False):
    dct_item = {}

    percentage_roll = crDice.RollPercentage()[1]

    if percentage_roll <= 10:
        base_value = 15
        name = "buckler"
    elif percentage_roll <= 15:
        base_value = 3
        name = "shield, light, wooden"
    elif percentage_roll <= 20:
        base_value = 9
        name = "shield, light, steel"
    elif percentage_roll <= 30:
        base_value = 7
        name = "shield, heavy, wooden"
    elif percentage_roll <= 95:
        base_value = 20
        name = "shield, heavy, steel"
    elif percentage_roll <= 100:
        base_value = 30
        name = "shield, tower"

    if magic:
        masterwork = True

    if masterwork:
        base_value += 150
        if not magic:
            name = "%s, masterwork" % name

    dct_item["name"] = name
    dct_item["value"] = base_value
    dct_item["mod"] = 0

    return dct_item


#-----------------------------------------------------------------------
#------ Generate Specific Armor / Shields (Table 7-14, 7-15 Page 227) --
#-----------------------------------------------------------------------


def GetSpecificArmor(m_type):
    dct_item = {}

    minor = False
    medium = False
    major = False

    if string.upper(m_type) == "MINOR": minor = True
    elif string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True

    percentage_roll = crDice.RollPercentage()[1]

    if (percentage_roll <= 50 and minor
    or percentage_roll <= 25 and medium):
        name = "mithral shirt"
        base_value = 1100
        mod = 1
    elif (percentage_roll <= 80 and minor
    or percentage_roll <= 45 and medium):
        name = "dragonhide plate"
        base_value = 3300
        mod = 1
    elif (percentage_roll <= 100 and minor
    or percentage_roll <= 57 and medium):
        name = "elven chain"
        base_value = 4150
        mod = 1
    elif percentage_roll <= 67 and medium:
        name = "rhino hide"
        base_value = 5165
        mod = 2
    elif (percentage_roll <= 82 and medium
    or percentage_roll <= 10 and major):
        name = "adamantine breastplate"
        base_value = 10200
        mod = 1
    elif (percentage_roll <= 97 and medium
    or percentage_roll <= 20 and major):
        name = "dwarven plate"
        base_value = 16500
        mod = 1
    elif (percentage_roll <= 100 and medium
    or percentage_roll <= 32 and major):
        name = "banded mail of luck"
        base_value = 18900
        mod = 3
    elif percentage_roll <= 50 and major:
        name = "celestial armor"
        base_value = 22400
        mod = 3
    elif percentage_roll <= 60 and major:
        name = "plate armor of the deep"
        base_value = 24650
        mod = 1
    elif percentage_roll <= 75 and major:
        name = "breastplate of command"
        base_value = 25400
        mod = 2
    elif percentage_roll <= 90 and major:
        name = "mithral full plate of speed"
        base_value = 26500
        mod = 1
    elif percentage_roll <= 100 and major:
        name = "demon armor"
        base_value = 52260
        mod = 4

    dct_item["name"] = name
    dct_item["value"] = base_value
    dct_item["mod"] = mod

    return dct_item


def GetSpecificShield(m_type):
    dct_item = {}

    minor = False
    medium = False
    major = False

    if string.upper(m_type) == "MINOR": minor = True
    elif string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True

    percentage_roll = crDice.RollPercentage()[1]

    if (percentage_roll <= 30 and minor
    or percentage_roll <= 20 and medium):
        name = "darkwood buckler"
        base_value = 205
        mod = 1
    elif (percentage_roll <= 80 and minor
    or percentage_roll <= 45 and medium):
        name = "darkwood shield"
        base_value = 257
        mod = 1
    elif (percentage_roll <= 95 and minor
    or percentage_roll <= 70 and medium):
        name = "mithral heavy shield"
        base_value = 1020
        mod = 1
    elif (percentage_roll <= 100 and minor
    or percentage_roll <= 85 and medium
    or percentage_roll <= 20 and major):
        name = "caster's shield"
        base_value = 3153
        mod = 1

        has_spell_roll = crDice.RollPercentage()[1]
        if has_spell_roll <= 50:
            pass
        elif has_spell_roll <= 100:

            s_type_roll = crDice.RollPercentage()[1]
            if s_type_roll <= 80:
                s_type = "divine"
            elif s_type_roll <= 100:
                s_type = "arcane"

            s_level_roll = crDice.RollDice(1, 65)[1]
            if s_level_roll <= 5:
                s_level = 2
            elif s_level_roll <= 65:
                s_level = 3

            name += (" - w/spell (%s)" %
            scroll_lib.GetOneSpell(s_type, s_level)["name"])

    elif (percentage_roll <= 90 and medium
    or percentage_roll <= 40 and major):
        name = "spined shield"
        base_value = 5580
        mod = 1
    elif (percentage_roll <= 95 and medium
    or percentage_roll <= 60 and major):
        name = "lion's shield"
        base_value = 9170
        mod = 2
    elif (percentage_roll <= 100 and medium
    or percentage_roll <= 90 and major):
        name = "winged shield"
        base_value = 17257
        mod = 3
    elif percentage_roll <= 100 and major:
        name = "absorbing shield"
        base_value = 50170
        mod = 1

    dct_item["name"] = name
    dct_item["value"] = base_value
    dct_item["mod"] = mod

    return dct_item


#-----------------------------------------------------------------------
#------ Armor/Shields Special Abilities (Table 7-5/7-6, Page 217) ------
#-----------------------------------------------------------------------


def GetArmorSpecialAbilities(m_type, item, dct_abilities=None):

    if not dct_abilities:
        dct_abilities = {}

    # These values exist to allow for recursion
    ability = None
    value = " "
    mod = -1
    skip_ability = False

    # This dict allows us to add weight value
    # to mods that are strings
    dct_mods = {0:0,

                "light": 1,
                "moderate": 2,
                "heavy": 3,

                "improved": 4,
                "greater": 5,

                "13": 13,
                "15": 15,
                "17": 17,
                "19": 19}

    minor = False
    medium = False
    major = False

    if string.upper(m_type) == "MINOR": minor = True
    elif string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True

    percentage_roll = crDice.RollPercentage()[1]

    if (percentage_roll <= 25 and minor
    or percentage_roll <= 5 and medium
    or percentage_roll <= 3 and major):
        ability = "glamered"
        mod = 0
        value = "2700"
    elif (percentage_roll <= 32 and minor
    or percentage_roll <= 8 and medium
    or percentage_roll <= 4 and major):
        ability = "fortification"
        mod = "light"
        value = "+1"
    elif (percentage_roll <= 52 and minor
    or percentage_roll <= 11 and medium):
        ability = "slick"
        mod = 0
        value = "3750"
    elif (percentage_roll <= 72 and minor
    or percentage_roll <= 14 and medium):
        ability = "shadow"
        mod = 0
        value = "3750"
    elif (percentage_roll <= 92 and minor
    or percentage_roll <= 17 and medium):
        ability = "silent moves"
        mod = 0
        value = "3750"
    elif (percentage_roll <= 96 and minor
    or percentage_roll <= 19 and medium):
        ability = "spell resistance"
        mod = "13"
        value = "+2"
    elif (percentage_roll <= 97 and minor
    or percentage_roll <= 29 and medium
    or percentage_roll <= 7 and major):
        ability = "slick"
        mod = "improved"
        value = "15000"
    elif (percentage_roll <= 98 and minor
    or percentage_roll <= 39 and medium
    or percentage_roll <= 10 and major):
        ability = "shadow"
        mod = "improved"
        value = "15000"
    elif (percentage_roll <= 99 and minor
    or percentage_roll <= 49 and medium
    or percentage_roll <= 13 and major):
        ability = "silent moves"
        mod = "improved"
        value = "15000"
    elif (percentage_roll <= 54 and medium
    or percentage_roll <= 16 and major):
        ability = "acid resistance"
        mod = 0
        value = "18000"
    elif (percentage_roll <= 59 and medium
    or percentage_roll <= 19 and major):
        ability = "cold resistance"
        mod = 0
        value = "18000"
    elif (percentage_roll <= 64 and medium
    or percentage_roll <= 22 and major):
        ability = "electricity resistance"
        mod = 0
        value = "18000"
    elif (percentage_roll <= 69 and medium
    or percentage_roll <= 25 and major):
        ability = "fire resistance"
        mod = 0
        value = "18000"
    elif (percentage_roll <= 74 and medium
    or percentage_roll <= 28 and major):
        ability = "sonic resistance"
        mod = 0
        value = "18000"
    elif (percentage_roll <= 79 and medium
    or percentage_roll <= 33 and major):
        ability = "ghost touch"
        mod = 0
        value = "+3"
    elif (percentage_roll <= 84 and medium
    or percentage_roll <= 35 and major):
        ability = "invulnerability"
        mod = 0
        value = "+3"
    elif (percentage_roll <= 89 and medium
    or percentage_roll <= 40 and major):
        ability = "fortification"
        mod = "moderate"
        value = "+3"
    elif (percentage_roll <= 94 and medium
    or percentage_roll <= 42 and major):
        ability = "spell resistance"
        mod = "15"
        value = "+3"
    elif (percentage_roll <= 99 and medium
    or percentage_roll <= 43 and major):
        ability = "wild"
        mod = 0
        value = "+3"
    elif percentage_roll <= 48 and major:
        ability = "slick"
        mod = "greater"
        value = "33750"
    elif percentage_roll <= 53 and major:
        ability = "shadow"
        mod = "greater"
        value = "33750"
    elif percentage_roll <= 58 and major:
        ability = "silent moves"
        mod = "greater"
        value = "33750"
    elif percentage_roll <= 63 and major:
        ability = "acid resistance"
        mod = "improved"
        value = "42000"
    elif percentage_roll <= 68 and major:
        ability = "cold resistance"
        mod = "improved"
        value = "42000"
    elif percentage_roll <= 73 and major:
        ability = "electricity resistance"
        mod = "improved"
        value = "42000"
    elif percentage_roll <= 78 and major:
        ability = "fire resistance"
        mod = "improved"
        value = "42000"
    elif percentage_roll <= 83 and major:
        ability = "sonic resistance"
        mod = "improved"
        value = "42000"
    elif percentage_roll <= 88 and major:
        ability = "spell resistance"
        mod = "17"
        value = "+4"
    elif percentage_roll <= 89 and major:
        ability = "etherealness"
        mod = 0
        value = "49000"
    elif percentage_roll <= 90 and major:
        ability = "undead controlling"
        mod = 0
        value = "49000"
    elif percentage_roll <= 92 and major:
        ability = "fortification"
        mod = "heavy"
        value = "+5"
    elif percentage_roll <= 94 and major:
        ability = "spell resistance"
        mod = "19"
        value = "+5"
    elif percentage_roll <= 95 and major:
        ability = "acid resistance"
        mod = "greater"
        value = "66000"
    elif percentage_roll <= 96 and major:
        ability = "cold resistance"
        mod = "greater"
        value = "66000"
    elif percentage_roll <= 97 and major:
        ability = "electricity resistance"
        mod = "greater"
        value = "66000"
    elif percentage_roll <= 98 and major:
        ability = "fire resistance"
        mod = "greater"
        value = "66000"
    elif percentage_roll <= 99 and major:
        ability = "sonic resistance"
        mod = "greater"
        value = "66000"
    elif (percentage_roll <= 100 and minor
    or percentage_roll <= 100 and medium
    or percentage_roll <= 100 and major):
        # Use Recursion to Roll Again Twice
        for x in xrange(2):
            GetArmorSpecialAbilities(m_type, item, dct_abilities)


    # Do not allow an ability to be added if it takes the total
    # item mod/enhancement value above +10
    total_mods = 0
    for abil in dct_abilities.keys():
        if dct_abilities[abil]["value"][0] == "+":
            total_mods += int(dct_abilities[abil]["value"][0:])
    if (value[0] == "+"
    and int(value[0:]) + total_mods + item["mod"]) > 10:
        skip_ability = True


    # Add ability to dictionary
    if ability and (mod >= 0) and not skip_ability:
        if dct_abilities and dct_abilities.has_key(ability):
            if dct_abilities[ability]["mod"] == mod:
                # Same Ability + Same Mod = No Change
                return dct_abilities

            elif dct_mods[mod] > dct_mods[dct_abilities[ability]["mod"]]:
                # Same Ability + Better Mod = Replace Ability
                dct_abilities[ability]["mod"] = mod
                dct_abilities[ability]["value"] = value
        else:
            dct_abilities[ability] = {}
            dct_abilities[ability]["mod"] = mod
            dct_abilities[ability]["value"] = value

    return dct_abilities


def GetShieldSpecialAbilities(m_type, item, dct_abilities=None):

    if not dct_abilities:
        dct_abilities = {}

    # These values exist to allow for recursion
    ability = None
    value = " "
    mod = -1
    skip_ability = False

    # This dict allows us to add weight value
    # to mods that are strings
    dct_mods = {0:0,

                "light": 1,
                "moderate": 2,
                "heavy": 3,

                "improved": 4,
                "greater": 5,

                "13": 13,
                "15": 15,
                "17": 17,
                "19": 19}

    minor = False
    medium = False
    major = False

    if string.upper(m_type) == "MINOR": minor = True
    elif string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True

    percentage_roll = crDice.RollPercentage()[1]

    if (percentage_roll <= 20 and minor
    or percentage_roll <= 10 and medium
    or percentage_roll <= 5 and major):
        ability = "arrow catching"
        mod = 0
        value = "+1"
    elif (percentage_roll <= 40 and minor
    or percentage_roll <= 20 and medium
    or percentage_roll <= 8 and major):
        ability = "bashing"
        mod = 0
        value = "+1"
    elif (percentage_roll <= 50 and minor
    or percentage_roll <= 25 and medium
    or percentage_roll <= 10 and major):
        ability = "blinding"
        mod = 0
        value = "+1"
    elif (percentage_roll <= 75 and minor
    or percentage_roll <= 40 and medium
    or percentage_roll <= 15 and major):
        ability = "fortification"
        mod = "light"
        value = "+1"
    elif (percentage_roll <= 92 and minor
    or percentage_roll <= 50 and medium
    or percentage_roll <= 20 and major):
        ability = "arrow deflection"
        mod = 0
        value = "+2"
    elif (percentage_roll <= 97 and minor
    or percentage_roll <= 57 and medium
    or percentage_roll <= 25 and major):
        ability = "animated"
        mod = 0
        value = "+2"
    elif (percentage_roll <= 99 and minor
    or percentage_roll <= 59 and medium):
        ability = "spell resistance"
        mod = "13"
        value = "+2"
    elif (percentage_roll <= 63 and medium
    or percentage_roll <= 28 and major):
        ability = "acid resistance"
        mod = 0
        value = "18000"
    elif (percentage_roll <= 67 and medium
    or percentage_roll <= 31 and major):
        ability = "cold resistance"
        mod = 0
        value = "18000"
    elif (percentage_roll <= 71 and medium
    or percentage_roll <= 34 and major):
        ability = "electricity resistance"
        mod = 0
        value = "18000"
    elif (percentage_roll <= 75 and medium
    or percentage_roll <= 37 and major):
        ability = "fire resistance"
        mod = 0
        value = "18000"
    elif (percentage_roll <= 79 and medium
    or percentage_roll <= 40 and major):
        ability = "sonic resistance"
        mod = 0
        value = "18000"
    elif (percentage_roll <= 85 and medium
    or percentage_roll <= 46 and major):
        ability = "ghost touch"
        mod = 0
        value = "+3"
    elif (percentage_roll <= 95 and medium
    or percentage_roll <= 56 and major):
        ability = "fortification"
        mod = "moderate"
        value = "+3"
    elif (percentage_roll <= 98 and medium
    or percentage_roll <= 58 and major):
        ability = "spell resistance"
        mod = "15"
        value = "+3"
    elif (percentage_roll <= 99 and medium
    or percentage_roll <= 59 and major):
        ability = "wild"
        mod = 0
        value = "+3"
    elif percentage_roll <= 64 and major:
        ability = "acid resistance"
        mod = "improved"
        value = "42000"
    elif percentage_roll <= 69 and major:
        ability = "cold resistance"
        mod = "improved"
        value = "42000"
    elif percentage_roll <= 74 and major:
        ability = "electricity resistance"
        mod = "improved"
        value = "42000"
    elif percentage_roll <= 79 and major:
        ability = "fire resistance"
        mod = "improved"
        value = "42000"
    elif percentage_roll <= 84 and major:
        ability = "sonic resistance"
        mod = "improved"
        value = "42000"
    elif percentage_roll <= 86 and major:
        ability = "spell resistance"
        mod = "17"
        value = "+4"
    elif percentage_roll <= 87 and major:
        ability = "undead controlling"
        mod = 0
        value = "49000"
    elif percentage_roll <= 91 and major:
        ability = "fortification"
        mod = "heavy"
        value = "+5"
    elif percentage_roll <= 93 and major:
        ability = "reflecting"
        mod = 0
        value = "+5"
    elif percentage_roll <= 94 and major:
        ability = "spell resistance"
        mod = "19"
        value = "+5"
    elif percentage_roll <= 95 and major:
        ability = "acid resistance"
        mod = "greater"
        value = "66000"
    elif percentage_roll <= 96 and major:
        ability = "cold resistance"
        mod = "greater"
        value = "66000"
    elif percentage_roll <= 97 and major:
        ability = "electricity resistance"
        mod = "greater"
        value = "66000"
    elif percentage_roll <= 98 and major:
        ability = "fire resistance"
        mod = "greater"
        value = "66000"
    elif percentage_roll <= 99 and major:
        ability = "sonic resistance"
        mod = "greater"
        value = "66000"
    elif (percentage_roll <= 100 and minor
    or percentage_roll <= 100 and medium
    or percentage_roll <= 100 and major):
        # Use Recursion to Roll Again Twice
        for x in xrange(2):
            GetShieldSpecialAbilities(m_type, item, dct_abilities)


    # Do not allow an ability to be added if it takes the total
    # item mod/enhancement value above +10
    total_mods = 0
    for abil in dct_abilities.keys():
        if dct_abilities[abil]["value"][0] == "+":
            total_mods += int(dct_abilities[abil]["value"][0:])
    if (value[0] == "+"
    and int(value[0:]) + total_mods + item["mod"]) > 10:
        skip_ability = True


    # Add ability to dictionary
    if ability and (mod >= 0) and not skip_ability:
        if dct_abilities and dct_abilities.has_key(ability):
            if dct_abilities[ability]["mod"] == mod:
                # Same Ability + Same Mod = No Change
                return dct_abilities

            elif dct_mods[mod] > dct_mods[dct_abilities[ability]["mod"]]:
                # Same Ability + Better Mod = Replace Ability
                dct_abilities[ability]["mod"] = mod
                dct_abilities[ability]["value"] = value
        else:
            dct_abilities[ability] = {}
            dct_abilities[ability]["mod"] = mod
            dct_abilities[ability]["value"] = value

    return dct_abilities


#-----------------------------------------------------------------------
#------ Generate One Magic Armor / Shield (Table 7-2, Page 216) --------
#-----------------------------------------------------------------------


def GetOneMagicArmorShield(m_type):

    dct_item = {}

    dct_types = {}
    dct_types["armor"] = GetArmorType
    dct_types["shield"] = GetShieldType
    dct_types["specific_armor"] = GetSpecificArmor
    dct_types["specific_shield"] = GetSpecificShield

    i_type=None
    specific = False
    dct_abilities = {}
    special_abilities_count = 0
    ability_str = ""

    minor = False
    medium = False
    major = False

    if string.upper(m_type) == "MINOR": minor = True
    elif string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True

    while True:

        percentage_roll = crDice.RollPercentage()[1]

        if (percentage_roll <= 60 and minor
        or percentage_roll <= 5 and medium):
            mod = 1
            i_type = "shield"
        elif (percentage_roll <= 80 and minor
        or percentage_roll <= 10 and medium):
            mod = 1
            i_type = "armor"
        elif (percentage_roll <= 85 and minor
        or percentage_roll <= 20 and medium):
            mod = 2
            i_type = "shield"
        elif (percentage_roll <= 87 and minor
        or percentage_roll <= 30 and medium):
            mod = 2
            i_type = "armor"
        elif (percentage_roll <= 40 and medium
        or percentage_roll <= 8 and major):
            mod = 3
            i_type = "shield"
        elif (percentage_roll <= 50 and medium
        or percentage_roll <= 16 and major):
            mod = 3
            i_type = "armor"
        elif (percentage_roll <= 55 and medium
        or percentage_roll <= 27 and major):
            mod = 4
            i_type = "shield"
        elif (percentage_roll <= 57 and medium
        or percentage_roll <= 38 and major):
            mod = 4
            i_type = "armor"
        elif percentage_roll <= 49 and major:
            mod = 5
            i_type = "shield"
        elif percentage_roll <= 57 and major:
            mod = 5
            i_type = "armor"
        elif (percentage_roll <= 89 and minor
        or percentage_roll <= 60 and medium
        or percentage_roll <= 60 and major):
            i_type = "specific_armor"
            specific = True
        elif (percentage_roll <= 91 and minor
        or percentage_roll <= 63 and medium
        or percentage_roll <= 63 and major):
            i_type = "specific_shield"
            specific = True
        elif (percentage_roll <= 100 and minor
        or percentage_roll <= 100 and medium
        or percentage_roll <= 100 and major):
            special_abilities_count += 1
            continue

        if specific:

            item = dct_types[i_type](m_type)
            name = item["name"]
            base_value = item["value"]
            mod = item["mod"]

            # Comment out the next two lines
            # to allow specific armor/shields to have special abilities
            mod = 0
            break

        else:
            item = dct_types[i_type](magic=True)
            item["mod"] += mod
            name = "%s +%d" % (item["name"], mod)
            base_value = item["value"]


        # Generate appropriate abilities
        # based upon if the final item is armor or a shield
        for x in xrange(special_abilities_count):
            if not dct_abilities:
                if i_type == "armor" or i_type == "specific_armor":
                    dct_abilities = GetArmorSpecialAbilities(m_type, item)
                elif i_type == "shield" or i_type == "specific_shield":
                    dct_abilities = GetShieldSpecialAbilities(m_type, item)
            else:
                if i_type == "armor" or i_type == "specific_armor":
                    GetArmorSpecialAbilities(m_type, item, dct_abilities)
                elif i_type == "shield" or i_type == "specific_shield":
                    GetShieldSpecialAbilities(m_type, item, dct_abilities)

        
        if dct_abilities:

            if len(dct_abilities.keys()) > 1:
                ability_str += " - w/abilities ("
            else:
                ability_str += " - w/ability ("

            for ability in dct_abilities.keys():

                # If value contains '+' then add to effective bonus
                # where value is concerned.
                if dct_abilities[ability]["value"][0] == "+":
                    mod += int(dct_abilities[ability]["value"][0:])
                else:
                    base_value += int(dct_abilities[ability]["value"])

                ability_str += '%s' % ability
                if dct_abilities[ability]["mod"]:
                    if dct_abilities[ability]["mod"].isdigit():
                        ability_str += ' [%s]; ' % dct_abilities[ability]["mod"]
                    else:
                        ability_str += ', %s; ' % dct_abilities[ability]["mod"]
                else:
                    ability_str += '; '

            ability_str = "%s)" % ability_str[:-2]

        break

    name += ability_str
    base_value += ((mod**2) * 1000)

    dct_item["name"] = name
    dct_item["value"] = base_value

    return dct_item


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
