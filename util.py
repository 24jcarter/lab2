import RPi.GPIO as GPIO
from time import sleep

def switchPressed(pin):
	ledpwm = GPIO.PWM(pin, 100)
	ledpwm.start(0)
	for duty in range(101):
		ledpwm.ChangeDutyCycle(duty)
		sleep(0.01) 
	for duty in range(100, -1, -1):
		ledpwm.ChangeDutyCycle(duty)
		sleep(0.01)
	