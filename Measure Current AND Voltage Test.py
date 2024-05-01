from Phidget22.Phidget import *
from Phidget22.Devices.CurrentInput import *
from Phidget22.Devices.VoltageInput import *
import time

def onCurrentChange(self, current):
	print("Current: " + str(current))

def onVoltageChange(self, voltage):
	print("Voltage: " + str(voltage))


def main():
	currentInput0 = CurrentInput()
	voltageInput0 = VoltageInput()

	currentInput0.setOnCurrentChangeHandler(onCurrentChange)
	voltageInput0.setOnVoltageChangeHandler(onVoltageChange)
	

	currentInput0.openWaitForAttachment(5000)
	voltageInput0.openWaitForAttachment(5000)

	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass

	currentInput0.close()
	voltageInput0.close()

main()


