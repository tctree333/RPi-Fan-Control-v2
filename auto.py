from gpiozero import OutputDevice
from time import sleep
import subprocess
import sys

pin = 18
processes = int(subprocess.check_output(['pgrep', '-fc', 'python auto.py']))
relay = OutputDevice(pin)

if processes > 1:
	sys.exit()

with open('status', 'r') as f:
	if int(f.read()) == 0:
		sys.exit()



