#!/usr/bin/env python

import serial

# ser = serial.Serial('/dev/ttyACM0',9600)
ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
while True:
	line = ser.readline().strip()

	numbers = line.split(';')
	print numbers
	moist = int (numbers[0], 16)
	light = int (numbers[1], 16)
	print moist
	print light
