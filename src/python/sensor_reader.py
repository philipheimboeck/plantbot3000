#!/usr/bin/env python

import serial

MAX_SENSOR_VALUE_MOIST = 1024
MAX_SENSOR_VALUE_LIGHT = 1024

class SensorReader(object):
	"""docstring for SensorReader"""

	moist = 0
	light = 0

	def __init__(self):
		super(SensorReader, self).__init__()
		self.ser = serial.Serial('/dev/ttyACM0',9600)
		# self.ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

	def read(self):
		line = self.ser.readline().strip()
		numbers = line.split(';')
		self.moist = int (numbers[0], 16)
		self.light = int (numbers[1], 16)

	def getLightValue(self):
		return self.light

	def getMoistValue(self):
		return self.moist

	def getLightPercentage(self):
		return self.light/MAX_SENSOR_VALUE_LIGHT * 100

	def getMoistPercentage(self):
		return self.moist/MAX_SENSOR_VALUE_MOIST * 100
