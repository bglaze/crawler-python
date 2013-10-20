#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Experience Calculator for Crawler I
#  by Brock Glaze
#
#  crCalc_Experience.py


import crawler
import crFormulas
import math
import wx


#-----------------------------------------------------------------------
#------ Calculate Experience -------------------------------------------
#-----------------------------------------------------------------------


def CalculateExperience(x, y):
    # x = Character Level y = Monster Level
    i = 0
    if x < 3:
        x = 3
    if (x <= 6) and (y <= 1):
        i = 300 * y
    elif y < 1:
        i = 0
    else:
        i = (
        6.25 * x * (math.pow(2, crFormulas.EvenUp(7 -
        (x - y)) / 2)) * (11 - (x - y) -
        crFormulas.EvenUp(7 - (x - y)))
        )

    if (y == 4 or y == 6 or y == 8 or y == 10
    or y == 12 or y == 14 or y == 16 or y == 18
    or y == 20):

        if x <= 3:
            i = 1350 * math.pow(2, (y - 4) / 2)
        elif (x == 5 and y >= 6):
            i = 2250 * math.pow(2, (y - 6) / 2)
        elif (x == 7 and y >= 8):
            i = 3150 * math.pow(2, (y - 8) / 2)
        elif (x == 9 and y >= 10):
            i = 4050 * math.pow(2, (y - 10) / 2)
        elif (x == 11 and y >= 12):
            i = 4950 * math.pow(2, (y - 12) / 2)
        elif (x == 13 and y >= 14):
            i = 5850 * math.pow(2, (y - 14) / 2)
        elif (x == 15 and y >= 16):
            i = 6750 * math.pow(2, (y - 16) / 2)
        elif (x == 17 and y >= 18):
            i = 7650 * math.pow(2, (y - 18) / 2)
        elif (x == 19 and y >= 20):
            i = 8550 * math.pow(2, (y - 20) / 2)

    if (y == 7 or y == 9 or y == 11 or y == 13
    or y == 15 or y == 17 or y == 19):

        if x == 6:
            i = 2700 * math.pow(2, (y - 7) / 2)
        if (x == 8 and y >= 9):
            i = 3600 * math.pow(2, (y - 9) / 2)
        if (x == 10 and y >= 11):
            i = 4500 * math.pow(2, (y - 11) / 2)
        if (x == 12 and y >= 13):
            i = 5400 * math.pow(2, (y - 13) / 2)
        if (x == 14 and y >= 15):
            i = 6300 * math.pow(2, (y - 15) / 2)
        if (x == 16 and y >= 17):
            i = 7200 * math.pow(2, (y - 17) / 2)
        if (x == 18 and y >= 19):
            i = 8100 * math.pow(2, (y - 19) / 2)

    # Next we'll use recursion.
    # This is a clean way to make sure that any errors
    # in the formula are taken care of.
    if y > 20:
        i = 2 * CalculateExperience(x, y - 2)

    if (x - y) > 7:
        i = 0
    elif (y - x) > 7:
        i = 0
    return i


# Calculate experience, convert and return list of readable strings
def ExperienceTextulator(plrLst, monLst):
    # 1lv3 2lv4 = [(1.0, 3.0), (2.0, 4.0)]
    # 1cr4 3cr2 = [(1.0, 4.0), (3.0, 2.0)]
    returnLst = []
    PartyTotal = crFormulas.CountChars(plrLst)
    plrCount = 0
    plrDict = {}

    for i in plrLst:
        for x in range(int(i[0])):
            plrCount += 1
            expCount = 0
            for i2 in monLst:
                for x2 in range(int(i2[0])):
                    expCount += CalculateExperience(i[1], i2[1]) / PartyTotal

            plrDict[i[1]] = (i[0], expCount)


    for i in sorted(plrDict.items()):
        returnLst.append(
        'Experience: Level %d (%d players): %d xp each' % (i[0], i[1][0], i[1][1])
        )

    return returnLst


#-----------------------------------------------------------------------
#------ Console Mode ---------------------------------------------------
#-----------------------------------------------------------------------


def PrintIntro():
    print 'D&D Experience Calculator Module'


def GetMonsters():
    print '\n[Enter Monsters]'
    print 'Format > 2cr2 1cr3'
    inpLst, monLst = raw_input('> ').split(), []
    for i in inpLst:
        aLst = i.split('cr')
        monLst.append((float(aLst[0]), float(aLst[1])))
    print
    return monLst


def GetPlayers():
    print '\n[Enter Players]'
    print 'Format > 1lv3 3lv4 1lv5'
    inpLst, plrLst = raw_input('> ').split(), []
    for i in inpLst:
        aLst = i.split('lv')
        plrLst.append((float(aLst[0]), float(aLst[1])))
    return plrLst


def Console():
    PrintIntro()
    option = 'unknown'
    while option.upper() != str('Q'):
        option = raw_input("\n\nType 'calc' or 'q'\n> ")
        if option == 'calc':
            plrLst = GetPlayers()
            monLst = GetMonsters()
            for line in ExperienceTextulator(plrLst, monLst):
                print "%s\n" % line,

    print '\nGoodbye\n'


#***********************************************************************


if __name__ == "__main__":
    #~ crawler.Main()
    Console()
