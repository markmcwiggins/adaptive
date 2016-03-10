#!/usr/bin/env python

import os

for i in range(100):
    os.system("./randhand.py >y%d.dat" % (i + 1))
