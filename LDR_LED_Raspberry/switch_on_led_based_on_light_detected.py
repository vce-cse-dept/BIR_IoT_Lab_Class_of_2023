import RPi.GPIO as GPIO
import time
ldr = 18
led    = 22
GPIO.setmode(BOARD)
GPIO.setup(led, GPIO.OUT)
while True:
	count=0
	GPIO.setup(ldr, GPIO.OUT)
	GPIO.output(ldr, GPIO.LOW)
	time.sleep(0.5)
	GPIO.setup(ldr, GPIO.IN)
	while (GPIO.input(ldr)==GPIO.LOW):
		count+=1
	print("count: ",count)
	if (count>=10000):
		GPIO.output(led, GPIO.HIGH)
	else
		GPIO.output(led, GPIO.LOW)
	time.sleep(0.5)