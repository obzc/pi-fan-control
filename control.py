import threading
import os
import RPi.GPIO as GPIO

PIN = 4
MAX_TEMP = 63
MIN_TEMP = 56
FAN_STATUS = "OFF"
TIMER = 10.0

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT)


def printit():
	global FAN_STATUS
	threading.Timer(TIMER, printit).start()
	temp = float(os.popen("vcgencmd measure_temp").readline().split('=')[1].split('\'')[0])
	if temp > MAX_TEMP:
		GPIO.output(PIN,GPIO.HIGH)
		FAN_STATUS = "ON"
	elif (temp < MIN_TEMP):
		GPIO.output(PIN,GPIO.LOW)
		FAN_STATUS = "OFF"

	print("C: {} | F: {}".format(temp, FAN_STATUS))


printit()


