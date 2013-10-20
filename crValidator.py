#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  An alpha/digit validator class for Crawler I
#  by Brock Glaze
#
#  crValidator.py

from __future__ import division, print_function
import crawler
import string
import wx


ALPHA_ONLY = 1
DIGIT_ONLY = 2
DIGIT_MINUS_ONLY = 3
DIGIT_DECIMAL_ONLY = 4


# List of digits including "-" for negative numbers
digits_minus = string.digits[:]
digits_minus += "-"

# List of digits including "." for decimal numbers
digits_decimal = string.digits[:]
digits_decimal += "."



class Validator(wx.PyValidator):
    def __init__(self, flag=None, pyVar=None):
        wx.PyValidator.__init__(self)
        self.flag = flag
        self.Bind(wx.EVT_CHAR, self.OnChar)


    def Clone(self):
        return Validator(self.flag)


    def Validate(self, win):
        tc = self.GetWindow()
        val = tc.GetValue()

        if self.flag == ALPHA_ONLY:
            for x in val:
                if x not in string.letters:
                    return False

        elif self.flag == DIGIT_ONLY:
            for x in val:
                if x not in string.digits:
                    return False

        elif self.flag == DIGIT_MINUS_ONLY:
            for x in val:
                if x not in digits_minus:
                    return False

        elif self.flag == DIGIT_DECIMAL_ONLY:
            for x in val:
                if x not in digits_decimal:
                    return False

        return True


    def OnChar(self, event):
        tc = self.GetWindow()
        val = tc.GetValue()
        key = event.GetKeyCode()

        if key < wx.WXK_SPACE or key == wx.WXK_DELETE or key > 255:
            event.Skip()
            return

        if self.flag == ALPHA_ONLY and chr(key) in string.letters:
            event.Skip()
            return

        if self.flag == DIGIT_ONLY and chr(key) in string.digits:
            event.Skip()
            return

        if self.flag == DIGIT_MINUS_ONLY and chr(key) in digits_minus:
            if (chr(key) != "-" or
            (chr(key) == "-"
            and ("-" not in val or tc.GetSelection()[0] == 0)
            and (tc.GetInsertionPoint() == 0 or tc.GetSelection()[0] == 0)
            )):
                event.Skip()
                return

        if self.flag == DIGIT_DECIMAL_ONLY and chr(key) in digits_decimal:
            if (chr(key) != "." or
            (chr(key) == "."
            and ("." not in val or tc.GetSelection()[0] == 0)
            and (tc.GetInsertionPoint() == 0 or tc.GetSelection()[0] == 0)
            )):
                event.Skip()
                return

        if not wx.Validator_IsSilent():
            #~ wx.Bell()
            pass

        # Returning without calling event.Skip eats the event before it
        # gets to the text control
        return


#***********************************************************************


if __name__ == '__main__':
    crawler.Main()
