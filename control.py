import threading
import os
import RPi.GPIO as GPIO
PIN = 4
SINIR = 59

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN,GPIO.OUT)

def printit():
	threading.Timer(5.0, printit).start()
	temp = float(os.popen("vcgencmd measure_temp").readline().split('=')[1].split('\'')[0]);
	if temp > SINIR:
		print("{} fan çalıştı.".format(temp))
		GPIO.output(PIN,GPIO.HIGH)
	else:
		print("{} fan durdu".format(temp))
		GPIO.output(PIN,GPIO.LOW)
		
printit()


