import RPi.GPIO as gpio

import time


gpio.setmode(gpio.BCM)

gpio.setup(14, gpio.OUT) #DIR1

gpio.setup(1, gpio.OUT) #PWM1


gpio.output(14, True)

p = gpio.PWM(12, 50)
p.start()

time.sleep(60)

gpio.cleanup()