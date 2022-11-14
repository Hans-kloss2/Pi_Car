import RPi.GPIO as gpio

import time

gpio.setmode(gpio.BCM)

gpio.setup(24, gpio.OUT) #DIR1

gpio.setup(12, gpio.OUT) #PWM1


gpio.output(24, True)

p = gpio.PWM(12, 100)
p.start(50)

time.sleep(60)

gpio.cleanup()