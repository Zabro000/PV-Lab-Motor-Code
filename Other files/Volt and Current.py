from Phidget22.Phidget import *
from Phidget22.Devices.CurrentInput import *
import time

def onCurrentChange(self, current):
	print("Current: " + str(current))

def main():
	currentInput0 = CurrentInput()

	currentInput0.setOnCurrentChangeHandler(onCurrentChange)

	currentInput0.openWaitForAttachment(5000)

	try:
		input("Press Enter to Stop\n")
	except (Exception, KeyboardInterrupt):
		pass

	currentInput0.close()

main()