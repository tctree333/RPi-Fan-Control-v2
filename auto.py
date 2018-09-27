# Import Modules
from gpiozero import OutputDevice
from time import sleep
from subprocess import check_output, PIPE, Popen
import sys

# Definitons
pin = 18 # Pin number
onTemp = 45 # Temperature ('C) to trigger fan (should be around 30-50 depending on fan)
delayTime = 60 # Delay (sec) between temperature checks

# Check to see if it is running somewhere else
processes = int(check_output(['pgrep', '-fc', 'python auto.py']))
if processes > 1:
	print "Error: Other Processes Running"
	sys.exit()

# Check to see if it is supposed to be running
with open('status', 'r') as f:
	state = int(f.read())
	f.close()
	if state != 1:
		print "Error: State != 1" , state
		sys.exit()

# Setup GPIO
fan = OutputDevice(18)

# Function to get temperature
def getTemp():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])

# Function to get status
def getState():
	with open('status', 'r') as f:
		state = int(f.read())
		f.close()
	return state


# Actual loop
while getState() == 1:
	if getTemp() > onTemp:
		# temperature too high
		fan.on()
	else:
		# temperature too low
		fan.off()
	sleep(delayTime)

print "Error: Exited While Loop", state
sys.exit()
