#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Treasure Generators for Crawler I
#  by Brock Glaze
#
#  crCalc_Treasure_Weapons.py


import crawler
import crDice
import string
import wx


#-----------------------------------------------------------------------
#------ Generate Weapon Type (Table 7-10, Page 222) --------------------
#-----------------------------------------------------------------------


def GetWeaponType(masterwork=False, magic=False):

    percentage_roll = crDice.RollPercentage()[1]

    if percentage_roll <= 70:
        return GetOneCommonMeleeWep(masterwork, magic)
    elif percentage_roll <= 80:
        return GetOneUncommonWep(masterwork, magic)
    elif percentage_roll <= 100:
        return GetOneCommonRangedWep(masterwork, magic)


#-----------------------------------------------------------------------
#------ Generate Common Melee Weapons (Table 7-11, Page 222)------------
#-----------------------------------------------------------------------


def GetOneCommonMeleeWep(masterwork=False, magic=False):
    # All values for weapons are in gold
    dct_weapon = {}

    double_weapon = False
    atk_type = ""

    percentage_roll = crDice.RollPercentage()[1]

    if percentage_roll <= 4:
        base_value = 2
        name = "dagger"
        atk_type = "slashing, piercing"
    elif percentage_roll <= 14:
        base_value = 20
        name = "greataxe"
        atk_type = "slashing"
    elif percentage_roll <= 24:
        base_value = 50
        name = "greatsword"
        atk_type = "slashing"
    elif percentage_roll <= 28:
        base_value = 2
        name = "kama"
        atk_type = "slashing"
    elif percentage_roll <= 41:
        base_value = 15
        name = "longsword"
        atk_type = "slashing"
    elif percentage_roll <= 45:
        base_value = 5
        name = "mace, light"
        atk_type = "bludgeoning"
    elif percentage_roll <= 50:
        base_value = 12
        name = "mace, heavy"
        atk_type = "bludgeoning"
    elif percentage_roll <= 54:
        base_value = 2
        name = "nunchaku"
        atk_type = "bludgeoning"
    elif percentage_roll <= 57:
        base_value = 0
        double_weapon = True
        name = "quarterstaff"
        atk_type = "bludgeoning"
    elif percentage_roll <= 61:
        base_value = 20
        name = "rapier"
        atk_type = "piercing"
    elif percentage_roll <= 66:
        base_value = 15
        name = "scimitar"
        atk_type = "slashing"
    elif percentage_roll <= 70:
        base_value = 2
        name = "shortspear"
        atk_type = "piercing"
    elif percentage_roll <= 74:
        base_value = 3
        name = "siangham"
        atk_type = "piercing"
    elif percentage_roll <= 84:
        base_value = 35
        name = "sword, bastard"
        atk_type = "slashing"
    elif percentage_roll <= 89:
        base_value = 10
        name = "sword, short"
        atk_type = "piercing"
    else:
        base_value = 30
        name = "dwarven waraxe"
        atk_type = "slashing"

    if magic:
        masterwork = True

    if masterwork:
        if double_weapon:
            base_value += 600
        else:
            base_value += 300

        if not magic:
            name = "%s, masterwork" % name

    dct_weapon["name"] = name
    dct_weapon["value"] = base_value
    dct_weapon["type"] = "melee"
    dct_weapon["atk_type"] = atk_type
    dct_weapon["mod"] = 0

    return dct_weapon


#-----------------------------------------------------------------------
#------ Generate Uncommon Weapons (Table 7-12, Page 222) ---------------
#-----------------------------------------------------------------------


def GetOneUncommonWep(masterwork=False, magic=False):
    # All values for weapons are in gold
    dct_weapon = {}

    double_weapon = False
    i_type = "melee"
    atk_type = ""

    percentage_roll = crDice.RollPercentage()[1]

    if percentage_roll <= 3:
        name = "axe, orc double"
        base_value = 60
        double_weapon = True
        atk_type = "slashing"
    elif percentage_roll <= 7:
        name = "battleaxe"
        base_value = 10
        atk_type = "slashing"
    elif percentage_roll <= 10:
        name = "chain, spiked"
        base_value = 25
        atk_type = "piercing"
    elif percentage_roll <= 12:
        name = "club"
        base_value = 0
        atk_type = "bludgeoning"
    elif percentage_roll <= 16:
        name = "crossbow, hand"
        base_value = 100
        i_type = "ranged"
        atk_type = "piercing"
    elif percentage_roll <= 19:
        name = "crossbow, repeating"
        base_value = 250
        i_type = "ranged"
        atk_type = "piercing"
    elif percentage_roll <= 21:
        name = "dagger, punching"
        base_value = 2
        atk_type = "piercing"
    elif percentage_roll <= 23:
        name = "falchion"
        base_value = 75
        atk_type = "slashing"
    elif percentage_roll <= 26:
        name = "flail, dire"
        base_value = 90
        atk_type = "bludgeoning"
        double_weapon = True
    elif percentage_roll <= 31:
        name = "flail, heavy"
        base_value = 15
        atk_type = "bludgeoning"
    elif percentage_roll <= 35:
        name = "flail, light"
        base_value = 8
        atk_type = "bludgeoning"
    elif percentage_roll <= 37:
        name = "gauntlet"
        base_value = 2
        atk_type = "bludgeoning"
    elif percentage_roll <= 39:
        name = "gauntlet, spiked"
        base_value = 5
        atk_type = "piercing"
    elif percentage_roll <= 41:
        name = "glaive"
        base_value = 8
        atk_type = "slashing"
    elif percentage_roll <= 43:
        name = "greatclub"
        base_value = 5
        atk_type = "bludgeoning"
    elif percentage_roll <= 45:
        name = "guisarme"
        base_value = 9
        atk_type = "slashing"
    elif percentage_roll <= 48:
        name = "halberd"
        base_value = 10
        atk_type = "slashing, piercing"
    elif percentage_roll <= 51:
        name = "halfspear"
        base_value = 1
        atk_type = "piercing"
    elif percentage_roll <= 54:
        name = "hammer, gnome hooked"
        base_value = 20
        atk_type = "bludgeoning, piercing"
        double_weapon = True
    elif percentage_roll <= 56:
        name = "hammer, light"
        base_value = 1
        atk_type = "bludgeoning"
    elif percentage_roll <= 58:
        name = "handaxe"
        base_value = 6
        atk_type = "slashing"
    elif percentage_roll <= 61:
        name = "kukri"
        base_value = 8
        atk_type = "slashing"
    elif percentage_roll <= 64:
        name = "lance"
        base_value = 10
        atk_type = "piercing"
    elif percentage_roll <= 67:
        name = "longspear"
        base_value = 5
        atk_type = "piercing"
    elif percentage_roll <= 70:
        name = "morningstar"
        base_value = 8
        atk_type = "bludgeoning, piercing"
    elif percentage_roll <= 72:
        name = "net"
        base_value = 20
        i_type = "ranged"
    elif percentage_roll <= 74:
        name = "pick, heavy"
        base_value = 8
        atk_type = "piercing"
    elif percentage_roll <= 76:
        name = "pick, light"
        base_value = 4
        atk_type = "piercing"
    elif percentage_roll <= 78:
        name = "ranseur"
        base_value = 10
        atk_type = "piercing"
    elif percentage_roll <= 80:
        name = "sap"
        base_value = 1
        atk_type = "bludgeoning"
    elif percentage_roll <= 82:
        name = "scythe"
        base_value = 18
        atk_type = "slashing, piercing"
    elif percentage_roll <= 84:
        name = "shuriken"
        base_value = 1
        i_type = "ranged"
        atk_type = "piercing"
    elif percentage_roll <= 86:
        name = "sickle"
        base_value = 6
        atk_type = "slashing"
    elif percentage_roll <= 89:
        name = "sword, two-bladed"
        base_value = 100
        atk_type = "slashing"
        double_weapon = True
    elif percentage_roll <= 91:
        name = "trident"
        base_value = 15
        atk_type = "piercing"
    elif percentage_roll <= 94:
        name = "urgosh, dwarven"
        base_value = 50
        atk_type = "slashing, piercing"
        double_weapon = True
    elif percentage_roll <= 97:
        name = "warhammer"
        base_value = 12
        atk_type = "bludgeoning"
    else:
        name = "whip"
        base_value = 1
        atk_type = "slashing"

    if magic:
        masterwork = True

    if masterwork:
        if double_weapon:
            base_value += 600
        else:
            base_value += 300

        if not magic:
            name = "%s, masterwork" % name

    dct_weapon["name"] = name
    dct_weapon["value"] = base_value
    dct_weapon["type"] = i_type
    dct_weapon["atk_type"] = atk_type
    dct_weapon["mod"] = 0

    return dct_weapon


#-----------------------------------------------------------------------
#------ Generate Uncommon Ranged Weapons (Table 7-13, Page 223) --------
#-----------------------------------------------------------------------


def GetOneCommonRangedWep(masterwork=False, magic=False):
    # All values for weapons are in gold
    dct_weapon = {}

    atk_type = "piercing"

    percentage_roll_1 = crDice.RollPercentage()[1]

    if percentage_roll_1 <= 10:
        # Second Level Percentage Roll
        percentage_roll_2 = crDice.RollPercentage()[1]

        if percentage_roll_2 <= 50:
            name = "arrows (50)"
            atk_type = ""
            base_value = 50
        elif percentage_roll_2 <= 80:
            name = "bolts, crossbow (50)"
            atk_type = ""
            base_value = 50
        else:
            name = "bullets, sling (50)"
            atk_type = ""
            base_value = 50

    elif percentage_roll_1 <= 15:
        name = "axe, throwing"
        atk_type = "slashing"
        base_value = 8
    elif percentage_roll_1 <= 25:
        name = "crossbow, heavy"
        base_value = 50
    elif percentage_roll_1 <= 35:
        name = "crossbow, light"
        base_value = 35
    elif percentage_roll_1 <= 39:
        name = "dart"
        base_value = 1
    elif percentage_roll_1 <= 41:
        name = "javelin"
        base_value = 1
    elif percentage_roll_1 <= 46:
        name = "shortbow"
        base_value = 30
    elif percentage_roll_1 <= 51:
        name = "shortbow, composite"
        base_value = 75
    elif percentage_roll_1 <= 56:
        if masterwork:
            name = "shortbow, composite (+1 Str bonus)"
            base_value = 150
            magic = True
        else:
            name = "shortbow, composite"
            base_value = 75
    elif percentage_roll_1 <= 61:
        if masterwork:
            name = "shortbow, composite (+2 Str bonus)"
            base_value = 225
            magic = True
        else:
            name = "shortbow, composite"
            base_value = 75
    elif percentage_roll_1 <= 65:
        name = "sling"
        atk_type = "bludgeoning"
        base_value = 0
    elif percentage_roll_1 <= 75:
        name = "longbow"
        base_value = 75
    elif percentage_roll_1 <= 80:
        name = "longbow, composite"
        base_value = 100
    elif percentage_roll_1 <= 85:
        if masterwork:
            name = "longbow, composite (+1 Str bonus)"
            base_value = 200
            magic = True
        else:
            name = "longbow, composite"
            base_value = 100
    elif percentage_roll_1 <= 90:
        if masterwork:
            name = "longbow, composite (+2 Str bonus)"
            base_value = 300
            magic = True
        else:
            name = "longbow, composite"
            base_value = 100
    elif percentage_roll_1 <= 95:
        if masterwork:
            name = "longbow, composite (+3 Str bonus)"
            base_value = 400
            magic = True
        else:
            name = "longbow, composite"
            base_value = 100
    else:
        if masterwork:
            name = "longbow, composite (+4 Str bonus)"
            base_value = 500
            magic = True
        else:
            name = "longbow, composite"
            base_value = 100

    if magic:
        masterwork = True

    if masterwork:
        base_value += 300

        if not magic:
            name = "%s, masterwork" % name

    dct_weapon["name"] = name
    dct_weapon["value"] = base_value
    dct_weapon["type"] = "ranged"
    dct_weapon["atk_type"] = atk_type
    dct_weapon["mod"] = 0

    return dct_weapon


#-----------------------------------------------------------------------
#------ Generate Pre-Made Specific Weapons (Table 7-16, Page 227) ------
#-----------------------------------------------------------------------


def GetSpecificWeapon(m_type):
    dct_weapon = {}

    minor = False
    medium = False
    major = False

    if string.upper(m_type) == "MINOR": minor = True
    elif string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True

    i_type = "melee"

    percentage_roll = crDice.RollPercentage()[1]

    if percentage_roll <= 15 and minor:
        name = "sleep arrow"
        base_value = 132
        mod = 1
        i_type = "ranged"
        atk_type = ""
    elif percentage_roll <= 25 and minor:
        name = "screaming bolt"
        base_value = 267
        mod = 2
        i_type = "ranged"
        atk_type = ""
    elif percentage_roll <= 45 and minor:
        name = "silver dagger, masterwork"
        base_value = 322
        mod = 1
        atk_type = "slashing, piercing"
    elif percentage_roll <= 65 and minor:
        name = "cold iron longsword, masterwork"
        base_value = 330
        mod = 1
        atk_type = "slashing"
    elif (percentage_roll <= 75 and minor
    or percentage_roll <= 9 and medium):
        name = "javelin of lightning"
        base_value = 1500
        mod = 1
        i_type = "ranged"
        atk_type = "piercing"
    elif (percentage_roll <= 80 and minor
    or percentage_roll <= 15 and medium):
        name = "slaying arrow"
        base_value = 2282
        mod = 1
        i_type = "ranged"
        atk_type = ""
    elif (percentage_roll <= 90 and minor
    or percentage_roll <= 24 and medium):
        name = "adamantine dagger"
        base_value = 3002
        mod = 1
        atk_type = "slashing, piercing"
    elif (percentage_roll <= 100 and minor
    or percentage_roll <= 33 and medium):
        name = "adamantine battleaxe"
        base_value = 3010
        mod = 1
        atk_type = "slashing"
    elif percentage_roll <= 37 and medium:
        name = "slaying arrow, greater"
        base_value = 4057
        mod = 2
        i_type = "ranged"
        atk_type = ""
    elif percentage_roll <= 40 and medium:
        name = "shatterspike"
        base_value = 4315
        mod = 1
        atk_type = "slashing"
    elif percentage_roll <= 46 and medium:
        name = "dagger of venom"
        base_value = 8302
        mod = 1
        atk_type = "slashing, piercing"
    elif percentage_roll <= 51 and medium:
        name = "trident of warning"
        base_value = 10115
        mod = 2
        atk_type = "piercing"
    elif (percentage_roll <= 57 and medium
    or percentage_roll <= 4 and major):
        name = "assassin's dagger"
        base_value = 10302
        mod = 2
        atk_type = "slashing, piercing"
    elif (percentage_roll <= 62 and medium
    or percentage_roll <= 7 and major):
        name = "shifter's sorrow"
        base_value = 12780
        mod = 1
        atk_type = "slashing"
    elif (percentage_roll <= 66 and medium
    or percentage_roll <= 9 and major):
        name = "trident of fish command"
        base_value = 18650
        mod = 1
        atk_type = "piercing"
    elif (percentage_roll <= 74 and medium
    or percentage_roll <= 13 and major):
        name = "flame tongue"
        base_value = 20715
        mod = 1
        atk_type = "slashing"
    elif (percentage_roll <= 79 and medium
    or percentage_roll <= 17 and major):
        name = "luck blade (0 wishes)"
        base_value = 22060
        mod = 2
        atk_type = "piercing"
    elif (percentage_roll <= 86 and medium
    or percentage_roll <= 24 and major):
        name = "sword of subtlety"
        base_value = 22310
        mod = 1
        atk_type = "piercing"
    elif (percentage_roll <= 91 and medium
    or percentage_roll <= 31 and major):
        name = "sword of the planes"
        base_value = 22315
        mod = 1
        atk_type = "slashing"
    elif (percentage_roll <= 95 and medium
    or percentage_roll <= 37 and major):
        name = "nine lives stealer"
        base_value = 23057
        mod = 2
        atk_type = "slashing"
    elif (percentage_roll <= 98 and medium
    or percentage_roll <= 42 and major):
        name = "sword of life stealing"
        base_value = 25715
        mod = 2
        atk_type = "slashing"
    elif (percentage_roll <= 100 and medium
    or percentage_roll <= 46 and major):
        name = "oathbow"
        base_value = 25600
        mod = 2
        i_type = "ranged"
        atk_type = "piercing"
    elif percentage_roll <= 51 and major:
        name = "mace of terror"
        base_value = 38552
        mod = 2
        atk_type = "bludgeoning"
    elif percentage_roll <= 57 and major:
        name = "life-drinker"
        base_value = 40320
        mod = 1
        atk_type = "slashing"
    elif percentage_roll <= 62 and major:
        name = "sylvan scimitar"
        base_value = 47315
        mod = 3
        atk_type = "slashing"
    elif percentage_roll <= 67 and major:
        name = "rapier of puncturing"
        base_value = 50320
        mod = 2
        atk_type = "piercing"
    elif percentage_roll <= 73 and major:
        name = "sun blade"
        base_value = 50335
        mod = 2
        atk_type = "slashing"
    elif percentage_roll <= 79 and major:
        name = "frost brand"
        base_value = 54475
        mod = 3
        atk_type = "slashing"
    elif percentage_roll <= 84 and major:
        name = "dwarven thrower"
        base_value = 60312
        mod = 2
        atk_type = "bludgeoning"
    elif percentage_roll <= 91 and major:
        name = "luck blade (1 wish)"
        base_value = 62360
        mod = 2
        atk_type = "piercing"
    elif percentage_roll <= 95 and major:
        name = "mace of smiting"
        base_value = 75312
        mod = 3
        atk_type = "bludgeoning"
    elif percentage_roll <= 97 and major:
        name = "luck blade (2 wishes)"
        base_value = 102660
        mod = 2
        atk_type = "piercing"
    elif percentage_roll <= 99 and major:
        name = "holy avenger"
        base_value = 120630
        mod = 2
        atk_type = "slashing"
    elif percentage_roll <= 100 and major:
        name = "luck blade (3 wishes)"
        base_value = 142960
        mod = 2
        atk_type = "piercing"

    dct_weapon["name"] = name
    dct_weapon["value"] = base_value
    dct_weapon["mod"] = mod
    dct_weapon["type"] = i_type
    dct_weapon["atk_type"] = atk_type

    return dct_weapon


#-----------------------------------------------------------------------
#------ Weapon Special Abilities (Table 7-14/7-15, Page 223) -----------
#-----------------------------------------------------------------------


def GetDesignatedFoe():

    dct_foes = {
    5: "aberrations",
    9: "animals",
    16: "constructs",
    22: "dragons",
    27: "elementals",
    32: "fey",
    39: "giants",
    40: "humanoids, aquatic",
    42: "humanoids, dwarf",
    44: "humanoids, elf",
    45: "humanoids, gnoll",
    46: "humanoids, gnome",
    49: "humanoids, goblinoid",
    50: "humanoids, halfling",
    54: "humanoids, human",
    57: "humanoids, reptilian",
    60: "humanoids, orc",
    65: "magical beasts",
    70: "monstrous humanoids",
    72: "oozes",
    73: "outsiders, air",
    76: "outsiders, chaotic",
    77: "outsiders, earth",
    80: "outsiders, evil",
    81: "outsiders, fire",
    84: "outsiders, good",
    87: "outsiders, lawful",
    88: "outsiders, water",
    90: "plants",
    98: "undead",
    100: "vermin"
    }

    percentage_roll = crDice.RollPercentage()[1]

    for ref in sorted(dct_foes.keys()):
        if percentage_roll <= ref:
            name = "%s" % (dct_foes[ref])

            return name


def GetMeleeAbilities(m_type, weapon, dct_abilities=None):

    if not dct_abilities:
        dct_abilities = {"aligned": False}

    ability = None

    minor = False
    medium = False
    major = False

    if string.upper(m_type) == "MINOR": minor = True
    elif string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True


    while True:

        percentage_roll = crDice.RollPercentage()[1]

        if (percentage_roll <= 10 and minor
        or percentage_roll <= 6 and medium
        or percentage_roll <= 3 and major):
            ability = "bane vs. %s" % GetDesignatedFoe()
            value = "+1"
        elif (percentage_roll <= 17 and minor
        or percentage_roll <= 12 and medium):
            ability = "defending"
            value = "+1"
        elif (percentage_roll <= 27 and minor
        or percentage_roll <= 19 and medium
        or percentage_roll <= 6 and major):
            ability = "flaming"
            value = "+1"
        elif (percentage_roll <= 37 and minor
        or percentage_roll <= 26 and medium
        or percentage_roll <= 9 and major):
            ability = "frost"
            value = "+1"
        elif (percentage_roll <= 47 and minor
        or percentage_roll <= 33 and medium
        or percentage_roll <= 12 and major):
            ability = "shock"
            value = "+1"
        elif (percentage_roll <= 56 and minor
        or percentage_roll <= 38 and medium
        or percentage_roll <= 15 and major):
            ability = "ghost touch"
            value = "+1"
        elif (percentage_roll <= 67 and minor
        or percentage_roll <= 44 and medium):

            # Must be a piercing or slashing weapon
            if ("piercing" in weapon["atk_type"]
            or "slashing" in weapon["atk_type"]):
                ability = "keen"
                value = "+1"
            else:
                # Roll Again
                continue

        elif (percentage_roll <= 71 and minor
        or percentage_roll <= 48 and medium
        or percentage_roll <= 19 and major):
            ability = "ki focus"
            value = "+1"
        elif (percentage_roll <= 75 and minor
        or percentage_roll <= 50 and medium):
            ability = "merciful"
            value = "+1"
        elif (percentage_roll <= 82 and minor
        or percentage_roll <= 54 and medium
        or percentage_roll <= 21 and major):
            ability = "mighty cleaving"
            value = "+1"
        elif (percentage_roll <= 87 and minor
        or percentage_roll <= 59 and medium
        or percentage_roll <= 24 and major):
            ability = "spell storing"
            value = "+1"
        elif (percentage_roll <= 91 and minor
        or percentage_roll <= 63 and medium
        or percentage_roll <= 28 and major):
            ability = "throwing"
            value = "+1"
        elif (percentage_roll <= 95 and minor
        or percentage_roll <= 65 and medium
        or percentage_roll <= 32 and major):
            ability = "thundering"
            value = "+1"
        elif (percentage_roll <= 99 and minor
        or percentage_roll <= 69 and medium
        or percentage_roll <= 36 and major):
            ability = "vicious"
            value = "+1"
        elif (percentage_roll <= 72 and medium
        or percentage_roll <= 41 and major):

            # A weapon cannot have two alignment values
            if not dct_abilities["aligned"]:
                ability = "anarchic"
                value = "+2"
                dct_abilities["aligned"] = True
            else:
                # Roll Again
                continue

        elif (percentage_roll <= 75 and medium
        or percentage_roll <= 46 and major):

            # A weapon cannot have two alignment values
            if not dct_abilities["aligned"]:
                ability = "axiomatic"
                value = "+2"
                dct_abilities["aligned"] = True
            else:
                # Roll Again
                continue

        elif (percentage_roll <= 78 and medium
        or percentage_roll <= 49 and major):

            # Must be a bludgeoning weapon
            if "bludgeoning" in weapon["atk_type"]:
                ability = "disruption"
                value = "+2"
            else:
                # Roll Again
                continue

        elif (percentage_roll <= 81 and medium
        or percentage_roll <= 54 and major):
            ability = "flaming burst"
            value = "+2"
        elif (percentage_roll <= 84 and medium
        or percentage_roll <= 59 and major):
            ability = "icy burst"
            value = "+2"
        elif (percentage_roll <= 87 and medium
        or percentage_roll <= 64 and major):

            # A weapon cannot have two alignment values
            if not dct_abilities["aligned"]:
                ability = "holy"
                value = "+2"
                dct_abilities["aligned"] = True
            else:
                # Roll Again
                continue

        elif (percentage_roll <= 90 and medium
        or percentage_roll <= 69 and major):
            ability = "shocking burst"
            value = "+2"
        elif (percentage_roll <= 93 and medium
        or percentage_roll <= 74 and major):

            # A weapon cannot have two alignment values
            if not dct_abilities["aligned"]:
                ability = "unholy"
                value = "+2"
                dct_abilities["aligned"] = True
            else:
                # Roll Again
                continue

        elif (percentage_roll <= 95 and medium
        or percentage_roll <= 78 and major):
            ability = "wounding"
            value = "+2"
        elif percentage_roll <= 83 and major:
            ability = "speed"
            value = "+3"
        elif percentage_roll <= 86 and major:
            ability = "brilliant energy"
            value = "+4"
        elif percentage_roll <= 88 and major:
            ability = "dancing"
            value = "+4"
        elif percentage_roll <= 90 and major:

            # Must be a piercing or slashing weapon
            if ("piercing" in weapon["atk_type"]
            or "slashing" in weapon["atk_type"]):
                ability = "vorpal"
                value = "+5"
            else:
                # Roll Again
                continue

        elif (percentage_roll <= 100 and minor
        or percentage_roll <= 100 and medium
        or percentage_roll <= 100 and major):
            # Break out of loop, so that recursion call can be made
            break


        # Do not allow an ability to be added if it takes the total
        # item mod/enhancement value above +10
        total_mods = 0
        for abil in dct_abilities.keys():

            # Skip the aligned bool key
            if abil != "aligned":
                total_mods += int(dct_abilities[abil]["value"][0:])


        # If abilities dct is full up to 10,
        # stop rolling and just return the dct
        if (int(value[0:]) + total_mods + weapon["mod"]) > 10:
            return dct_abilities


        if ability and not dct_abilities.has_key(ability):
            dct_abilities[ability] = {}
            dct_abilities[ability]["value"] = value
            break
        else:
            # Roll Again if ability already exists
            continue


    # Roll twice
    if (percentage_roll > 99 and percentage_roll <= 100 and minor
    or percentage_roll > 95 and percentage_roll <= 100 and medium
    or percentage_roll > 90 and percentage_roll <= 100 and major):
        for x in xrange(2):
            GetMeleeAbilities(m_type, weapon, dct_abilities)


    return dct_abilities


def GetRangedAbilities(m_type, weapon, dct_abilities=None):

    if not dct_abilities:
        dct_abilities = {"aligned": False}

    ability = None

    minor = False
    medium = False
    major = False

    if string.upper(m_type) == "MINOR": minor = True
    elif string.upper(m_type) == "MEDIUM": medium = True
    elif string.upper(m_type) == "MAJOR": major = True


    while True:

        percentage_roll = crDice.RollPercentage()[1]

        if (percentage_roll <= 12 and minor
        or percentage_roll <= 8 and medium
        or percentage_roll <= 4 and major):
            ability = "bane vs. %s" % GetDesignatedFoe()
            value = "+1"
        elif (percentage_roll <= 25 and minor
        or percentage_roll <= 16 and medium
        or percentage_roll <= 8 and major):
            ability = "distance"
            value = "+1"
        elif (percentage_roll <= 40 and minor
        or percentage_roll <= 28 and medium
        or percentage_roll <= 12 and major):
            ability = "flaming"
            value = "+1"
        elif (percentage_roll <= 55 and minor
        or percentage_roll <= 40 and medium
        or percentage_roll <= 16 and major):
            ability = "frost"
            value = "+1"
        elif (percentage_roll <= 60 and minor
        or percentage_roll <= 42 and medium):
            ability = "merciful"
            value = "+1"
        elif (percentage_roll <= 68 and minor
        or percentage_roll <= 47 and medium
        or percentage_roll <= 21 and major):
            ability = "returning"
            value = "+1"
        elif (percentage_roll <= 83 and minor
        or percentage_roll <= 59 and medium
        or percentage_roll <= 25 and major):
            ability = "shock"
            value = "+1"
        elif (percentage_roll <= 93 and minor
        or percentage_roll <= 64 and medium
        or percentage_roll <= 27 and major):
            ability = "seeking"
            value = "+1"
        elif (percentage_roll <= 99 and minor
        or percentage_roll <= 68 and medium
        or percentage_roll <= 29 and major):
            ability = "thundering"
            value = "+1"
        elif (percentage_roll <= 71 and medium
        or percentage_roll <= 34 and major):

            # A weapon cannot have two alignment values
            if not dct_abilities["aligned"]:
                ability = "anarchic"
                value = "+2"
                dct_abilities["aligned"] = True
            else:
                # Roll Again
                continue

        elif (percentage_roll <= 74 and medium
        or percentage_roll <= 39 and major):

            # A weapon cannot have two alignment values
            if not dct_abilities["aligned"]:
                ability = "axiomatic"
                value = "+2"
                dct_abilities["aligned"] = True
            else:
                # Roll Again
                continue

        elif (percentage_roll <= 79 and medium
        or percentage_roll <= 49 and major):
            ability = "flaming burst"
            value = "+2"
        elif (percentage_roll <= 82 and medium
        or percentage_roll <= 54 and major):

            # A weapon cannot have two alignment values
            if not dct_abilities["aligned"]:
                ability = "holy"
                value = "+2"
                dct_abilities["aligned"] = True
            else:
                # Roll Again
                continue

        elif (percentage_roll <= 87 and medium
        or percentage_roll <= 64 and major):
            ability = "icy burst"
            value = "+2"
        elif (percentage_roll <= 92 and medium
        or percentage_roll <= 74 and major):
            ability = "shocking burst"
            value = "+2"
        elif (percentage_roll <= 95 and medium
        or percentage_roll <= 79 and major):

            # A weapon cannot have two alignment values
            if not dct_abilities["aligned"]:
                ability = "unholy"
                value = "+2"
                dct_abilities["aligned"] = True
            else:
                # Roll Again
                continue

        elif percentage_roll <= 84 and major:
            ability = "speed"
            value = "+3"
        elif percentage_roll <= 90 and major:
            ability = "brilliant energy"
            value = "+4"
        elif (percentage_roll <= 100 and minor
        or percentage_roll <= 100 and medium
        or percentage_roll <= 100 and major):
            # Break out of loop, so that recursion call can be made
            break


        # Do not allow an ability to be added if it takes the total
        # item mod/enhancement value above +10
        total_mods = 0
        for abil in dct_abilities.keys():

            # Skip the aligned bool key
            if abil != "aligned":
                total_mods += int(dct_abilities[abil]["value"][0:])


        # If abilities dct is full up to 10,
        # stop rolling and just return the dct
        if (int(value[0:]) + total_mods + weapon["mod"]) > 10:
            return dct_abilities


        if ability and not dct_abilities.has_key(ability):
            dct_abilities[ability] = {}
            dct_abilities[ability]["value"] = value
            break
        else:
            # Roll Again if ability already exists
            continue


    # Roll twice
    if (percentage_roll > 99 and percentage_roll <= 100 and minor
    or percentage_roll > 95 and percentage_roll <= 100 and medium
    or percentage_roll > 90 and percentage_roll <= 100 and major):
        for x in xrange(2):
            GetRangedAbilities(m_type, weapon, dct_abilities)


    return dct_abilities


#-----------------------------------------------------------------------
#------ Generate One Magic Weapon (Table 7-9 pg. 222) ------------------
#-----------------------------------------------------------------------


def GetOneMagicWeapon(m_type):

    dct_weapon = {}

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

        if (percentage_roll <= 70 and minor
        or percentage_roll <= 10 and medium):
            mod = 1
        elif (percentage_roll <= 85 and minor
        or percentage_roll <= 29  and medium):
            mod = 2
        elif (percentage_roll <= 58 and medium
        or percentage_roll <= 20  and major):
            mod = 3
        elif (percentage_roll <= 62 and medium
        or percentage_roll <= 38  and major):
            mod = 4
        elif percentage_roll <= 49  and major:
            mod = 5
        elif (percentage_roll <= 90 and minor
        or percentage_roll <= 68 and medium
        or percentage_roll <= 63 and major):
            specific = True
        elif (percentage_roll <= 100 and minor
        or percentage_roll <= 100 and medium
        or percentage_roll <= 100 and major):
            special_abilities_count += 1
            continue

        if specific:

            weapon = GetSpecificWeapon(m_type)
            name = weapon["name"]
            base_value = weapon["value"]
            mod = 0

            break

        else:
            weapon = GetWeaponType(magic=True)
            weapon["mod"] += mod
            name = "%s +%d" % (weapon["name"], mod)
            base_value = weapon["value"]
            i_type = weapon["type"]


        # Generate appropriate abilities
        # based upon if the final weapon is melee or ranged
        for x in xrange(special_abilities_count):
            if not dct_abilities:
                if i_type == "melee":
                    dct_abilities = GetMeleeAbilities(m_type, weapon)
                elif i_type == "ranged":
                    dct_abilities = GetRangedAbilities(m_type, weapon)
            else:
                if i_type == "melee":
                    GetMeleeAbilities(m_type, weapon, dct_abilities)
                elif i_type == "ranged":
                    GetRangedAbilities(m_type, weapon, dct_abilities)


        if dct_abilities:

            if len(dct_abilities.keys()) > 2:
                ability_str += " - w/abilities ("
            else:
                ability_str += " - w/ability ("

            for ability in dct_abilities.keys():

                # skip the "aligned" bool key
                if ability != "aligned":
                    # Add effective bonus to mod for value purposes.
                    mod += int(dct_abilities[ability]["value"][0:])

                    ability_str += '%s; ' % ability

            ability_str = "%s)" % ability_str[:-2]

        break

    name += ability_str
    base_value += ((mod**2) * 2000)

    dct_weapon["name"] = name
    dct_weapon["value"] = base_value

    return dct_weapon


#***********************************************************************

if __name__ == "__main__":
    crawler.Main()
