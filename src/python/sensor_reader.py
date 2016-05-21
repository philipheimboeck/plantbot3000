#!/usr/bin/env python

import serial

MAX_SENSOR_VALUE_MOIST = 1023
MAX_SENSOR_VALUE_LIGHT = 1023

class SensorReader(object):
	"""docstring for SensorReader"""

	moist = 0
	light = 0

	def __init__(self):
		super(SensorReader, self).__init__()
		self.ser = serial.Serial('/dev/ttyACM0',9600)
		# self.ser = serial.Serial('/dev/cu.usbmodem1411', 9600)

	def read(self):
		# Write to arduino so it answers with current values
		self.ser.write("get".encode())

		# Get the data
		line = self.ser.readline().strip()
		numbers = line.split(';')
		self.moist = int (numbers[0], 16)
		self.light = int (numbers[1], 16)

	def getLightValue(self):
		return self.light

	def getMoistValue(self):
		return self.moist

	def getMoistPercentage(self):
		return 100-float(self.moist)/MAX_SENSOR_VALUE_MOIST * 100
