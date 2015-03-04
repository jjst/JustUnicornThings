#!/usr/bin/env python

import unicornhat as unicorn
import time
import sys
import itertools
import colorsys
import numpy as np
import signal
import random

unicorn.brightness(0.5)

def sigterm_handler(signal, frame):
    unicorn.clear()
    sys.exit(0)

signal.signal(signal.SIGTERM, sigterm_handler)

pixels_to_light = {
    (1, 1), (1, 2), (1, 5), (1, 6),
        (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
        (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
        (5, 2), (5, 3), (5, 4), (5, 5),
        (6, 3), (6, 4),
}

def draw_heart(hue, brightness):
  for x, y in pixels_to_light:
    color = colorsys.hsv_to_rgb(hue, 1, brightness)
    color = [int(c * 255) for c in color]
    r, g, b = color  
    unicorn.set_pixel(x, y, r, g, b)
  unicorn.show()


# For hue, generate floats between 1 -> 0. We want a lot of points
# as we want hue to move slowly.
hue_values = np.linspace(1, 0, 2000)
# For brightness, we want a sinusoid that changes fast. We also want
# the brightness to stay long, and the darkness to be short-lived, so
# we'll generate an uneven sinusoid using log values between 0 and pi,
# with the most values concentrated closer to 0 where the cos is greater.
base = 3
log_values = (np.logspace(0, 1, num=100, base=base) - 1)/(base - 1)
log_values = np.pi * np.append(log_values[::-1], log_values)
sinusoid = np.cos(log_values)
# We adjust the sinusoid to that it varies between 0 and 1
brightness_values = (sinusoid+ 1)/2.
hsv_variations = itertools.izip(
    hue_values,
    itertools.cycle(brightness_values))


for hue, brightness in hsv_variations:
   draw_heart(hue, brightness)
   time.sleep(0.002)
