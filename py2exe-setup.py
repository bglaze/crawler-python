#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(
    windows = [
        {
        "script": "crawler.pyw",
        "icon_resources": [(0, 'images/icon.ico')]
        }
    ],
)
