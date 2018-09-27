import sys
from gpiozero import OutputDevice

pin = 18
arg = str(sys.argv[1])
fan = OutputDevice(pin)

fan.on()

state = fan.value

print state
