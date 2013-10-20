#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Difficulty Calculator for Crawler I
#  by Brock Glaze
#
#  crCalc_Difficulty.py


import crawler
import wx
import crFormulas


set_challenging = 2 # 0 (Standard)


# Difficulty Ratings and Advice
def DifficultyAdvice(x):
    mobPower = ('Unknown', 'Unknown')
    if x < -9: # x < -9 (Standard)
        mobPower = ('Trivial', 'this would be a waste of time.')
    elif x < -4: # x < -4 (Standard)
        mobPower = ('Very Easy',
                    'you will wipe the floor with them.')
    elif x < 0: # x < 0 (Standard)
        mobPower = ('Easy', "this shouldn't take too much effort.")
    elif x <= set_challenging: # x <= 0 (Standard)
        mobPower = ('Challenging',
                    'if you stay alert, you should be fine.')
    elif x <= 4: # x <= 4 (Standard)
        mobPower = ('Very Difficult', 'use all of your resources.')
    elif x <= 7: # x <= 7 (Standard)
        mobPower = ('Overpowering', 'run away!')
    else:
        mobPower = ('Impossible',
                    'just start rolling up new characters.')
    return mobPower


# Original DifficultyPercent
def DifficultyPercent(x):
    enc_percent = ('Unknown', 'Unknown')
    if x < -4:
        enc_percent = "0%"
    elif x < 0:
        enc_percent = "10%"
    elif x <= set_challenging:
        enc_percent = "50%"
    elif x <= 4:
        enc_percent = "15%"
    elif x <= 7:
        enc_percent = "5%"
    else:
        enc_percent = "0%"
    return enc_percent


# Experimental version of DifficultyPercent
def DifficultyPercent2(x):
    # What percentage of an adventures encounters should be at this EL.
    p = 0
    if x < 0:
        p = 50 + (x * 20)
    elif x > 5:
        p = 15 - ((x-5) * 5)
    else:
        p = 50 - (x * 7)

    if (x <=8 and x > 5 and p <=2):
        p = 2 # special case guess.

    if (p < 0):
        p = 0

    p = int(round(p)) # smooth it out a bit.

    return "%s%%" % p


def Difference(x, y):
    return 2 * (crFormulas.Log2(x) - crFormulas.Log2(y))


# Difficulty formula for list of players vs list of monsters
# 1lv3 2lv4 = [(1.0, 3.0), (2.0, 4.0)]
# 1cr4 3cr2 = [(1.0, 4.0), (3.0, 2.0)]
def GetDifficulty(plrLst, monLst):
    PartyTotalPower = crFormulas.TotalPower(plrLst)
    MonsterTotalPower = crFormulas.TotalPower(monLst)
    return Difference(MonsterTotalPower, (PartyTotalPower / 4))


# Calculate difficulty, convert and return readable string
def DifficultyTextulator(plrLst, monLst):

    d = GetDifficulty(plrLst, monLst)

    EL = int(crFormulas.FoeEffectiveLevel(monLst))

    if EL < 1:
        EL = "< 1"

    returnTxt = (
    "Difficulty (EL %s): %s -- %s"
    #~ " (%s of Total)"
    % (EL,
    DifficultyAdvice(d)[0],
    DifficultyAdvice(d)[1],
    #~ DifficultyPercent(d)
    ))

    return returnTxt


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
