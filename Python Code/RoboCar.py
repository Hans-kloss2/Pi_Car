import RPi.GPIO as gpio

import time
gpio.cleanup()

gpio.setmode(gpio.BCM)

gpio.setup(14, gpio.OUT) #DIR1

gpio.setup(1, gpio.OUT) #PWM1


gpio.output(14, True)

p = gpio.PWM(1, 100)
p.start(0)

time.sleep(60)

gpio.cleanup()