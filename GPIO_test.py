import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM) # GPIO Nummern statt Board Nummern

aktive_gpio = [17, 21, 22, 23, 24, 10, 9, 11]

for relais in aktive_gpio:
	GPIO.setup(relais, GPIO.OUT) #GPIO Modus zuweisen

	# RELAIS_1_GPIO = 17

for relais in aktive_gpio: #machma an und wieder aus
	GPIO.output(relais, GPIO.LOW) # aus
	sleep(0.5)
	GPIO.output(relais, GPIO.HIGH) # an
	sleep(0.10)
	GPIO.output(relais, GPIO.LOW) #aus
	sleep(0.5)
	GPIO.output(relais, GPIO.HIGH) # an
	sleep(0.10)
	GPIO.output(relais, GPIO.LOW) #aus
