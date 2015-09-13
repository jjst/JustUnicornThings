#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 13:56:19 2015
"""
from __future__ import division
import unicornhat as UH
import time
import random
import datetime
import signal

UH.brightness(1.0)

EXIT = False

def sigterm_handler(signal, frame):
    global EXIT
    EXIT = True

signal.signal(signal.SIGTERM, sigterm_handler)

def rainbow_clock():
    while not EXIT:
        rgb_value=datetime.datetime.now().time()
        r=rgb_value.hour
        r= int( (r / 23) * 255)
        g=rgb_value.minute
        g= int( (g / 59) * 255)
        b=rgb_value.second
        b=int((b / 59) * 255)
        for i in range(8):
            for j in range(8):
                UH.set_pixel(i,j,r,g,b)
        UH.show()
        time.sleep(1)
        print datetime.datetime.now().time()
        print r,g,b
    UH.clear()
    UH.show()
rainbow_clock()
