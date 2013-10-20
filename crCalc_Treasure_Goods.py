#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Treasure Generators for Crawler I
#  by Brock Glaze
#
#  crCalc_Treasure_Goods.py


import crawler
import crDice
import random
import string
import wx


#-----------------------------------------------------------------------
#------ Generate Gems (Table 3-6, Page 55) -----------------------------
#-----------------------------------------------------------------------


def GetOneGem():
    # All values for gems are in gold
    dct_gem = {}

    percentage_roll = crDice.RollPercentage()[1]

    if percentage_roll <= 25:
        lst_gems = ["banded agate", "eye agate", "moss agate",
                    "azurite", "blue quartz", "hematite",
                    "lapis lazuli", "malachite", "obsidian",
                    "rhodochrosite", "tiger eye turquoise",
                    "freshwater (irregular) pearl"]
        random.shuffle(lst_gems)
        dct_gem["name"] = lst_gems[0]
        dct_gem["value"] = crDice.RollDice(4, 4)[1]

    elif percentage_roll <= 50:
        lst_gems = ["bloodstone", "carnelian", "chalcedony",
                    "chrysoprase" "citrine", "iolite",
                    "jasper", "moonstone", "onyx", "peridot",
                    "rock crystal (clear quartz)", "sard",
                    "sardonyx", "rose quartz", "smoky quartz",
                    "star rose quartz", "zircon"]
        random.shuffle(lst_gems)
        dct_gem["name"] = lst_gems[0]
        dct_gem["value"] = (crDice.RollDice(2, 4)[1] * 10)

    elif percentage_roll <= 70:
        lst_gems = ["amber", "amethyst", "chrysoberyl", "coral",
                    "red garnet", "brown-green garnet", "jade",
                    "jet", "white pearl", "golden pearl",
                    "pink pearl", "silver pearl", "red spinel",
                    "red-brown spinel", "deep green spinel",
                    "tourmaline"]
        random.shuffle(lst_gems)
        dct_gem["name"] = lst_gems[0]
        dct_gem["value"] = (crDice.RollDice(4, 4)[1] * 10)

    elif percentage_roll <= 90:
        lst_gems = ["alexandrite", "aquamarine", "violet",
                    "garnet", "black pearl", "deep blue spinel",
                    "golden yellow topaz"]
        random.shuffle(lst_gems)
        dct_gem["name"] = lst_gems[0]
        dct_gem["value"] = (crDice.RollDice(2, 4)[1] * 100)

    elif percentage_roll <= 99:
        lst_gems = ["emerald", "white opal", "black opal",
                    "fire opal", "blue sapphire",
                    "fiery yellow corundum", "rich purple corundum",
                    "blue star sapphire", "black star sapphire",
                    "star ruby"]
        random.shuffle(lst_gems)
        dct_gem["name"] = lst_gems[0]
        dct_gem["value"] = (crDice.RollDice(4, 4)[1] * 100)

    else:
        lst_gems = ["clearest bright green emerald",
                    "blue-white diamond", "canary diamond",
                    "pink diamond", "brown diamond", "blue diamond",
                    "jacinth"]
        random.shuffle(lst_gems)
        dct_gem["name"] = lst_gems[0]
        dct_gem["value"] = (crDice.RollDice(2, 4)[1] * 1000)

    return dct_gem


#-----------------------------------------------------------------------
#------ Generate Art (Table 3-7, Page 55) ------------------------------
#-----------------------------------------------------------------------


def GetOneArt():
    # All values for art are in gold
    dct_art = {}

    percentage_roll = crDice.RollPercentage()[1]

    if percentage_roll <= 10:
        lst_art = [("silver ewer", [
                   ("small", 1, 4), ("medium", 5, 12), ("large", 13, 30)
                   ]),

                   ("carved bone statuette", [
                   ("small", 0, 1), ("medium", 2, 3)
                   ]),

                   ("carved ivory statuette", [
                   ("small", 0, 1), ("medium", 2, 3)
                   ]),

                   ("finely wrought gold bracelet", [
                   ("small", 0, 1)
                   ])

                   ]

        value = (crDice.RollDice(1, 10)[1] * 10)

    elif percentage_roll <= 25:
        lst_art = [("cloth of gold vestments", [
                   ("small", 1, 1)
                   ]),

                   ("black velvet mask with numerous citrines", [
                   ("small", 0, 0)
                   ]),

                   ("silver chalice with lapis lazuli gems", [
                   ("small", 1, 1)
                   ])

                   ]
        value = (crDice.RollDice(3, 6)[1] * 10)

    elif percentage_roll <= 40:
        lst_art = [("well-done wool tapestry", [
                   ("medium", 1, 3), ("large", 4, 7)
                   ]),

                   ("brass mug with jade inlays", [
                   ("small", 1, 2)
                   ])

                   ]
        value = (crDice.RollDice(1, 6)[1] * 100)

    elif percentage_roll <= 50:
        lst_art = [("silver comb with moonstones", [
                   ("small", 0, 0)
                   ]),

                   ("silver-plated steel longsword with "
                    "jet jewel in hilt", [
                   ("medium", 4, 6)
                   ])

                   ]
        value = (crDice.RollDice(1, 10)[1] * 100)

    elif percentage_roll <= 60:
        lst_art = [("carved harp of exotic wood with "
                    "ivory inlay and zircon gems", [
                   ("small", 12, 30), ("medium", 35, 65), ("large", 70, 95)
                   ]),

                   ("solid gold idol", [
                   ("medium", 10, 10)
                   ])

                   ]
        value = (crDice.RollDice(2, 6)[1] * 100)

    elif percentage_roll <= 70:
        lst_art = [("gold dragon comb with red garnet eye", [
                   ("small", 0, 0)
                   ]),

                   ("gold and topaz bottle stopper cork", [
                   ("small", 0, 0)
                   ]),

                   ("ceremonial electrum dagger with "
                   "a star ruby in the pommel", [
                   ("small", 1, 2)
                   ])

                   ]
        value = (crDice.RollDice(3, 6)[1] * 100)

    elif percentage_roll <= 80:
        lst_art = [("eyepatch with mock eye of sapphire and moonstone", [
                   ("small", 0, 0)
                   ]),

                   ("fire opal pendant on a fine gold chain", [
                   ("small", 0, 0)
                   ]),

                   ("old masterpiece painting", [
                   ("medium", 3, 8), ("large", 9, 20), ("very large", 25, 65)
                   ])

                   ]
        value = (crDice.RollDice(4, 6)[1] * 100)

    elif percentage_roll <= 85:
        lst_art = [("embroidered silk and velvet mantle with "
                   "numerous moonstones", [
                   ("small", 0, 1)
                   ]),

                   ("sapphire pendant on gold chain", [
                   ("small", 0, 0)
                   ])

                   ]
        value = (crDice.RollDice(5, 6)[1] * 100)

    elif percentage_roll <= 90:
        lst_art = [("embroidered and bejeweled glove", [
                   ("small", 0, 0),
                   ]),

                   ("jeweled anklet", [
                   ("small", 0, 0)
                   ]),

                   ("gold music box", [
                   ("small", 2, 5), ("medium", 8, 13)
                   ])

                   ]
        value = (crDice.RollDice(1, 4)[1] * 1000)

    elif percentage_roll <= 95:
        lst_art = [("golden circlet with four aquamarines", [
                   ("small", 0, 1)
                   ]),
                   
                   ("a string of pink pearls (necklace)", [
                   ("small", 0, 0)
                   ])

                   ]
        value = (crDice.RollDice(1, 6)[1] * 1000)

    elif percentage_roll <= 99:
        lst_art = [("jeweled gold crown", [
                   ("small", 0, 1)
                   ]),

                   ("jeweled electrum ring", [
                   ("small", 0, 0)
                   ])

                   ]
        value = (crDice.RollDice(2, 4)[1] * 1000)

    elif percentage_roll <= 100:
        lst_art = [("gold and ruby ring", [
                   ("small", 0, 0)
                   ]),

                   ("gold cup set with emeralds", [
                   ("small", 1, 1)
                   ])

                   ]
        value = (crDice.RollDice(2, 6)[1] * 1000)

    random.shuffle(lst_art)
    art = lst_art[0]
    lst_size = art[1]
    random.shuffle(lst_size)

    # Art Name, Size, and Weight
    name = art[0]
    size = lst_size[0][0]
    weight = random.randint(lst_size[0][1], lst_size[0][2])

    name += " (%s, %d" % (size, weight)
    if weight == 1:
        name += " lb)"
    else:
        name += " lbs)"

    dct_art["name"] = name
    dct_art["value"] = value

    return dct_art


#-----------------------------------------------------------------------
#------ Generate One Random Good ---------------------------------------
#-----------------------------------------------------------------------

def GetOneGood(m_type):
    gem = False
    art = False

    if string.upper(m_type) == "GEM": gem = True
    elif string.upper(m_type) == "ART": art = True

    if gem:
        return GetOneGem()
    elif art:
        return GetOneArt()


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
