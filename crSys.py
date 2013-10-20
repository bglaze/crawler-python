#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  System Functions module for Crawler I
#  by Brock Glaze
#
#  crSys.py


import os


def opj(path):
    """Convert paths to the platform-specific separator"""
    str = apply(os.path.join, tuple(path.split('/')))
    # HACK: on Linux, a leading / gets lost...
    if path.startswith('/'):
        str = '/' + str
    return str


if __name__ == '__main__':
    pass
