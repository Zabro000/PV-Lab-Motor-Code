# How to install and activate a venv
# https://python.land/virtual-environments/virtualenv
# https://virgo.readthedocs.io/en/latest/
# venv\Scripts\Activate.ps1
# https://virgo.readthedocs.io/en/latest/reference.html
# https://docs.python.org/3/library/time.html

from Phidget22.Phidget import *
from Phidget22.Devices.VoltageInput import *
import time

def onVoltageChange(self, voltage):
	print("Voltage: " + str(voltage))

def main():
	voltageInput0 = VoltageInput()

	voltageInput0.setOnVoltageChangeHandler(onVoltageChange)

	voltageInput0.openWaitForAttachment(5000)

	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass

	voltageInput0.close()

main()



def phidget_test() -> None:
	...

