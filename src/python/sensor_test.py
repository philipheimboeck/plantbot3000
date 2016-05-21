#!/usr/bin/env python

import re, sys, os

from sensor_reader import SensorReader

reader = SensorReader()

reader.read()
print("Light value: %d" % (reader.getLightValue()))
print("Moist value: %d" % (reader.getMoistValue()))
print("Light level: %d" % (reader.getLightPercentage()))
print("Moist level: %d" % (reader.getMoistPercentage()))
