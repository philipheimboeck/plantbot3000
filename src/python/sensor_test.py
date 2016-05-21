#!/usr/bin/env python

import re, sys, os, time

from sensor_reader import SensorReader

reader = SensorReader()

while(True):
    reader.read()
    print("Light value: %d" % (reader.getLightValue()))
    print("Moist value: %d" % (reader.getMoistValue()))
    print("Light level: %d" % (reader.getLightPercentage()))
    print("Moist level: %d" % (reader.getMoistPercentage()))
    time.sleep(1)
