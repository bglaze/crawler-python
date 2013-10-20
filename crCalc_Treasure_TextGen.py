#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Treasure Text Generator for Crawler I
#  by Brock Glaze
#
#  crCalc_Treasure_TextGen.py


import crawler
import crDice
import crCalc_Treasure_Goods as goods_lib
import crCalc_Treasure as treasure_lib
import math
import wx
import crFormulas


# Convert Choice Items into Fraction Multipliers
treasurePerc = [0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1, 2, 3, 4]


#-----------------------------------------------------------------------
#------ Generate Full Treasure (Table 3-5, Page 52-53) -----------------
#-----------------------------------------------------------------------


# Class to hold coins, goods, and items.
class treasureHold():
    def __init__(self):

        # Monster Specific Treasure Percentages
        self.coins_perc = None
        self.goods_perc = None
        self.items_perc = None

        # Total Treasure Values
        self.total_cp = 0
        self.total_sp = 0
        self.total_gp = 0
        self.total_pp = 0

        self.total_goods = {}
        self.total_goods["gem"] = []
        self.total_goods["art"] = []

        self.total_items = {}
        self.total_items["mundane"] = []
        self.total_items["minor"] = []
        self.total_items["medium"] = []
        self.total_items["major"] = []

        self.total_gold_value = 0

    def LenGoods(self):
        count = 0

        count += len(self.total_goods["gem"])
        count += len(self.total_goods["art"])

        return count

    def LenItems(self):
        count = 0

        count += len(self.total_items["mundane"])
        count += len(self.total_items["minor"])
        count += len(self.total_items["medium"])
        count += len(self.total_items["major"])

        return count

    def TotalCoins(self):
        total_coins = (self.total_cp +
                       self.total_sp +
                       self.total_gp +
                       self.total_pp)
        return total_coins


# Dictionary of stats to generate treasure per level from 1-20
dct_tr_lvl = {

1: {
"c_tier": (14, 29, 52, 95, 100),
"c_roll1": None,
"c_roll2": (1, 6, 1000),
"c_roll3": (1, 8, 100),
"c_roll4": (2, 8, 10),
"c_roll5": (1, 4, 10),

"g_tier": (90, 95, 100),
"g_roll1": None,
"g_roll2": (1, 1, "gem"),
"g_roll3": (1, 1, "art"),

"i_tier": (0, 71, 95, 100),
"i_roll1": None,
"i_roll2": None,
"i_roll3": (1, 1, "mundane"),
"i_roll4": (1, 1, "minor"),
},

2: {
"c_tier": (13, 23, 43, 95, 100),
"c_roll1": None,
"c_roll2": (1, 10, 1000),
"c_roll3": (2, 10, 100),
"c_roll4": (4, 10, 10),
"c_roll5": (2, 8, 10),

"g_tier": (81, 95, 100),
"g_roll1": None,
"g_roll2": (1, 3, "gem"),
"g_roll3": (1, 3, "art"),

"i_tier": (0, 49, 85, 100),
"i_roll1": None,
"i_roll2": None,
"i_roll3": (1, 1, "mundane"),
"i_roll4": (1, 1, "minor"),
},

3: {
"c_tier": (11, 21, 41, 95, 100),
"c_roll1": None,
"c_roll2": (2, 10, 1000),
"c_roll3": (4, 8, 100),
"c_roll4": (1, 4, 100),
"c_roll5": (1, 10, 10),

"g_tier": (77, 95, 100),
"g_roll1": None,
"g_roll2": (1, 3, "gem"),
"g_roll3": (1, 3, "art"),

"i_tier": (0, 49, 79, 100),
"i_roll1": None,
"i_roll2": None,
"i_roll3": (1, 3, "mundane"),
"i_roll4": (1, 1, "minor"),
},

4: {
"c_tier": (11, 21, 41, 95, 100),
"c_roll1": None,
"c_roll2": (3, 10, 1000),
"c_roll3": (4, 12, 1000),
"c_roll4": (1, 6, 100),
"c_roll5": (1, 8, 10),

"g_tier": (70, 95, 100),
"g_roll1": None,
"g_roll2": (1, 4, "gem"),
"g_roll3": (1, 3, "art"),

"i_tier": (0, 42, 79, 100),
"i_roll1": None,
"i_roll2": None,
"i_roll3": (1, 4, "mundane"),
"i_roll4": (1, 1, "minor"),
},

5: {
"c_tier": (10, 19, 38, 95, 100),
"c_roll1": None,
"c_roll2": (1, 4, 10000),
"c_roll3": (1, 6, 1000),
"c_roll4": (1, 8, 100),
"c_roll5": (1, 10, 10),

"g_tier": (60, 95, 100),
"g_roll1": None,
"g_roll2": (1, 4, "gem"),
"g_roll3": (1, 4, "art"),

"i_tier": (0, 57, 67, 100),
"i_roll1": None,
"i_roll2": None,
"i_roll3": (1, 4, "mundane"),
"i_roll4": (1, 3, "minor"),
},

6: {
"c_tier": (10, 18, 37, 95, 100),
"c_roll1": None,
"c_roll2": (1, 6, 10000),
"c_roll3": (1, 8, 1000),
"c_roll4": (1, 10, 100),
"c_roll5": (1, 12, 10),

"g_tier": (56, 92, 100),
"g_roll1": None,
"g_roll2": (1, 4, "gem"),
"g_roll3": (1, 4, "art"),

"i_tier": (54, 59, 99, 100),
"i_roll1": None,
"i_roll2": (1, 4, "mundane"),
"i_roll3": (1, 3, "minor"),
"i_roll4": (1, 1, "medium"),
},

7: {
"c_tier": (11, 18, 35, 93, 100),
"c_roll1": None,
"c_roll2": (1, 10, 10000),
"c_roll3": (1, 12, 1000),
"c_roll4": (2, 6, 100),
"c_roll5": (3, 4, 10),

"g_tier": (48, 88, 100),
"g_roll1": None,
"g_roll2": (1, 4, "gem"),
"g_roll3": (1, 4, "art"),

"i_tier": (0, 51, 97, 100),
"i_roll1": None,
"i_roll2": None,
"i_roll3": (1, 3, "minor"),
"i_roll4": (1, 1, "medium"),
},

8: {
"c_tier": (10, 15, 29, 85, 100),
"c_roll1": None,
"c_roll2": (1, 12, 10000),
"c_roll3": (2, 6, 1000),
"c_roll4": (2, 8, 100),
"c_roll5": (3, 6, 10),

"g_tier": (45, 85, 100),
"g_roll1": None,
"g_roll2": (1, 6, "gem"),
"g_roll3": (1, 4, "art"),

"i_tier": (0, 48, 96, 100),
"i_roll1": None,
"i_roll2": None,
"i_roll3": (1, 4, "minor"),
"i_roll4": (1, 1, "medium"),
},

9: {
"c_tier": (10, 15, 29, 85, 100),
"c_roll1": None,
"c_roll2": (2, 6, 10000),
"c_roll3": (2, 8, 1000),
"c_roll4": (5, 4, 100),
"c_roll5": (2, 12, 10),

"g_tier": (40, 80, 100),
"g_roll1": None,
"g_roll2": (1, 8, "gem"),
"g_roll3": (1, 4, "art"),

"i_tier": (0, 43, 91, 100),
"i_roll1": None,
"i_roll2": None,
"i_roll3": (1, 4, "minor"),
"i_roll4": (1, 1, "medium"),
},

10: {
"c_tier": (0, 10, 24, 79, 100),
"c_roll1": None,
"c_roll2": None,
"c_roll3": (2, 10, 1000),
"c_roll4": (6, 4, 100),
"c_roll5": (5, 6, 10),

"g_tier": (35, 79, 100),
"g_roll1": None,
"g_roll2": (1, 8, "gem"),
"g_roll3": (1, 6, "art"),

"i_tier": (40, 88, 99, 100),
"i_roll1": None,
"i_roll2": (1, 4, "minor"),
"i_roll3": (1, 1, "medium"),
"i_roll4": (1, 1, "major"),
},

11: {
"c_tier": (0, 8, 14, 75, 100),
"c_roll1": None,
"c_roll2": None,
"c_roll3": (3, 10, 1000),
"c_roll4": (4, 8, 100),
"c_roll5": (4, 10, 10),

"g_tier": (24, 74, 100),
"g_roll1": None,
"g_roll2": (1, 10, "gem"),
"g_roll3": (1, 6, "art"),

"i_tier": (31, 84, 98, 100),
"i_roll1": None,
"i_roll2": (1, 4, "minor"),
"i_roll3": (1, 1, "medium"),
"i_roll4": (1, 1, "major"),
},

12: {
"c_tier": (0, 8, 14, 75, 100),
"c_roll1": None,
"c_roll2": None,
"c_roll3": (3, 12, 1000),
"c_roll4": (1, 3, 1000),
"c_roll5": (1, 4, 100),

"g_tier": (17, 70, 100),
"g_roll1": None,
"g_roll2": (1, 10, "gem"),
"g_roll3": (1, 8, "art"),

"i_tier": (27, 82, 97, 100),
"i_roll1": None,
"i_roll2": (1, 6, "minor"),
"i_roll3": (1, 1, "medium"),
"i_roll4": (1, 1, "major"),
},

13: {
"c_tier": (0, 0, 8, 75, 100),
"c_roll1": None,
"c_roll2": None,
"c_roll3": None,
"c_roll4": (1, 4, 1000),
"c_roll5": (1, 10, 100),

"g_tier": (11, 66, 100),
"g_roll1": None,
"g_roll2": (1, 12, "gem"),
"g_roll3": (1, 10, "art"),

"i_tier": (19, 73, 95, 100),
"i_roll1": None,
"i_roll2": (1, 6, "minor"),
"i_roll3": (1, 1, "medium"),
"i_roll4": (1, 1, "major"),
},

14: {
"c_tier": (0, 0, 8, 75, 100),
"c_roll1": None,
"c_roll2": None,
"c_roll3": None,
"c_roll4": (1, 6, 1000),
"c_roll5": (1, 12, 100),

"g_tier": (11, 66, 100),
"g_roll1": None,
"g_roll2": (2, 8, "gem"),
"g_roll3": (2, 6, "art"),

"i_tier": (19, 58, 92, 100),
"i_roll1": None,
"i_roll2": (1, 6, "minor"),
"i_roll3": (1, 1, "medium"),
"i_roll4": (1, 1, "major"),
},

15: {
"c_tier": (0, 0, 3, 74, 100),
"c_roll1": None,
"c_roll2": None,
"c_roll3": None,
"c_roll4": (1, 8, 1000),
"c_roll5": (3, 4, 100),

"g_tier": (9, 65, 100),
"g_roll1": None,
"g_roll2": (2, 10, "gem"),
"g_roll3": (2, 8, "art"),

"i_tier": (11, 46, 90, 100),
"i_roll1": None,
"i_roll2": (1, 10, "minor"),
"i_roll3": (1, 1, "medium"),
"i_roll4": (1, 1, "major"),
},

16: {
"c_tier": (0, 0, 3, 74, 100),
"c_roll1": None,
"c_roll2": None,
"c_roll3": None,
"c_roll4": (1, 12, 1000),
"c_roll5": (3, 4, 100),

"g_tier": (7, 64, 100),
"g_roll1": None,
"g_roll2": (4, 6, "gem"),
"g_roll3": (2, 10, "art"),

"i_tier": (40, 46, 90, 100),
"i_roll1": None,
"i_roll2": (1, 10, "minor"),
"i_roll3": (1, 3, "medium"),
"i_roll4": (1, 1, "major"),
},

17: {
"c_tier": (0, 0, 3, 68, 100),
"c_roll1": None,
"c_roll2": None,
"c_roll3": None,
"c_roll4": (3, 4, 1000),
"c_roll5": (2, 10, 100),

"g_tier": (4, 63, 100),
"g_roll1": None,
"g_roll2": (4, 8, "gem"),
"g_roll3": (3, 8, "art"),

"i_tier": (0, 33, 83, 100),
"i_roll1": None,
"i_roll2": None,
"i_roll3": (1, 3, "medium"),
"i_roll4": (1, 1, "major"),
},

18: {
"c_tier": (0, 0, 2, 65, 100),
"c_roll1": None,
"c_roll2": None,
"c_roll3": None,
"c_roll4": (3, 6, 1000),
"c_roll5": (5, 4, 100),

"g_tier": (4, 54, 100),
"g_roll1": None,
"g_roll2": (3, 12, "gem"),
"g_roll3": (3, 10, "art"),

"i_tier": (0, 24, 80, 100),
"i_roll1": None,
"i_roll2": None,
"i_roll3": (1, 4, "medium"),
"i_roll4": (1, 1, "major"),
},

19: {
"c_tier": (0, 0, 2, 65, 100),
"c_roll1": None,
"c_roll2": None,
"c_roll3": None,
"c_roll4": (3, 8, 1000),
"c_roll5": (3, 10, 100),

"g_tier": (3, 50, 100),
"g_roll1": None,
"g_roll2": (6, 6, "gem"),
"g_roll3": (6, 6, "art"),

"i_tier": (0, 4, 70, 100),
"i_roll1": None,
"i_roll2": None,
"i_roll3": (1, 4, "medium"),
"i_roll4": (1, 1, "major"),
},

20: {
"c_tier": (0, 0, 2, 65, 100),
"c_roll1": None,
"c_roll2": None,
"c_roll3": None,
"c_roll4": (4, 8, 1000),
"c_roll5": (4, 10, 100),

"g_tier": (2, 38, 100),
"g_roll1": None,
"g_roll2": (4, 10, "gem"),
"g_roll3": (7, 6, "art"),

"i_tier": (0, 25, 65, 100),
"i_roll1": None,
"i_roll2": None,
"i_roll3": (1, 4, "medium"),
"i_roll4": (1, 3, "major"),
},

}


# Generate treasure for 1 level and
# store data in the treasureHold class
def TreasureLevel(lvl, tH):

    # Level Values Dictionary
    d = dct_tr_lvl


    RollPerc = crDice.RollPercentage
    RollDice = crDice.RollDice


    # Coins
    coins_tier1 = d[lvl]["c_tier"][0]
    coins_tier2 = d[lvl]["c_tier"][1]
    coins_tier3 = d[lvl]["c_tier"][2]
    coins_tier4 = d[lvl]["c_tier"][3]
    coins_tier5 = d[lvl]["c_tier"][4]

    # Assign percentage or "times to run" to coins
    coins_times = 1
    coins_perc = tH.coins_perc
    if tH.coins_perc >= 1:
        coins_perc = 1
        coins_times = tH.coins_perc

    for x in xrange(coins_times):

        coins_roll = RollPerc()[1]

        if coins_roll <= coins_tier1:
            pass

        elif coins_roll <= coins_tier2:
            if d[lvl]["c_roll2"]:
                amount = int(
                         math.floor(
                         (RollDice(
                         d[lvl]["c_roll2"][0],
                         d[lvl]["c_roll2"][1])[1] *
                         d[lvl]["c_roll2"][2]) * coins_perc
                         ))
                tH.total_cp += amount
                tH.total_gold_value += amount / 100

        elif coins_roll <= coins_tier3:
            if d[lvl]["c_roll3"]:
                amount = int(
                         math.floor(
                         (RollDice(
                         d[lvl]["c_roll3"][0],
                         d[lvl]["c_roll3"][1])[1] *
                         d[lvl]["c_roll3"][2]) * coins_perc
                         ))
                tH.total_sp += amount
                tH.total_gold_value += amount / 10

        elif coins_roll <= coins_tier4:
            if d[lvl]["c_roll4"]:
                amount = int(
                         math.floor(
                         (RollDice(
                         d[lvl]["c_roll4"][0],
                         d[lvl]["c_roll4"][1])[1] *
                         d[lvl]["c_roll4"][2]) * coins_perc
                         ))
                tH.total_gp += amount
                tH.total_gold_value += amount

        elif coins_roll <= coins_tier5:
            if d[lvl]["c_roll5"]:
                amount = int(
                         math.floor(
                         (RollDice(
                         d[lvl]["c_roll5"][0],
                         d[lvl]["c_roll5"][1])[1] *
                         d[lvl]["c_roll5"][2]) * tH.coins_perc
                         ))
                tH.total_pp += amount
                tH.total_gold_value += amount * 10


    # Goods
    goods_tier1 = d[lvl]["g_tier"][0]
    goods_tier2 = d[lvl]["g_tier"][1]
    goods_tier3 = d[lvl]["g_tier"][2]

    # Assign percentage or "times to run" to goods
    goods_times = 1
    goods_perc = tH.goods_perc
    if tH.goods_perc >= 1:
        goods_perc = 1
        goods_times = tH.goods_perc

    for x in xrange(goods_times):

        goods_roll = RollPerc()[1]

        if goods_roll <= goods_tier1:
            pass

        elif goods_roll <= goods_tier2:
            amount = int(
                     math.floor(
                     (RollDice(
                     d[lvl]["g_roll2"][0],
                     d[lvl]["g_roll2"][1])[1]) * goods_perc
                     ))
            for x in xrange(amount):
                good = goods_lib.GetOneGood(d[lvl]["g_roll2"][2])
                tH.total_goods[d[lvl]["g_roll2"][2]].append(good)
                tH.total_gold_value += good["value"]

        elif goods_roll <= goods_tier3:
            amount = int(
                     math.floor(
                     (RollDice(
                     d[lvl]["g_roll3"][0],
                     d[lvl]["g_roll3"][1])[1]) * goods_perc
                     ))
            for x in xrange(amount):
                good = goods_lib.GetOneGood(d[lvl]["g_roll3"][2])
                tH.total_goods[d[lvl]["g_roll3"][2]].append(good)
                tH.total_gold_value += good["value"]


    # Items
    items_tier1 = d[lvl]["i_tier"][0]
    items_tier2 = d[lvl]["i_tier"][1]
    items_tier3 = d[lvl]["i_tier"][2]
    items_tier4 = d[lvl]["i_tier"][3]

    # Assign percentage or "times to run" to coins
    items_times = 1
    items_perc = tH.items_perc
    if tH.items_perc >= 1:
        items_perc = 1
        items_times = tH.items_perc

    for x in xrange(items_times):

        items_roll = RollPerc()[1]

        if items_roll <= items_tier1:
            pass

        elif items_roll <= items_tier2:
            if d[lvl]["i_roll2"]:
                amount = int(
                         math.floor(
                         (RollDice(
                         d[lvl]["i_roll2"][0],
                         d[lvl]["i_roll2"][1])[1]) * items_perc
                         ))
                for x in xrange(amount):
                    item = treasure_lib.GetOneItem(d[lvl]["i_roll2"][2])
                    tH.total_items[d[lvl]["i_roll2"][2]].append(item)
                    tH.total_gold_value += item["value"]

        elif items_roll <= items_tier3:
            if d[lvl]["i_roll3"]:
                amount = int(
                         math.floor(
                         (RollDice(
                         d[lvl]["i_roll3"][0],
                         d[lvl]["i_roll3"][1])[1]) * items_perc
                         ))
                for x in xrange(amount):
                    item = treasure_lib.GetOneItem(d[lvl]["i_roll3"][2])
                    tH.total_items[d[lvl]["i_roll3"][2]].append(item)
                    tH.total_gold_value += item["value"]

        elif items_roll <= items_tier4:
            if d[lvl]["i_roll4"]:
                amount = int(
                         math.floor(
                         (RollDice(
                         d[lvl]["i_roll4"][0],
                         d[lvl]["i_roll4"][1])[1]) * items_perc
                         ))
                for x in xrange(amount):
                    item = treasure_lib.GetOneItem(d[lvl]["i_roll4"][2])
                    tH.total_items[d[lvl]["i_roll4"][2]].append(item)
                    tH.total_gold_value += item["value"]


# Initiate treasure generator for selected level and
# print it to the main text control
def FullTreasureTextulator(txt_affect, frame, monCtrlLst):


#-----------------------------------------------------------------------
#------ Master Treasure Hold (To compare others to) --------------------
#-----------------------------------------------------------------------


    master_tH = treasureHold()

    master_tH.coins_perc = treasurePerc[0]
    master_tH.goods_perc = treasurePerc[0]
    master_tH.items_perc = treasurePerc[0]

    # Find selected monster row, verify the fields are filled in,
    # and assign the int values to vars "Number" and "Level"
    monLst = []
    for t in monCtrlLst:
        if t[0].GetValue() and t[1].GetValue():

            lst_ratings = t[3]

            # Set treasure rating to the highest in the encounter
            if treasurePerc[lst_ratings[0]] > master_tH.coins_perc:
                master_tH.coins_perc = treasurePerc[lst_ratings[0]]
            if treasurePerc[lst_ratings[1]] > master_tH.goods_perc:
                master_tH.goods_perc = treasurePerc[lst_ratings[1]]
            if treasurePerc[lst_ratings[2]] > master_tH.items_perc:
                master_tH.items_perc = treasurePerc[lst_ratings[2]]

            monLst.append((float(t[0].GetValue()), float(t[1].GetValue())))
            master_EL = crFormulas.FoeEffectiveLevel(monLst)

            if master_EL < 1:
                master_EL = 1
            elif master_EL > 20:
                master_EL = 20

    # Assign all the items and values to master_tH
    TreasureLevel(master_EL, master_tH)


#-----------------------------------------------------------------------
#------ All Monsters Treasure Hold (To compare Master) -----------------
#-----------------------------------------------------------------------


    tH = treasureHold()

    # Find selected monster row, verify the fields are filled in,
    # and assign the int values to vars "Number" and "Level"
    mon_count = 0
    for t in monCtrlLst:
        if t[0].GetValue() and t[1].GetValue():
            for x in xrange(int(t[0].GetValue())):

                mon_count += 1

                lst_ratings = t[3]

                tH.coins_perc = treasurePerc[lst_ratings[0]]
                tH.goods_perc = treasurePerc[lst_ratings[1]]
                tH.items_perc = treasurePerc[lst_ratings[2]]

                monLst = [(1.0, float(t[1].GetValue()))]
                EL = crFormulas.FoeEffectiveLevel(monLst)

                if EL < 1:
                    EL = 1
                elif EL > 20:
                    EL = 20

                TreasureLevel(EL, tH)


    # If master TreasureHold has nothing, don't even bother
    if master_tH.total_gold_value == 0 or mon_count == 1:
        tH = master_tH

    else:

        # Kind of a voodoo way to keep
        # average values even across the board
        m_tH_multipler = 4.5 - ((mon_count * .095) + (EL * .15))
        m_tH_total_gold = (master_tH.total_gold_value * m_tH_multipler)


        # Set total coins to same as master (but keeping diversity)
        while tH.TotalCoins() > master_tH.TotalCoins():

            if tH.total_gold_value > m_tH_total_gold:

                # Old calculation
                #~ neg_percentage = (100 / mon_count) * .010

                if tH.total_cp:
                    tH.total_cp -= 100
                    tH.total_gold_value -= 1

                elif tH.total_sp:
                    tH.total_sp -= 10
                    tH.total_gold_value -= 1

                elif tH.total_gp:
                    tH.total_gp -= 1
                    tH.total_gold_value -= 1

                elif tH.total_pp:
                    tH.total_pp -= 1
                    tH.total_gold_value -= 10

            else:
                break


        # Set total goods to same as master (but keeping diversity)
        current_item = "gem"
        while tH.LenGoods() > master_tH.LenGoods():

            if tH.total_gold_value > m_tH_total_gold:

                if current_item == "gem":
                    neg_list = tH.total_goods["gem"]
                    current_item = "art"

                elif current_item == "art":
                    neg_list = tH.total_goods["art"]
                    current_item = "gem"

                if neg_list:
                    neg_item = neg_list.pop(-1)
                    tH.total_gold_value -= neg_item["value"]

            else:
                break


        # Set total items to same as master (but keeping diversity)
        current_item = "mundane"
        while tH.LenItems() > master_tH.LenItems():

            if tH.total_gold_value > m_tH_total_gold:

                if current_item == "mundane":
                    neg_list = tH.total_items["mundane"]
                    current_item = "minor"

                elif current_item == "minor":
                    neg_list = tH.total_items["minor"]
                    current_item = "medium"

                elif current_item == "medium":
                    neg_list = tH.total_items["medium"]
                    current_item = "major"

                elif current_item == "major":
                    neg_list = tH.total_items["major"]
                    current_item = "mundane"

                if neg_list:
                    neg_item = neg_list.pop(-1)
                    tH.total_gold_value -= neg_item["value"]

            else:
                break


#-----------------------------------------------------------------------
#------ Print Treasure -------------------------------------------------
#-----------------------------------------------------------------------


    if frame.menu_options.IsChecked(frame.ID_CLEAR_TEXT):
        txt_affect.Clear()

    Found_Loot = False

    new_line = "\n"
    if txt_affect.GetValue() == "":
        new_line = ""

    text = (
    "%s:::: Generated Treasure for "
    "Encounter Level %d ::::" % (new_line, master_EL)
    )

    if tH.total_cp or tH.total_sp or tH.total_gp or tH.total_pp:

        text += "\n\n-- Coins --"
        Found_Loot = True

        if tH.total_pp: text += "\n%dpp" % tH.total_pp
        if tH.total_gp: text += "\n%dgp" % tH.total_gp
        if tH.total_sp: text += "\n%dsp" % tH.total_sp
        if tH.total_cp: text += "\n%dcp" % tH.total_cp


    if tH.total_goods["gem"] or tH.total_goods["art"]:

        text += "\n\n-- Goods --"
        Found_Loot = True

        if tH.total_goods["gem"]:
            for gem in tH.total_goods["gem"]:
                text += (
                "\n%s (%sg)" %
                (gem["name"], gem["value"])
                )

        if tH.total_goods["art"]:
            for art in tH.total_goods["art"]:
                text += (
                "\n%s (%sg)" %
                (art["name"], art["value"])
                )

    if (tH.total_items["mundane"] or tH.total_items["minor"]
    or tH.total_items["medium"] or tH.total_items["major"]):

        text += "\n\n-- Items --"
        Found_Loot = True

        if tH.total_items["mundane"]:
            for mundane in tH.total_items["mundane"]:
                text += (
                "\n%s (%sg)" %
                (mundane["name"], mundane["value"])
                )

        if tH.total_items["minor"]:
            for minor in tH.total_items["minor"]:
                text += (
                "\n%s (%sg)" %
                (minor["name"], minor["value"])
                )

        if tH.total_items["medium"]:
            for medium in tH.total_items["medium"]:
                text += (
                "\n%s (%sg)" %
                (medium["name"], medium["value"])
                )

        if tH.total_items["major"]:
            for major in tH.total_items["major"]:
                text += (
                "\n%s (%sg)" %
                (major["name"], major["value"])
                )

    if not Found_Loot:
        text += "\n\n-- Nothing --"

    text += "\n\nTotal Value: %dgp\n" % tH.total_gold_value

    txt_affect.DoAppendText(text)

    return tH.total_gold_value


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
