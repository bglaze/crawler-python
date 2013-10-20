#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Treasure Generators for Crawler I
#  by Brock Glaze
#
#  crCalc_Treasure_Mundane.py


import crawler
import crCalc_Treasure_Weapons as weapon_lib
import crDice
import string
import wx


#-----------------------------------------------------------------------
#------ Generate One Mundane Item (Table 3-8, Page 56) -----------------
#-----------------------------------------------------------------------


def GetOneMundane():
    # All values for items are in gold
    dct_mundane = {}

    percentage_roll_1 = crDice.RollPercentage()[1]

    # First Tier of Gear
    if percentage_roll_1 <= 17:
        # Second Level Percentage Roll
        percentage_roll_2 = crDice.RollPercentage()[1]

        if percentage_roll_2 <= 12:
            base_value = 20
            how_many = crDice.RollDice(1, 4)[1]
            name = "alchemist's fire (%d flasks)" % how_many
            if how_many < 2: name = name[:-2] + ")"
        elif percentage_roll_2 <= 24:
            base_value = 10
            how_many = crDice.RollDice(2, 4)[1]
            name = "acid (%d flasks)" % how_many
        elif percentage_roll_2 <= 36:
            base_value = 20
            how_many = crDice.RollDice(1, 4)[1]
            name = "smokesticks (%d sticks)" % how_many
            if how_many < 2: name = name[:-2] + ")"
        elif percentage_roll_2 <= 48:
            base_value = 25
            how_many = crDice.RollDice(1, 4)[1]
            name = "holy water (%d flasks)" % how_many
            if how_many < 2: name = name[:-2] + ")"
        elif percentage_roll_2 <= 62:
            base_value = 50
            how_many = crDice.RollDice(1, 4)[1]
            name = "antitoxin (%d doses)" % how_many
            if how_many < 2: name = name[:-2] + ")"
        elif percentage_roll_2 <= 74:
            base_value = 50
            how_many = 1
            name = "everburning torch"
        elif percentage_roll_2 <= 88:
            base_value = 50
            how_many = crDice.RollDice(1, 4)[1]
            name = "tanglefoot bags (%d bags)" % how_many
            if how_many < 2: name = name[:-2] + ")"
        elif percentage_roll_2 <= 100:
            base_value = 30
            how_many = crDice.RollDice(1, 4)[1]
            name = "thunderstones (%d stones)" % how_many
            if how_many < 2: name = name[:-2] + ")"

    # Second Tier of Gear
    elif percentage_roll_1 <= 50:
        # Second tier items only come in singles
        how_many = 1

        # Second Level Percentage Roll
        percentage_roll_2 = crDice.RollPercentage()[1]

        if percentage_roll_2 <= 12:
            base_value = 100
            name = "chain shirt"
        elif percentage_roll_2 <= 18:
            base_value = 175
            name = "studded leather, masterwork"
        elif percentage_roll_2 <= 26:
            base_value = 200
            name = "breastplate"
        elif percentage_roll_2 <= 34:
            base_value = 250
            name = "banded mail"
        elif percentage_roll_2 <= 54:
            base_value = 600
            name = "half-plate"
        elif percentage_roll_2 <= 80:
            base_value = 1500
            name = "full plate"
        elif percentage_roll_2 <= 90:

            # Third Level Percentage Roll
            percentage_roll_3 = crDice.RollPercentage()[1]

            if percentage_roll_3 <= 50:
                base_value = 205
                name = "darkwood buckler"
            else:
                base_value = 257
                name = "darkwood shield"

        else:
            # Third Level Percentage Roll
            percentage_roll_3 = crDice.RollPercentage()[1]

            if percentage_roll_3 <= 17:
                base_value = 165
                name = "buckler"
            elif percentage_roll_3 <= 40:
                base_value = 153
                name = "light wooden shield"
            elif percentage_roll_3 <= 60:
                base_value = 159
                name = "light steel shield"
            elif percentage_roll_3 <= 83:
                base_value = 157
                name = "heavy wooden shield"
            else:
                base_value = 170
                name = "heavy steel shield"

    # Third Tier of Gear
    elif percentage_roll_1 <= 83:
        # Third tier items only come in singles
        how_many = 1

        # Second Level Percentage Roll
        percentage_roll_2 = crDice.RollPercentage()[1]

        if percentage_roll_2 <= 50:
            item = weapon_lib.GetOneCommonMeleeWep(masterwork=True)
            base_value = item["value"]
            name = item["name"]

        elif percentage_roll_2 <= 70:
            item = weapon_lib.GetOneUncommonWep(masterwork=True)
            base_value = item["value"]
            name = item["name"]

        else:
            item = weapon_lib.GetOneCommonRangedWep(masterwork=True)
            base_value = item["value"]
            name = item["name"]

    # Fourth Tier of Gear
    else:
        # Fourth tier items only come in singles
        how_many = 1

        # Second Level Percentage Roll
        percentage_roll_2 = crDice.RollPercentage()[1]

        if percentage_roll_2 <= 3:
            base_value = 2
            name = "backpack (empty)"
        elif percentage_roll_2 <= 6:
            base_value = 2
            name = "crowbar"
        elif percentage_roll_2 <= 11:
            base_value = 12
            name = "lantern, bullseye"
        elif percentage_roll_2 <= 16:
            base_value = 20
            name = "lock, simple"
        elif percentage_roll_2 <= 21:
            base_value = 40
            name = "lock, average"
        elif percentage_roll_2 <= 28:
            base_value = 80
            name = "lock, good"
        elif percentage_roll_2 <= 35:
            base_value = 150
            name = "lock, superior"
        elif percentage_roll_2 <= 40:
            base_value = 50
            name = "manacles, masterwork"
        elif percentage_roll_2 <= 43:
            base_value = 10
            name = "small steel mirror"
        elif percentage_roll_2 <= 46:
            base_value = 10
            name = "silk rope (50ft)"
        elif percentage_roll_2 <= 53:
            base_value = 1000
            name = "spyglass"
        elif percentage_roll_2 <= 58:
            base_value = 55
            name = "artisan's tools, masterwork"
        elif percentage_roll_2 <= 63:
            base_value = 80
            name = "climber's kit"
        elif percentage_roll_2 <= 68:
            base_value = 50
            name = "disguise kit"
        elif percentage_roll_2 <= 73:
            base_value = 50
            name = "healer's kit"
        elif percentage_roll_2 <= 77:
            base_value = 25
            name = "holy symbol (silver)"
        elif percentage_roll_2 <= 81:
            base_value = 25
            name = "hourglass"
        elif percentage_roll_2 <= 88:
            base_value = 100
            name = "magnifying glass"
        elif percentage_roll_2 <= 95:
            base_value = 100
            name = "musical instrument, masterwork"
        else:
            base_value = 50
            name = "thieves' tools, masterwork"

    dct_mundane["name"] = name
    dct_mundane["value"] = (how_many * base_value)

    return dct_mundane


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
