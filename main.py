import RPi.GPIO as GPIO
import util

GPIO.setmode(GPIO.BCM)

led1 = 4
led2 = 17
led3 = 27

GPIO.setup(led1, GPIO.OUT, initial=0)
GPIO.setup(led2, GPIO.OUT, initial=0)
GPIO.setup(led3, GPIO.OUT, initial=0)

switch1 = 22
switch2 = 5

GPIO.setup(switch1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switch2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

led3pwm = GPIO.PWM(led3, 1)
led3pwm.start(50)

try:
	while True:
		if GPIO.input(switch1) == 1:
			util.switchPressed(led1)
		if GPIO.input(switch2) == 1:
			util.switchPressed(led2)
except KeyboardInterrupt:
	led3pwm.stop()
	GPIO.cleanup()
	print("Exiting...")
