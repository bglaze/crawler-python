#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Treasure Generators for Crawler I
#  by Brock Glaze
#
#  crDice.py


import crawler
import random
import wx


def RollDice(x, die):
    # Roll any number of any-sided dice
    lst_each_die = []
    total = 0
    for n in xrange(x):
        roll = random.randint(1, die)
        lst_each_die.append(roll)
        total += roll

    #~ print "\n-----\n%dd%d\n%d\n-----" % (x, die, total)

    return (lst_each_die, total)


def RollPercentage():
    # Roll two 10-siders, concatenate the two and return the result
    tens = random.randint(0, 9)
    hundreds = random.randint(0, 9)

    # 00 = 100
    if tens == 0 and hundreds == 0:
        perc = 100
    else:
        perc = int("%d%d" % (tens, hundreds))

    #~ print "Percentage: %d%%" % perc

    return ((tens, hundreds), perc)


def RollAttributes():
    # Roll 4 6-siders 6 times
    lst_attributes_and_scores = []
    lst_attribute_dice = []
    for n in xrange(6):

        lst_each_die = []
        for n in xrange(4):
            roll = random.randint(1, 6)
            lst_each_die.append(roll)
            lst_each_die.sort()
            lst_each_die.reverse()

        lst_attribute_dice.append(tuple(lst_each_die))

    for a in lst_attribute_dice:
        lst_attributes_and_scores.append((sum(a[:3]), a))

    return tuple(reversed(sorted(lst_attributes_and_scores)))


#***********************************************************************


if __name__ == "__main__":
    crawler.Main()
