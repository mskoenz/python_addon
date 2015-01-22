#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Author:  Mario S. Könz <mskoenz@gmx.net>
# Date:    06.06.2013 15:00:17 EDT
# File:    color.py

import sys

NO_COLOR = False
#~ NO_COLOR = True

ALL_COLORS = ["BLACK", "BLACKB", "RED", "REDB", "GREEN", "GREENB", "YELLOW", "YELLOWB", "BLUE", "BLUEB", "MAGENTA", "MAGENTAB", "CYAN", "CYANB", "WHITE", "WHITEB", "BLACKBG", "REDBG", "GREENBG", "YELLOWBG", "BLUEBG", "MAGENTABG", "CYANBG", "WHITEBG", "NONE"]
ALL_COLORS_IMPL = ["\033[0;30m", "\033[1;30m", "\033[0;31m", "\033[1;31m", "\033[0;32m", "\033[1;32m", "\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[1;34m", "\033[0;35m", "\033[1;35m", "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;37m", "\033[0;40m", "\033[0;41m", "\033[0;42m", "\033[0;43m", "\033[0;44m", "\033[0;45m", "\033[0;46m", "\033[0;47m", "\033[0m"]

#------------------- special bash prompt ------------------- 
CLRSCR_ = "\033[2J\033[100A"
CLEAR_ = "\x1B[2K"
UP_ = "\033[1A"
RENTER_ = UP_ + CLEAR_

color = {}
if NO_COLOR:
    for i in range(len(ALL_COLORS)):
        exec(ALL_COLORS[i] + '_ = ""')
        if sys.version_info >= (3, 0):
            exec("def " + ALL_COLORS[i] + "(out, end = \"\\n\"):\n\tprint(str(out), end=end)")
        else:
            exec("def " + ALL_COLORS[i] + "(out, end = \"\\n\"):\n\tprint(str(out) + end),")
        color[ALL_COLORS[i].lower()] = ""
        color["clrscr"] = ""
        color["clear"] = ""
        color["up"] = ""
        color["renter"] = ""
else:
    for i in range(len(ALL_COLORS)):
        exec(ALL_COLORS[i] + '_ = "' + ALL_COLORS_IMPL[i] + '"')
        if sys.version_info >= (3, 0):
            exec("def " + ALL_COLORS[i] + "(out, end = \"\\n\"):\n\tprint(" + ALL_COLORS[i] +  "_ + str(out) + NONE_, end=end)")
        else:
            exec("def " + ALL_COLORS[i] + "(out, end = \"\\n\"):\n\tprint(" + ALL_COLORS[i] +  "_ + str(out) + NONE_ + end),")
        color[ALL_COLORS[i].lower()] = ALL_COLORS_IMPL[i]
        color["clrscr"] = CLRSCR_
        color["clear"] = CLEAR_
        color["up"] = UP_
        color["renter"] = RENTER_
            
