from Phidget22.Phidget import *
from Phidget22.Devices.VoltageInput import *
import time
import keyboard

recording = False
high_voltage_list = []
low_voltage_list = []
all_voltage_list = []

def onVoltageChange(self, voltage):
    print("Voltage: " + str(voltage))
    all_voltage_list.append(voltage)
    
    if recording:
        if voltage > 2:
            high_voltage_list.append(voltage)
        else:
            low_voltage_list.append(voltage)

ch = VoltageInput()

# Register for event before calling open
ch.setOnVoltageChangeHandler(onVoltageChange)

ch.open()

while True:
    if keyboard.is_pressed(' '):
        recording = not recording
        if recording:
            print("Recording started.")
        else:
            print("Recording stopped.")
        time.sleep(0.3)  # Debounce time to prevent multiple toggles from one press
    
    if keyboard.is_pressed('s'):
        recording = False
        print("Recording stopped by user.")
        time.sleep(0.3)
    # Do work, wait for events, etc.
    time.sleep(0.1)
    if not recording:
        continue


# Print the recorded voltages
print("High Voltage List:", sorted(high_voltage_list))
print("Low Voltage List:", sorted(low_voltage_list))
print("All Voltage List:", sorted(all_voltage_list))




