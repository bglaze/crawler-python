#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Formulas for Crawler I
#  by Brock Glaze
#
#  crFormulas.py


import crawler
import math


def RoundOnePlace(x):
    return round(x * 10) / 10


def Log2(x):
    return 1.4426950408889633 * math.log(x)


def CRtoPL(x):
    i = 0
    if x < 2:
        i = x
    else:
        i = math.pow(2, (x / 2))
    return i


def PLtoCR(x):
    i = 0
    if x < 2:
        i = x
    else:
        i = 2 * math.log(x, 2)
    return i


def TotalPower(aLst):
    count = 0
    for i in aLst:
        count = count + i[0] * CRtoPL(i[1])
    return count


def TotalLevel(aLst):
    return PLtoCR(TotalPower(aLst))


def CountChars(aLst):
    count = 0
    for i in aLst:
        count = count + i[0]
    return count


def AveragePartyLevel(aLst):
    num_chars = CountChars(aLst)
    count = 0.0
    for i in aLst:
        count += i[0] * i[1]
    return count / num_chars


def FoeEffectiveLevel(aLst):
    return round(PLtoCR(TotalPower(aLst)))


# Original PartyEffectiveLevel
def PartyEffectiveLevel(aLst):
    return RoundOnePlace(PLtoCR(TotalPower(aLst) / 4))


# Experimental version of PartyEffectiveLevel
def PartyEffectiveLevel2(aLst):
    num_chars = CountChars(aLst)
    avg_lvl = AveragePartyLevel(aLst)
    
    if num_chars > 4:
        num_chars -= 4
        if num_chars % 2 != 0:
            num_chars -= 1

    return avg_lvl + num_chars / 2


def EvenUp(x):
    i = 2 * (int(x) / 2)
    if x < i:
        i += -2
    elif x > i:
        i += 2
    return i


#***********************************************************************


if __name__ == '__main__':
    crawler.Main()
    #~ monLst = [(3.0, 8.0), (4.0, 4.0)]
    #~ plrLst = [(2.0, 4.0), (3.0, 4.0)]
#~ 
    #~ effective_level = PartyEffectiveLevel2(plrLst)
    #~ monster_total_level = TotalLevel(monLst)
    #~ 
    #~ advice = DifficultyAdvice(GetDifficulty(plrLst, monLst))
    #~ percent = DifficultyPercent(GetDifficulty(plrLst, monLst))
    #~ print(
    #~ "Party Level:\t%s\n\n"
    #~ "Encounter Lvl:\t%s\n\n"
    #~ "Difficulty:\t%s, %s\n\n"
    #~ "%% of total:\t%s\n\n"
    #~ "%s\n\n" % (
#~ 
    #~ effective_level,
    #~ monster_total_level,
    #~ advice[0], advice[1],
    #~ percent,
    #~ GetTreasure(monLst)
    #~ ))
